from langgraph.graph import StateGraph, END
from social_media_agent.basemodel import OverallState, BaseNode

from social_media_agent.services.scraper_node import ScraperNode
from social_media_agent.services.validator_node import ValidatorNode
from social_media_agent.services.relevance_node import RelevanceNode
from social_media_agent.services.generator_node import GeneratorNode
from social_media_agent.services.reviewer_node import ReviewerNode
from social_media_agent.services.publisher_node import PublisherNode
import inspect


class GraphBuilder:
    def __init__(self):
        self.nodes = {
            "scrape": ScraperNode(),
            "validate": ValidatorNode(),
            "relevance": RelevanceNode(),
            "generate": GeneratorNode(),
            "review": ReviewerNode(),
            "publish": PublisherNode(),
        }

    def wrap_node(self, node: BaseNode):
        if inspect.iscoroutinefunction(node.run):
            async def fn(state: OverallState) -> OverallState:
                return await node.run(state)
        else:
            def fn(state: OverallState) -> OverallState:
                return node.run(state)
        return fn

    def build(self):
        builder = StateGraph(OverallState)

        for name, node in self.nodes.items():
            builder.add_node(name, self.wrap_node(node))

        # Setup edges
        builder.set_entry_point("scrape")
        builder.add_edge("scrape", "validate")
        builder.add_edge("validate", "relevance")
        builder.add_edge("relevance", "generate")
        builder.add_edge("generate", "review")

        # Human-in-the-loop branching
        def review_condition(state: OverallState) -> str:
            return {
                "accept": "publish",
                "edit": "publish",   
                "reject": END
            }.get(state["approved"], END)

        builder.add_conditional_edges("review", review_condition)
        builder.add_edge("publish", END)

        return builder.compile()
