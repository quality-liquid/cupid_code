from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import Dict, Any, Callable

# Handle both module execution and direct script execution
try:
    from .utils.prompts import ALL_TV_SHOWS_PROMPT, NERD_FILTERING_PROMPT
    from .tools import (
        talkingAboutLordOfTheRings,
        you_are_a_nerd,
        changeTheTopicAboutHer,
        talkingAboutStarWars,
        talkingAboutTheHobbit,
        talkingAboutStarTrek,
        talkingAboutThisTVShow
    )
except ImportError:
    from utils.prompts import ALL_TV_SHOWS_PROMPT, NERD_FILTERING_PROMPT
    from tools import (
        talkingAboutLordOfTheRings,
        you_are_a_nerd,
        changeTheTopicAboutHer,
        talkingAboutStarWars,
        talkingAboutTheHobbit,
        talkingAboutStarTrek,
        talkingAboutThisTVShow
    )


def _create_graph_agent(prompt, tool_router: Callable[[str, str], list[str]]):
    """
    Generic agent builder for LangGraph classification pipelines.
    
    Args:
        prompt: ChatPromptTemplate for classification
        tool_router: Function that takes (text, classification_label) and returns list of result strings
        
    Returns:
        Compiled LangGraph application
    """
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    detect_chain = prompt | llm
    
    graph = StateGraph(dict)
    
    def classify(state: Dict[str, Any]) -> Dict[str, Any]:
        text = state.get("input_text", "")
        resp = detect_chain.invoke({"input_text": text})
        label = getattr(resp, "content", str(resp)).strip().lower()
        return {**state, "classification": label}
    
    def call_tools(state: Dict[str, Any]) -> Dict[str, Any]:
        text = state.get("input_text", "")
        label = state.get("classification", "none")
        
        # Use the provided tool router to determine which tools to call
        parts = tool_router(text, label)
        
        result = "\n".join(p for p in parts if p)
        return {**state, "result": result or "No relevant tools to call."}
    
    def route_after_classify(state: Dict[str, Any]) -> str:
        label = state.get("classification", "none")
        return "call_tools" if label and label not in {"none", ""} else END
    
    graph.add_node("classify", classify)
    graph.add_node("call_tools", call_tools)
    
    graph.add_edge(START, "classify")
    graph.add_conditional_edges("classify", route_after_classify)
    graph.add_edge("call_tools", END)
    
    return graph.compile()


def create_agent():
    """Build a nerd-filtering agent for sci-fi/fantasy franchises."""
    
    def nerd_tool_router(text: str, label: str) -> list[str]:
        """Route to appropriate nerd/franchise tools based on classification."""
        parts = []
        
        if label == "star_wars":
            parts.append(talkingAboutStarWars(text))
            parts.append(you_are_a_nerd(text))
        elif label == "hobbit":
            parts.append(talkingAboutTheHobbit(text))
        elif label == "star_trek":
            parts.append(talkingAboutStarTrek(text))
        elif label == "lotr":
            parts.append(talkingAboutLordOfTheRings(text))
        
        # Always optionally add a topic change suggestion
        if label in {"star_wars", "hobbit", "star_trek", "lotr"}:
            parts.append(changeTheTopicAboutHer(text))
        
        return parts
    
    return _create_graph_agent(NERD_FILTERING_PROMPT, nerd_tool_router)


def create_TV_agent():
    """Build a TV show detection agent."""
    
    def tv_tool_router(text: str, label: str) -> list[str]:
        """Route to TV show tools based on classification."""
        parts = []
        
        if label and label != "none":
            parts.append(talkingAboutThisTVShow(text, show_name=label))
        
        return parts
    
    return _create_graph_agent(ALL_TV_SHOWS_PROMPT, tv_tool_router)
