from tavily import TavilyClient
import dotenv
import os

tavily_api = os.getenv('tavily_api')
client = TavilyClient(tavily_api)

class tavily_client:
    def __init__(self):
        pass

    def search(self, query):
        response = client.search(query)
        resp = response['results']
        result = []
        for res in resp:
            result.append(res['content'])
        return result