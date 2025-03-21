import whisper
from datetime import timedelta


def format_vtt(segments, mode):
    vtt_output = "WEBVTT\n\n"

    if mode == "words":
        for segment in segments:
            for word in segment["words"]:
                start = timedelta(seconds=word["start"])
                end = timedelta(seconds=word["end"])
                # text = word["text"].strip()

                vtt_output += f"{start} --> {end}\n{word['word']}\n"

    elif mode == "segms":
        for i, segment in enumerate(segments):
            start = timedelta(seconds=segment["start"])
            end = timedelta(seconds=segment["end"])
            text = segment["text"].strip()

            vtt_output += f"{start} --> {end}\n{text}\n"

    return vtt_output

def get_transcript(audio_path, folder_destination):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, word_timestamps=True)
    vtt_content = format_vtt(result["segments"], "segms")

    with open(folder_destination, "w") as f:
        f.write(vtt_content)    
        
    print(result["text"])
