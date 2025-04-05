from Agent import Agent
from Memory import Memory
from Discusser import Discusser
from Discusser import Discusser
import json
from Tavily_client import tavily_client
from writer import Writer

memory = Memory("flow")
discusser = Discusser(" Was a Time in the Past When People Didn’t Use Fire. What Do You Think Life Was Like Then?")
order = """If user ask to find the parts in the article, use RAG to find the answer.
If user ask for professional issues such as computer science, physics, math, biology, etc.,use search tools to find relevant knowledge.
If user ask for sumaary of the search result or article, use gemini-2.0-flash-thinking-exp-01-21 to generate the summary.
If user ask for generate a research result paper or report, use Claude 3.5 Sonnet to generate the paper.
            """
tools=["tavily", "RAG","Claude 3.5 Sonnet","gemini-2.0-flash-thinking-exp-01-21"]
agent = Agent(tools=tools,tool_order=order)
tavily = tavily_client()
writer = Writer()

steps = agent.step_plan("Make a research about the topic ' Was a Time in the Past When People Didn’t Use Fire. What Do You Think Life Was Like Then?'")
memory.add_memory(" Was a Time in the Past When People Didn’t Use Fire. What Do You Think Life Was Like Then?", "topic")
memory.add_memory(f"{steps}", "steps of research")
with open("step.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(steps,ensure_ascii=False,indent=4))
i = 0
d = 0
discuss_result = []
search_result = {}
with open("discuss.md", "w",encoding="utf-8") as f:
        f.write("")
for step in steps:
    if step["ifneed tool"] == True:
        print(step["action"])
        print(step["tools"])
        if step["tools"] == "tavily":
            resp = tavily.search(step["prompt"])
            memory.add_memory(resp, f"tavily search result {i}")
            search_result[f"tavily search result {i}"] = resp
            print(resp)
            i += 1
        elif step["tools"] == "RAG":
            pass
        elif step["tools"] == "Claude 3.5 Sonnet" or step["tools"] == "gemini-2.0-flash-thinking-exp-01-21":
            print("No need to search")
            discuss = discusser.discuss(f"{step['action']}\n{search_result}\n{discuss_result}")
            print(discuss)
            memory.add_memory(discuss, f"discussin {d}")
            d += 1
            discuss_result.append(discuss)
        print('-'*50)
result = writer.prewrite(f"{discuss_result}")
print(result)
with open("result.md", "w",encoding="utf-8") as f:
    f.write(result)
with open("discuss.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(discuss_result,ensure_ascii=False,indent=4))
with open("search.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(search_result,ensure_ascii=False,indent=4))


