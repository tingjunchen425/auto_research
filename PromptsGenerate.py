import google.generativeai as generativeai
from output_translate import markdown_json_to_python_list
import dotenv
import os

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class PromptsGenerate:
    def __init__(self):
        self.system_prompts = f"""
        According to the user's needs, generate prompts
        If there are several prompts, return the most suitable one
        Return the response in json format.The output should be a JSON dict with one field: 1. prompt(str): The prompt generated
        Make sure to return the response in json format : ```json
        ...
        """
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=self.system_prompts
        )

    def tavily_tasks(self, prompt):
        prompt = f"Generate a query for tavily api to search about {prompt}"
        self.chat = self.model.start_chat()
        response = self.chat.send_message(prompt)
        response = markdown_json_to_python_list(response.text)
        return response