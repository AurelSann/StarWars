import streamlit as st
from PIL import Image
import requests
import io


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

    # uploaded_file.__dict__

    image = Image.open(uploaded_file)
    st.image(image, caption='Beautiful ! Now, let\'s classify it...', use_column_width=True)

    # image.__dict__

    # convert imge to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # with open("image.jpg", "wb") as f:
    #     f.write(img_byte_arr)

    #API Call
    url = 'http://localhost:8000/uploadfile'
    files = {'file': img_byte_arr}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        resp = response.json()
        resp
    else:
        "ça marche pas"





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
#if API returns
#if Hubble == Sa/Sb
#if Hubble == Sb/Sc

