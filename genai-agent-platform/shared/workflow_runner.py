from cue.graph import build_cue_graph
from sdlc.graph import build_sdlc_graph

class WorkflowRunner:
    def __init__(self):
        self.workflows = {
            "cue": build_cue_graph(),
            "sdlc": build_sdlc_graph(),
        }

    async def run(self, workflow_name, input_data):
        graph = self.workflows[workflow_name]
        return await graph.ainvoke({"input": input_data})
