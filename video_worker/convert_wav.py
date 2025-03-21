import subprocess

def convert_video_to_wav(input_video, output_wav):
    # video_path = f"../{input_video}"
    print(input_video)
    command = [
        "ffmpeg",
        "-i", input_video,  # Input video file
        "-vn",  # Disable video (extract audio only)
        "-acodec", "pcm_s16le",  # WAV audio codec
        "-ar", "44100",  # Sample rate
        "-ac", "2",  # Number of audio channels
        output_wav  # Output WAV file
    ]
    subprocess.run(command, check=True)