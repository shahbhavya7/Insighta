import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1] # Extracting video ID from the URL by splitting the URL from '='and taking the second part
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id) # Getting the transcript text using the video ID

        transcript = "" # Initializing an empty string to store the transcript text
        for i in transcript_text: # Looping through each item in the transcript text
            transcript += " " + i["text"] # Concatenating the text from each item to the transcript string as it is in dictionary format from the API

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content(prompt+transcript_text) # Generating content using the model with the prompt and transcript text
    return response.text # response.text contains the generated summary text

st.title("Insighta 🎥 - Yt Video to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link: # Check if the YouTube link is provided
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.video(youtube_link) # Display the YouTube video in the Streamlit app


if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)




