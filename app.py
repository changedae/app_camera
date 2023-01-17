import streamlit as st
import os.path

imgPath=os.path.join(os.path.dirname(__file__),'images')
if not os.path.exists(imgPath):
     os.mkdir(imgPath)


st.subheader('학생사진촬영')

col1, col2 = st.columns(2)

hakbun=col1.text_input('학번')
name=col2.text_input('성명')

pic = st.camera_input('사진')

if pic is not None:
    fname, ext = os.path.splitext(pic.name)
    img_name = hakbun + name + ext

    with open(os.path.join(imgPath,img_name ), "wb") as f:
        f.write(pic.getbuffer())

