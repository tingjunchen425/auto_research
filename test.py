from Planner import Planner
from ToolController import ToolController
from Discusser import Discusser
import json
from output_translate import markdown_json_to_python_list
from PromptsGenerate import PromptsGenerate
from Agent import Agent
from Memory import Memory
from Discusser import Discusser

memory = Memory("discuss")
discusser = Discusser("The impact of AI on the future of work")

order = """If user ask to find the parts in the article, use RAG to find the answer.
If user ask for professional issues such as computer science, physics, math, biology, etc.,use search tools to find relevant knowledge.
If user ask for sumaary of the search result or article, use gemini-2.0-flash-thinking-exp-01-21 to generate the summary.
If user ask for generate a research result paper or report, use Claude 3.5 Sonnet to generate the paper.
            """
tools=["tavily", "RAG","Claude 3.5 Sonnet","gemini-2.0-flash-thinking-exp-01-21"]
agent = Agent(tools=tools,tool_order=order)

prompt = "Make a research about the topic 'The impact of AI on the future of work'"
resp = agent.step_plan(prompt)
memory.add_memory(prompt, "prompt")
memory.add_memory(order, "order")
memory.add_memory("The impact of AI on the future of work", "topic")
memory.add_memory(f"{resp}", "steps of research")
with open("step.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(resp,ensure_ascii=False,indent=4))
print('-'*50)
print(memory.query_memory("topic"))
print('-'*50)
print(memory.query_memory("prompt"))
print('-'*50)
print(memory.query_memory("ifneed tool"))
