import streamlit as st
from PIL import Image


#Titre
st.title('**GalaxyFinder**')
st.markdown('Hi there ! Let me show you galaxies.')

#File uploader
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a galaxy image", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))
