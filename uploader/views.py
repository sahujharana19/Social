from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Video
from .services.youtube_uploader import YouTubeUploader
from .utils.validators import validate_video


@csrf_exempt   # ✅ THIS @ WAS MISSING
def upload_video(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=400)

    print(request.FILES)   # will NOT be empty now

    video_file = request.FILES.get('video')
    if not video_file:
        return JsonResponse({'error': 'Video file missing'}, status=400)

    validate_video(video_file)

    video = Video.objects.create(
        title=request.POST.get('title', ''),
        description=request.POST.get('description', ''),
        platform=request.POST.get('platform', 'youtube'),
        video_file=video_file
    )

    uploader = YouTubeUploader(video)
    uploader.upload()

    return JsonResponse({'status': 'success', 'video_id': video.id})
