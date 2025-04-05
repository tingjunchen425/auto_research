import google.generativeai as generativeai
from output_translate import markdown_json_to_python_list
import dotenv
import os

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Planner:
    def __init__(self):
        self.system_prompts = f"""
        use zh-TW
        Design the process plan according to the user's needs
        The response should be explicit,for example: If the step is to search for information, the response should clearly describe the keywords or topic
        generate the response in JSON format, and output the format ["step1", "step2",...]
        the output should be only a JSON list not markdown, and there should not be any dict in the list
        Make sure to return the response in json format : ```json
        [
            "step1",
            "step2"
        ]
        ```
        """
        self.history = []
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=self.system_prompts
        )

    def plan(self, prompt):
        self.chat = self.model.start_chat(
            history=self.history
        )
        response = self.chat.send_message(prompt)
        response = markdown_json_to_python_list(response.text)
        # self.set_history("user", prompt)
        # self.set_history("model", response)
        return response
    
    def set_history(self, role, parts):
        self.history.append(
            {
                "role": role,
                "parts": [parts],
            }
        )