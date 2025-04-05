from Planner import Planner
from ToolController import ToolController
from PromptsGenerate import PromptsGenerate
import google.generativeai as generativeai
from output_translate import markdown_json_to_python_list
import dotenv
import os
import time

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Agent:
    def __init__(self,tools: list | None=None,tool_order: str | None=None):
        self.planner = Planner()
        self.toolcontroller = ToolController(tools=tools,order=tool_order)
        self.promptsgenerator = PromptsGenerate()
        print("Agent is ready")

    def step_plan(self, prompt):
        self.prompt = prompt
        try:
            steps = self.planner.plan(self.prompt)
            print("Steps planning is done")
            self.step_list = []
            for step in steps:
                tool_decide = self.toolcontroller.decide(step)
                ifneed = tool_decide['ifneed']
                tools = tool_decide['tools']
                if (ifneed == True and tools == "tavily"):
                    tasks = f"{step}, topic: {self.prompt}"
                    query = self.promptsgenerator.tavily_tasks(tasks)
                    query = query['prompt']
                else:
                    query = ""
                self.step_list.append({"action":step,"ifneed tool":ifneed,"tools":tools,"prompt":query})
                time.sleep(1)
            print("Tool decision is done")
            return self.step_list
        except Exception as e:
            print(e)
            return "Error"
        

