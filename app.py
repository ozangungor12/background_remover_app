import streamlit as st
import numpy as np
from PIL import Image
from modules.bg_remover import BackgroundRemover

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

st.write("### Background Remover")
st.sidebar.write("## Upload")
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

@st.cache_resource
def get_detector():
    return BackgroundRemover()

model = get_detector()

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        image = Image.open(my_upload)
        image = np.array(image)
        col1.write("Original Image")
        col1.image(image)

        det = model.remove(image)
        col2.write("Processed Image")
        col2.image(det)
        st.sidebar.markdown("\n")