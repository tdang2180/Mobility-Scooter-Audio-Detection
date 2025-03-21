import convert_wav
import whisper_transcript

try: 
    convert_wav.convert_video_to_wav("../videos/sample.mp4", "../audios/sample.wav")
    whisper_transcript.get_transcript("../videos/sample.mp4", "../transcriptions/sample_transcript.vtt")
except Exception as e:
    print(f'error: {e}')