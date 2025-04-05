import google.generativeai as generativeai
import dotenv
import os

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Writer:
    def __init__(self):
        self.query = "According the input information, generate a research result paper or report.Use zh-TW language."
        self.think_model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=self.query
        )
        self.write_model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=self.query
        )

    def prewrite(self, text):
        response = self.think_model.generate_content(text)
        return response.text
    
    def write(self, text):
        response = self.write_model.generate_content(text)
        return response.text

