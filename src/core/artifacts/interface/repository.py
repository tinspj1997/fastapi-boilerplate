from abc import ABC, abstractmethod
from src.core.artifacts.typed import RepoName


class IReposiitory(ABC):
    @property
    @abstractmethod
    def repository_name(self) -> RepoName:
        """unique name that identifies the repository"""
        ...

  