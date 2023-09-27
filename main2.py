import streamlit as st

# Streamlitアプリのタイトルを設定
st.title("YouTube動画表示アプリ")

# YouTube動画のURLを入力
youtube_url = st.text_input("YouTube動画のURLを入力してください:")

# YouTube動画のURLが入力された場合、埋め込みコードを表示
if youtube_url:
    st.write("YouTube動画を表示します:")
    st.video(youtube_url)
