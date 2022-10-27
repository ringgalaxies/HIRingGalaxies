import streamlit as st
#from PIL import Image
from side_logo_func import add_logo, add_logo_t

# set page config
st.set_page_config(page_title="Introduction: HI-RINGS", layout="centered")

st.title("Introduction")

image_logo = "https://raw.githubusercontent.com/ringgalaxies/ringgalaxies.github.io/main/images/RingLogoMini.png"

add_logo(image_logo)
add_logo_t()

st.subheader("Ring Galaxies")

st.markdown('**Ring galaxies** are a class of peculiar galaxies possessing distinct ring-like structures, \
    usually composed of young stars and gas. \
    In our project we study the distribution and kinematics of the HI gas for the largest sample of ring galaxies to-date.')

st.subheader("Web Application")

st.markdown('This Streamlit web application allows us and community to interactively explore\
    **The HI in Ring Galaxies Survey (HI-RINGS)** using: HI intensity data and images from several other surveys: DSS, WISE, 2MASS and GALEX.')

st.markdown('To start exploration, go to the page: **"Explore Sample of Ring Galaxies"**.')
#logo, name = st.sidebar.columns(2)
#with logo:
#    image = './images/Logo.png'
#    st.image(image, use_column_width=True)
#with name:
#    st.markdown("<h1 style='text-align: left; color: grey;'> \
#                Lords of Rings </h1>", unsafe_allow_html=True)



