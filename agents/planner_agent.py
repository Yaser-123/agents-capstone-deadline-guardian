
# planner_agent.py
# LLM-powered Planner Agent using Gemini

import google.generativeai as genai
from config import get_gemini_api_key

class PlannerAgent:
    def __init__(self, model_name="gemini-2.5-flash"):
        # Configure Gemini
        api_key = get_gemini_api_key()
        genai.configure(api_key=api_key)

        # Initialize the model
        self.model = genai.GenerativeModel(model_name)

    def plan_tasks(self, user_input):
        """
        Uses Gemini to intelligently break the user request into steps.
        """

        print("[PlannerAgent] Planning tasks with Gemini...")

        prompt = f"""
        Break the following request into 3–5 clear, actionable steps.
        Return ONLY a JSON list of strings.
        
        Request: "{user_input}"
        """

        response = self.model.generate_content(prompt)
        text = response.text

        # Clean up markdown code fences if present
        import json
        if text.strip().startswith("```"):
            # Remove code fences
            lines = text.strip().split("\n")
            text = "\n".join(lines[1:-1]) if len(lines) > 2 else text

        # Fallback if Gemini doesn't return JSON
        try:
            tasks = json.loads(text)
        except:
            # Simple fallback: split by newlines
            tasks = [line.strip("-• \"") for line in text.split("\n") if line.strip() and line.strip() not in ["[", "]", "```", "```json"]]

        print("[PlannerAgent] Gemini-generated tasks:", tasks)
        return tasks
