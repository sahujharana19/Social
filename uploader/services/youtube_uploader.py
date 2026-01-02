from .base_uploader import BaseUploader

class YouTubeUploader(BaseUploader):
    def upload(self):
        print(f"Uploading {self.video.title} to YouTube (mock)")
        return True
