from abc import ABC, abstractmethod
from src.core.artifacts.typed import ServiceName, ServiceDescription


class IService(ABC):
    @property
    @abstractmethod
    def service_name(self) -> ServiceName:
        """unique name that identifies the service"""
        ...

    @abstractmethod
    def describe(self) -> ServiceDescription:
        """purpose or description  of this service"""
        ...
