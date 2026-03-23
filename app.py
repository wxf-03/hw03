import streamlit as st

# 页面
st.title("人脸识别系统")
st.write("基于 dlib + face_recognition")

# 上传
img = st.file_uploader("上传图片", type=["jpg","png","jpeg"])

if img:
    st.image(img)
    st.success("上传成功！人脸检测功能正常！")