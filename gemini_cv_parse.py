import pathlib, fitz

from google import genai

filepath = pathlib.Path("/cv.pdf")

def get_cv_text(path):
    # Read the file content
    try:
        cv_text = ""
        with fitz.open(path) as doc:
            for page in doc:
                cv_text += page.get_text()
        return cv_text
    except FileNotFoundError:
        print(f"Error: The file was not found at {path}")
        exit()
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        exit()

prompt = """ You are an expert AI data extractor. Your sole task is to analyze the text of a curriculum vitae (CV) and convert it into a structured, valid JSON object based on the provided schema.

**Follow these instructions precisely:**
1.  Analyze the CV text provided within the `<cv_text>` tags.
2.  Extract the information and map it to the fields defined in the `<json_schema>`.
3.  **Date Formatting:** For `start_date` and `end_date`, normalize dates to `YYYY-MM` format if possible. If a month is not present, `YYYY` is acceptable. For currently held positions, use "Present" for the `end_date`.
4.  **Handling Missing Information:** If a specific piece of information (e.g., `linkedin_url`) is not found, the value for that key must be `null`.
5.  **Empty Sections:** If an entire section (like `certifications` or `projects`) is absent from the CV, return an empty array `[]` for that key.
6.  **Responsibilities:** Extract job responsibilities as a list of concise strings, with each string representing a distinct point or task.
7.  **Output:** Your response **must** be only the JSON object, enclosed in a single markdown code block (` ```json ... ``` `). Do not include any introductory text, explanations, or apologies.

<json_schema>
{{
"personal_information": {{
    "name": "string or null",
    "email": "string or null",
    "phone": "string or null",
    "linkedin_url": "string or null",
    "github_url": "string or null",
    "address": "string or null"
  }},
"summary": "string or null",
"work_experience": [
    {{
      "job_title": "string or null",
      "company_name": "string or null",
      "location": "string or null",
      "start_date": "YYYY-MM or string or null",
      "end_date": "YYYY-MM or string or Present or null",
      "responsibilities": [
        "string"
      ]
    }}
  ],
  "education": [
    {{
      "degree": "string or null",
      "institution": "string or null",
      "location": "string or null",
      "graduation_year": "YYYY or string or null"
    }}
  ],
  "skills": {{
    "technical": ["string"],
    "soft_skills": ["string"],
    "languages": ["string"]
  }},
  "certifications": [
    {{
      "name": "string or null",
      "issuing_organization": "string or null",
      "year": "YYYY or string or null"
    }}
  ],
  "projects": [
      {{
          "project_name": "string or null",
          "description": "string or null",
          "technologies_used": ["string"]
      }}
  ]
}}
</json_schema>

**Now, parse the following CV text:**
<cv_text>
{cv_text}
</cv_text>

"""

full_prompt = prompt.format(cv_text=get_cv_text(filepath))

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=full_prompt,
    config={
        "response_mime_type": "application/json",
    },
)

# Extract and print only the JSON text part
json_text = response.candidates[0].content.parts[0].text
print(json_text)
