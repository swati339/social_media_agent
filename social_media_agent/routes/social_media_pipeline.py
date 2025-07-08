
# from fastapi import FastAPI, APIRouter
# from social_media_agent.graph_builder import GraphBuilder
# from social_media_agent.basemodel import OverallState

# router = APIRouter()
# @router.post("/process")
# async def process(state: OverallState):
#     graph = GraphBuilder().build()
#     final_state = graph.invoke(state)
#     return final_state



from fastapi import APIRouter
from social_media_agent.graph_builder import GraphBuilder
from social_media_agent.basemodel import OverallState

router = APIRouter()

@router.post("/process")
async def process(state: OverallState):
    graph = GraphBuilder().build()
    final_state = await graph.ainvoke(state)  
    return final_state
