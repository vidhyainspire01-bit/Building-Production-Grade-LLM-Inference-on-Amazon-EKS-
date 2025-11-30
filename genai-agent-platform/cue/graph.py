from langgraph.graph import StateGraph, START, END
from cue.agents.signal_unifier import SignalUnifierAgent
from cue.agents.analyzer import AnalyzerAgent
from cue.agents.validator import ValidatorAgent
from cue.agents.summarizer import SummarizerAgent
from shared.memory import cue_memory

def build_cue_graph():
    sg = StateGraph()

    unify = SignalUnifierAgent()
    analyze = AnalyzerAgent()
    validate = ValidatorAgent()
    summarize = SummarizerAgent()

    sg.add_node("unify", unify.run)
    sg.add_node("analyze", analyze.run)
    sg.add_node("validate", validate.run)
    sg.add_node("summarize", summarize.run)

    sg.set_entry_point("unify")
    sg.add_edge("unify", "analyze")
    sg.add_edge("analyze", "validate")
    sg.add_edge("validate", "summarize")
    sg.add_edge("summarize", END)

    return sg.compile(checkpointer=cue_memory)
