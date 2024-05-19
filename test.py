from youtube_transcript_api import YouTubeTranscriptApi
from gradientai import Gradient, SummarizeParamsLength
from dotenv import load_dotenv

load_dotenv()

gradient = Gradient()

video_id = "YHxj3LvZoLQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
full_text = [
    i["text"].replace("\n", " ") if "\n" in i["text"] else i["text"] for i in transcript
]
Clean_text = "".join(full_text)

length = SummarizeParamsLength.MEDIUM
result_from_length = gradient.summarize(document=Clean_text, length=length)
print("Summary = ", result_from_length["summary"])
