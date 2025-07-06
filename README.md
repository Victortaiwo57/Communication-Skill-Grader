# Communication-Skill-Grader
A simple and intelligent scoring tool for grading communication tests using grammar, clarity, tone, and writing structure.


# Communication Test Grader

This project is a lightweight tool designed to automatically evaluate written communication tests. It scores user responses based on grammar, spelling, structure, clarity, tone, and overall communication effectiveness.

## ✨ Features

- ✅ Grammar and spelling detection
- ✅ Evaluation of clarity and tone
- ✅ Feedback generation (optional)
- ✅ Scalable and extendable with NLP tools

## 🚀 Use Cases

- Screening candidates during recruitment
- Grading written assessments in training programs
- Literacy/communication benchmarks for drivers or field agents

## ⚙️ Technologies Used

- Python 3.10+
- NLTK 
- Python shiny
- Pandas & Regex (for text processing)

## 🧠 How It Works

The system assigns a score based on:
- **Grammar Error** min(grammar_errors * 2.5, 30)
- **Default Score for all submission** (55%)
- **keyword_hits** min(keyword_hits * 2, 20)
- **vocab_score** min(vocab_score * 15, 15)
- **Word count** (if word count < 50 :(-40%), if word count > 50 < 100: (5%), if word count >100 :(10%)


