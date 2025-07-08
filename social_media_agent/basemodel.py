from abc import ABC, abstractmethod
from typing_extensions import TypedDict, Literal

class OverallState(TypedDict):
    """
    Overall state of the system.
    """
    url: str
    content: str
    is_valid: bool
    is_relevant: bool
    post: str
    approved: Literal["edit", "reject", "accept"]
    posted: bool


class BaseNode(ABC):
    """
    Base class for all nodes.
    """
    @abstractmethod
    def run(self, state: OverallState) -> OverallState:
        """
        Run the node.
        """
        pass