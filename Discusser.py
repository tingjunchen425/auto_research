import google.generativeai as generativeai
from output_translate import markdown_json_to_python_list
import dotenv
import os

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Discusser:
    def __init__(self, topic: str):
        self.topic = topic
        self.system_prompts = f"""
        Discuss the problem according the topic:{self.topic}, you are going to discuss with another AI model or human
        Return the response in text format.
        """
        self.history = []
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=self.system_prompts
        )

    def discuss(self, prompt):
        self.chat = self.model.start_chat(
            history=self.history
        )
        response = self.chat.send_message(prompt)
        # self.set_history("user", prompt)
        # self.set_history("model", response)
        return response.text
    
    def set_history(self, role, parts):
        self.history.append(
            {
                "role": role,
                "parts": [parts],
            }
        )