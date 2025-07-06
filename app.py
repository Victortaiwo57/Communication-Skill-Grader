import logging
import language_tool_python
from shiny import App, ui, reactive, render, Inputs, Outputs
from nltk.tokenize import word_tokenize, sent_tokenize

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

tool = language_tool_python.LanguageTool('en-US')
# Grading logic (same as before)
def grade_application(text):
    #tool = language_tool_python.LanguageTool('en-US')
    keywords = [
        "safety", "passion", "driver", "professional", "reliable", "customer",
        "service", "experience", "transportation", "platform", "record", "license",
        "local", "knowledge", "familiar", "hard", "working", "motivated",
        "love", "driving", "punctual", "committed", "sincere"
    ]

    word_count = len(word_tokenize(text))
    sentence_count = len(sent_tokenize(text))

    if word_count < 50:
        count = -40
    elif word_count > 100:
        count = 10
    else:
        count = 5

    matches = tool.check(text)
    grammar_errors = len(matches)
    keyword_hits = sum(1 for word in word_tokenize(text.lower()) if word in keywords)
    vocab = set(word_tokenize(text.lower()))
    vocab_score = len(vocab) / word_count

    score = 55
    score -= min(grammar_errors * 2.5, 30)
    score += min(keyword_hits * 2, 20)
    score += min(vocab_score * 15, 15)
    score += count

    score = min(max(score, 0), 95)

    if score >= 80:
        level = "Excellent"
    elif score >= 70:
        level = "Great"
    elif score >= 50:
        level = "Good"
    elif score >= 40:
        level = "Fair"
    else:
        level = "Poor"

    return {
        "score": round(score, 1),
        "word_count": word_count,
        "grammar_errors": grammar_errors,
        "keyword_hits": keyword_hits,
        "vocabulary_score": round(vocab_score, 2),
        "level": level
    }

# UI
app_ui = ui.page_fluid(
    ui.h2("TOCH Communication Test Grader"),
    ui.input_text_area("application_text", "Paste applicant response here:", rows=10, width="100%"),
    ui.input_action_button("submit_btn", "Submit for Grading", class_="btn btn-primary"),
    ui.output_ui("grading_status"),
    ui.output_text_verbatim("grading_result")
)

# Server
def server(input, output, session):
    graded_result = reactive.Value(None)
    grading_status = reactive.Value("")

    @reactive.Effect
    @reactive.event(input.submit_btn)
    def process_application():
        text = input.application_text().strip()
        if not text:
            graded_result.set(None)
            grading_status.set("Please enter a valid application.")
            return

        grading_status.set("Grading in progress...")
        logging.info("Grading started.")
        
        result = grade_application(text)
        graded_result.set(result)

        grading_status.set("Grading complete.")
        logging.info("Grading complete with score: %s", result["score"])

    @output
    @render.ui
    def grading_status_ui():
        return grading_status.get()

    @output
    @render.text
    def grading_result():
        result = graded_result.get()
        if result:
            return (
                f"Score: {result['score']}% ({result['level']})\n"
                f"Word Count: {result['word_count']}\n"
                f"Grammar Errors: {result['grammar_errors']}\n"
                f"Keyword Hits: {result['keyword_hits']}\n"
                f"Vocabulary Score: {result['vocabulary_score']}"
            )
        return ""

# App
app = App(app_ui, server)
