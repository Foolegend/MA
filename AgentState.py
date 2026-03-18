from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

model = ChatOpenAI(
    model="gpt-5",
    temperature=0.1,
    max_tokens=1000,
    timeout=30
    # ...（其他参数）
)



@tool
def search(query: str) -> str:
    """搜索信息。"""
    return f"结果：{query}"

@tool
def get_weather(location: str) -> str:
    """获取位置的天气信息。"""
    return f"{location} 的天气：晴朗，72°F"

agent = create_agent(model, tools=[search, get_weather])