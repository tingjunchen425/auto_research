import google.generativeai as generativeai
from output_translate import markdown_json_to_python_list
import dotenv
import os

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class ToolController:
    def __init__(self,tools: list | None=None,order: str | None=None):
        self.tools = tools
        self.order = order
        self.system_prompts = f"""
        Decide whether you need to use tools according to the user's needs, and the tools that can be used are as follows: {self.tools},
        If there are not any tools that can be used, the response should be "ifneed":false, "tools":""
        Please return in json format, json is a dict with two fields 1. ifneed"(bool): If you need to use tool 2. tools(str): The name of the tool to use
        {self.order}
        Make sure to return the response in json format : ```json
        ...
        ```
        """
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=self.system_prompts
        )

    def decide(self, prompt):
        self.chat = self.model.start_chat()
        response = self.chat.send_message(prompt)
        response = markdown_json_to_python_list(response.text)
        return response