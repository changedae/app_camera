import streamlit as st
import os

imgPath=os.path.join(os.path.dirname(__file__),'images')
if not os.path.exists(imgPath):
     os.mkdir(imgPath)

uploadedFile = st.file_uploader('이미지선택', type=['JPG,PNG'])

if uploadedFile is not None:
     with open(os.path.join(imgPath,uploadedFile.name),"wb") as f:
          f.write(uploadedFile.getbuffer())