import streamlit as st
from video_grab import search_yt
from strip_audio import download_save_audio
from llm_results import *
import pandas as pd
import os
import time


if "search_keyword" and "analysis_submitted" not in st.session_state:
    st.session_state["aai_api_key"] = '08d0a4c4a98341adbe2f3c0eb224dc69'
    st.session_state["search_keyword"] = ""
    st.session_state["analysis_submitted"] = False
    st.session_state["video_list"] = None

def save_keyword(keyword):
    st.session_state["search_keyword"] = keyword
    print("search keyword saved")

def update_analysis_state(video_list):
    st.session_state["analysis_submitted"] = True
    st.session_state["video_list"] = video_list

st.title("Get product review from YouTube")
st.subheader("🕒 Save 100x time, get 100% of the value for free ⭐")

markdown1 = '<p style="font-family:Georgia; color:White; font-size: 20px;">Do not want to waste time on YouTube videos to get info? Or, do you get overwhelmed with infinite pool of review videos on YouTube?</p>'
markdown2 = '<p style="font-family:Georgia; color:White; font-size: 20px;">Overwhelmed with infinite pool of review videos on YouTube?</p>'
markdown3 = '<p style="font-family:Georgia; color:White; font-size: 20px;">Find hard sorting through unnecessary info in YouTube videos?</p>'
markdown4 = '<p style="font-family:Georgia; color:White; font-size: 20px;">Worry not!</p>'
markdown5 = '<p style="font-family:Georgia; color:White; font-size: 20px;">We will review your chosen videos to summarize Pros and Cons of the product.</p>'

st.markdown(markdown1, unsafe_allow_html=True)
#st.markdown(markdown2, unsafe_allow_html=True)
#st.markdown(markdown3, unsafe_allow_html=True)
st.markdown(markdown4, unsafe_allow_html=True)
st.markdown(markdown5, unsafe_allow_html=True)

keys, input = st.columns(2)

st.subheader("Which product would you want to know more about?")
product = st.text_input(
    "Type in the name and model of the product you'd like to analyse the reviews of.", value=st.session_state["search_keyword"][:-7]
)
search_phrase = product + " review"
st.button("Search!", on_click=save_keyword, args=(search_phrase,))

if st.session_state["aai_api_key"] == "" and st.session_state["search_keyword"] != "":
    st.error("Please fill in your AssemblyAI API Key.", icon="🚨")

if st.session_state["aai_api_key"] != "" and st.session_state["search_keyword"] != "":
    video_list = None

    if not st.session_state["analysis_submitted"]:
        yt_api_key = 'AIzaSyACuaHf26JpcFFOxXw-wDUbPPoWncmRd6w'
        video_list = search_yt(yt_api_key, st.session_state["search_keyword"])  
    else:
        video_list = st.session_state["video_list"]

    if video_list is None:
        st.error("Make sure your YouTube Data API Key is correct.", icon="🚨")
    else:
        with st.form("video"):
            col1, col2, col3, col4 = st.columns(4)
            col5, col6, col7, col8 = st.columns(4)

            vid1 = col1.checkbox("👇 select video", key="vid1")
            col1.image(video_list[0]["video_thumbnail"])
            col1.write(video_list[0]["video_title"])

            vid2 = col2.checkbox("👇 select video", key="vid2")
            col2.image(video_list[1]["video_thumbnail"])
            col2.write(video_list[1]["video_title"])

            vid3 = col3.checkbox("👇 select video", key="vid3")
            col3.image(video_list[2]["video_thumbnail"])
            col3.write(video_list[2]["video_title"])

            vid4 = col4.checkbox("👇 select video", key="vid4")
            col4.image(video_list[3]["video_thumbnail"])
            col4.write(video_list[3]["video_title"])

            vid5 = col5.checkbox("👇 select video", key="vid5")
            col5.image(video_list[4]["video_thumbnail"])
            col5.write(video_list[4]["video_title"])

            vid6 = col6.checkbox("👇 select video", key="vid6")
            col6.image(video_list[5]["video_thumbnail"])
            col6.write(video_list[5]["video_title"])

            vid7 = col7.checkbox("👇 select video", key="vid7")
            col7.image(video_list[6]["video_thumbnail"])
            col7.write(video_list[6]["video_title"])

            vid8 = col8.checkbox("👇 select video", key="vid8")
            col8.image(video_list[7]["video_thumbnail"])
            col8.write(video_list[7]["video_title"])

            submitted = st.form_submit_button("Submit", on_click=update_analysis_state, args=(video_list,))

        if st.session_state["analysis_submitted"]:
            bool_list = [vid1, vid2, vid3, vid4, vid5, vid6, vid7, vid8]
            video_df = pd.DataFrame(video_list)
            selected_videos = video_df[bool_list]
            urls = selected_videos["video_link"].tolist()

            audio_files = []
            for url in urls:
                filename = download_save_audio(url)
                audio_files.append(filename)

            # Placeholder for a flashing message
            message_placeholder = st.empty()

            # Wait until all audio files are downloaded
            def check_audio_files_downloaded(files):
                return all(os.path.exists(file) for file in files)

            # Flashing message while waiting for downloads
            while not check_audio_files_downloaded(audio_files):
                for msg in ["⏳ Preparing audio files...", "⏳ Preparing audio files, please wait..."]:
                    message_placeholder.markdown(f"<h3 style='color:orange;'>{msg}</h3>", unsafe_allow_html=True)
                    time.sleep(1)

            # Flashing message while analysis is working
            message_placeholder.markdown("<h3 style='color:orange;'>🔍 Analyzing the audio, please wait...</h3>", unsafe_allow_html=True)

            # Once all audio files are ready, proceed with the analysis
            id_list = [transcribe(st.session_state["aai_api_key"], file) for file in audio_files]
            pros, cons = group_analyse(id_list)

            # Clear the placeholder after analysis is complete
            message_placeholder.empty()

            # Show results of llm analysis
            pros_col, cons_col = st.columns(2)
            pros_col.subheader("✅ Pros")
            pros_col.markdown(pros)

            cons_col.subheader("❌ Cons")
            cons_col.markdown(cons)
