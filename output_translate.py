import re
import json

def markdown_json_to_python_list(markdown_text):
    """
    從 Markdown 文本中提取 JSON list (```json[...]```) 並轉換為 Python list。

    Args:
        markdown_text: 包含 Markdown 格式 JSON list 的字串。

    Returns:
        如果找到並成功解析 JSON list，則返回 Python list。
        如果未找到 JSON list 或解析失敗，則返回 None。
    """
    json_list_str = None  # 初始化為 None，以處理未找到的情況

    # 正規表示式來尋找 ```json ... ``` 區塊並提取內容
    pattern = r"```json\s*([\s\S]*?)\s*```"  # 匹配 ```json 和 ``` 之間的任何內容 (包含換行)
    match = re.search(pattern, markdown_text)

    if match:
        json_list_str = match.group(1).strip()  # 提取匹配到的群組 (JSON 字串) 並去除前後空白

    if json_list_str:
        try:
            python_list = json.loads(json_list_str)  # 使用 json.loads 解析 JSON 字串為 Python list
            return python_list
        except json.JSONDecodeError:
            print("JSON 解析錯誤：Markdown 程式碼區塊中的內容不是有效的 JSON list。")
            return None  # JSON 解析失敗
    else:
        print("未在 Markdown 文本中找到 ```json ... ``` 格式的 JSON list。")
        return None  # 未找到 JSON list