# Auto Research Assistant (自動研究助手)

這是一個基於AI的自動化研究助手系統，能夠協助使用者自動規劃研究步驟、搜集資料、進行討論分析，並生成完整的研究報告。透過整合多種AI模型和搜尋工具，本系統可以顯著提高研究效率。

## 功能特點

- **自動化研究規劃**：根據研究主題自動生成研究步驟
- **智慧搜尋**：整合Tavily搜尋API，自動搜集相關資訊
- **記憶管理**：使用向量資料庫(ChromaDB)儲存和檢索相關資訊
- **AI分析與討論**：使用Gemini模型進行資料分析和討論
- **自動報告生成**：自動產出結構化的研究報告

## 系統架構

系統主要由以下幾個模組組成：

- **Agent**：核心代理類，協調各個組件工作
- **Planner**：負責規劃研究步驟
- **ToolController**：決定每個步驟需要使用的工具
- **Discusser**：處理研究過程中的討論和分析
- **Memory**：基於向量資料庫的記憶系統
- **Writer**：負責生成最終研究報告

## 系統需求(建議)
1. python 3.11
2. gemini api key
3. tavily api key
4. OPENAI_API_KEY

## 安裝指南

1. 克隆此儲存庫：
```bash
git clone https://github.com/tingjunchen425/auto_research.git
cd Auto_Research
```

2. 安裝所需依賴：
```bash
pip install -r requirements.txt
```

3. 設定API密鑰：
   - 複製.env.example為.env
        ```bash
        copy .env.example .env
        ```
    - 填入以下內容
        ```
        gemini_api = [您的Gemini API密鑰]
        tavily_api = [您的Tavily API密鑰]
        OPENAI_API_KEY = [您的OpenAI API密鑰]
        ```

## 使用方法

基本使用流程：

```python
from Agent import Agent
from Memory import Memory
from Discusser import Discusser

# 初始化記憶系統
memory = Memory("research_topic")

# 設定工具和順序
tools = ["tavily", "RAG", "gemini-2.0-flash-thinking-exp-01-21"]
order = """If user ask to find the parts in the article, use RAG to find the answer.
If user ask for professional issues, use search tools to find relevant knowledge.
If user ask for summary of the search result or article, use gemini-2.0-flash-thinking-exp-01-21.
"""

# 初始化代理
agent = Agent(tools=tools, tool_order=order)

# 開始研究流程
steps = agent.step_plan("您的研究主題")

# 執行研究步驟並生成報告
# (參考flow.py了解完整流程)
```

## 範例

系統可以自動研究各種主題，例如：
- 人類用火歷史研究
- AI對經濟的影響研究
- 以及各種需要資料收集和分析的研究主題

## 依賴項目

- Python 3.x
- Google Generative AI (Gemini)
- ChromaDB
- Sentence Transformers
- Tavily API

## 注意事項

- 請確保您的API密鑰有足夠的使用額度
- 向量資料庫在大型研究專案中可能需要較多記憶體
- 建議在研究複雜主題時適當調整步驟數量和搜尋範圍

## 授權

本專案採用MIT授權 - 詳見 [LICENSE](LICENSE) 文件

Copyright (c) 2025 tingjunchen425