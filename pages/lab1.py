import streamlit as st
# import cv2

st.title("lab1")

file = st.file_uploader("upload_file")

if file is None:
    file = st.camera_input("take picture")
    # bin 파일을 jpg로 변경하는 코드 

if file is not None:
  st.download_button(" 사진을 다운로드 ", file)
