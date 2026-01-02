def validate_video(file):
    if not file.name.endswith('.mp4'):
        raise ValueError('Only mp4 allowed')
