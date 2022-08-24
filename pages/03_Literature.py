import streamlit as st
#https://pypi.org/project/streamlit-image-comparison/
#from streamlit_image_comparison import image_comparison
from side_logo_func import add_logo


# set page config
st.set_page_config(page_title="Literature", layout="centered")

st.title("Literature")

add_logo("./images/Logo.png")


st.subheader('Data')

st.markdown('In this project, we are using HI data obtained through our observations \
	and those available in the Australia Telescope Compact Array (ATCA) archive.')

st.markdown('Optical images are obtained through publicly available surveys.')

st.subheader('Python Packages')

st.markdown('We are using the following Python packages:')
st.write("Colormaps: Viridis & Magma are from Matplotlib. Amber, Horizon, Gem, Toxic,\
					Ocean, Bubblegum, Rainforest, Sepia and Eclipse are from Cmasher.")

st.subheader('Publication')

st.markdown('Using sample of Ring Galaxies, we have published:')