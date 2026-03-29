import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="AI Background Remover", page_icon="🖼️")
st.title("🖼️ AI बॅकग्राउंड रिमूव्हर")
st.write("तुमचा फोटो अपलोड करा आणि जादू पहा!")

uploaded_file = st.file_uploader("फोटो निवडा (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='तुमचा मूळ फोटो', use_container_width=True)
    
    with st.spinner("बॅकग्राउंड काढत आहे... कृपया थांबा..."):
        input_bytes = uploaded_file.read()
        output_bytes = remove(input_bytes)
        output_image = Image.open(io.BytesIO(output_bytes))
    
    st.image(output_image, caption='बॅकग्राउंड काढलेला फोटो', use_container_width=True)
    
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="फ्रीमध्ये फोटो डाउनलोड करा",
        data=byte_im,
        file_name="bg_removed.png",
        mime="image/png"
    )
    st.success("तुमचे काम झाले आहे!")
