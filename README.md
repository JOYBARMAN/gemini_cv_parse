# 🤖 AI CV Parser (Gemini API)

🚀 An **AI-powered CV/Resume parsing system** built using **Google Gemini API**, designed to extract structured information from unstructured resumes with high flexibility and accuracy.

---

## 🧠 Overview

This project demonstrates how to use **LLM-based AI models** to transform unstructured CVs into structured, machine-readable data.

Unlike traditional rule-based parsers, this system leverages **Generative AI (Gemini)** to handle **different CV formats, layouts, and writing styles**.

---

## ⚙️ Tech Stack

* **Language:** Python
* **AI Model:** Google Gemini API
* **Processing:** Prompt Engineering + Text Parsing
* **Environment:** CLI / Script-based

---

## 🏗️ How It Works

1. User provides a CV (text/PDF content)
2. Content is sent to **Gemini AI model**
3. AI extracts structured data such as:

   * Name
   * Contact information
   * Skills
   * Experience
   * Education
4. Output is returned in **structured JSON format**

---

## 🔥 Features

* 📄 Parse CVs with **different formats and layouts**
* 🤖 AI-powered extraction using Gemini
* 🧠 Handles unstructured and inconsistent data
* 📦 Structured JSON output
* ⚡ Flexible and extensible parsing logic

---

## 📂 Project Structure

```id="z9x1p3"
gemini_cv_parse/
│── main.py
│── parser/
│── prompts/
│── utils/
│── requirements.txt
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```id="p1x7ka"
git clone https://github.com/JOYBARMAN/gemini_cv_parse.git
cd gemini_cv_parse
```

---

### 2️⃣ Install dependencies

```id="j8s2lp"
pip install -r requirements.txt
```

---

### 3️⃣ Setup environment variables

Create a `.env` file:

```id="l2n8qw"
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```id="h7q2zs"
python main.py --file sample_cv.pdf
```

---

## 📤 Example Output

```json id="9s8d1k"
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": ["Python", "Django", "REST APIs"],
  "experience": [
    {
      "company": "ABC Corp",
      "role": "Software Engineer",
      "duration": "2 years"
    }
  ],
  "education": [
    {
      "degree": "BSc in Computer Science",
      "institution": "XYZ University"
    }
  ]
}
```

---

## 🧠 Why AI Instead of Rules?

Traditional CV parsers break when:

* Format changes
* Layout is inconsistent
* Sections are unordered

This system uses **LLM reasoning** to:

* Understand context
* Adapt to different CV styles
* Extract meaningful structured data

---

## 📈 Future Improvements

* Add **confidence scoring for extracted fields**
* Support **bulk CV processing**
* Build **REST API service** for integration
* Add **frontend dashboard for recruiters**
* Fine-tune prompts for higher accuracy

---

## 🧩 Use Cases

* Recruitment platforms
* HR automation tools
* Applicant tracking systems (ATS)
* Resume analysis tools

---

## 📫 Author

**Joy Barman**

* GitHub: https://github.com/JOYBARMAN
* LinkedIn: https://linkedin.com/in/joy-barman/

---

## ⚡

> “AI is not just automation — it’s understanding unstructured data at scale.”

---

⭐ If you find this useful, consider giving it a star!
