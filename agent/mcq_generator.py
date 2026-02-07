from google import genai
import json
import re

class MCQGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-flash-latest"

    def generate_questions(self, topic, count):
        prompt = f"""
Generate {count} multiple-choice questions on {topic}.

Return ONLY valid JSON in this exact format:
[
  {{
    "question": "Question text",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer_idx": 0
  }}
]

Rules:
- No explanations
- No markdown
- JSON only
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        text = response.text
        match = re.search(r"\[.*\]", text, re.S)
        if not match:
            raise ValueError("Model did not return valid JSON")

        return json.loads(match.group())
