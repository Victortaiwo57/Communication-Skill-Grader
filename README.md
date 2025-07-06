# Communication-Skill-Grader
A simple and intelligent scoring tool for grading communication tests using grammar, clarity, tone, and writing structure.


# Communication Test Grader

This project is a lightweight tool designed to automatically evaluate written communication tests. It scores user responses based on grammar, spelling, structure, clarity, tone, and overall communication effectiveness.

## ✨ Features

- ✅ Automated scoring from 0% to 100%
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
- spaCy / TextBlob / NLTK (choose your NLP library)
- Flask or Streamlit (for web interface, optional)
- Pandas & Regex (for text processing)

## 🧠 How It Works

The system assigns a score based on:
- **Grammar** (25%)
- **Spelling** (20%)
- **Clarity & Coherence** (25%)
- **Relevance & Tone** (20%)
- **Structure & Formatting** (10%)

Each section is analyzed and combined into a weighted final score between **0% and 100%**.

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/communication-test-grader.git
cd communication-test-grader
pip install -r requirements.txt
