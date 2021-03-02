import streamlit as st
from PIL import Image


##Design, couleurs


#Titre
st.title('**GalaxyFinder**')
st.markdown("Hi there ! Let me show you galaxies. It's very simple.")

#Explanation
st.markdown("You just have to upload a galaxy picture on the File uploader below:")


#File uploader
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a galaxy image", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Beautiful ! Now, let\'s classify it...', use_column_width=True)


#API Call


#Wait time
if st.checkbox('Show progress bar'):
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'


##Output pour chaque classe

