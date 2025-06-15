from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage
import sys
sys.path.append('libs/langgraph')
from tests.fake_chat import FakeChatModel

class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

llm = FakeChatModel(messages=[AIMessage(content="LangGraph is a framework for building stateful LLM applications.")])


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


graph = graph_builder.compile()

for event in graph.stream({"messages": [{"role": "user", "content": "What is LangGraph?"}]}):
    for value in event.values():
        print("Assistant:", value["messages"][-1].content)
