from abc import ABC, abstractmethod

class BaseUploader(ABC):
    def __init__(self, video):
        self.video = video

    @abstractmethod
    def upload(self):
        pass
