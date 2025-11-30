from langgraph.graph import StateGraph, START, END
from shared.memory import sdlc_memory
from sdlc.agents.requirement_analyzer import RequirementAnalyzer
from sdlc.agents.architecture_agent import ArchitectureAgent
from sdlc.agents.codegen_agent import CodeGenAgent
from sdlc.agents.reviewer_agent import ReviewerAgent

def build_sdlc_graph():
    sg = StateGraph()

    req = RequirementAnalyzer()
    arch = ArchitectureAgent()
    codegen = CodeGenAgent()
    review = ReviewerAgent()

    sg.add_node("requirements", req.run)
    sg.add_node("architecture", arch.run)
    sg.add_node("code", codegen.run)
    sg.add_node("review", review.run)

    sg.set_entry_point("requirements")
    sg.add_edge("requirements", "architecture")
    sg.add_edge("architecture", "code")
    sg.add_edge("code", "review")
    sg.add_edge("review", END)

    return sg.compile(checkpointer=sdlc_memory)
