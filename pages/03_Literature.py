import streamlit as st
#https://pypi.org/project/streamlit-image-comparison/
#from streamlit_image_comparison import image_comparison
from side_logo_func import add_logo, add_logo_t


# set page config
st.set_page_config(page_title="Literature", layout="centered")

st.title("Literature")

image_logo = "https://raw.githubusercontent.com/ringgalaxies/ringgalaxies.github.io/main/images/RingLogoMini.png"

add_logo(image_logo)
add_logo_t()

st.subheader('Data')

st.markdown('In this project, we are using HI data obtained through our observations \
	and those available in the Australia Telescope Compact Array (ATCA) archive.')

st.markdown('Images from DSS, WISE, 2MASS and GALEX survey are obtained through publicly available sources.')

st.subheader('Python Packages')

st.markdown('We are using the following Python packages: astropy, aplpy, matplotlib, cmasher and streamlit_image_comparison')

st.write("Colormaps: Viridis & Magma are from Matplotlib. Amber, Horizon, Gem, Toxic,\
					Ocean, Bubblegum, Rainforest, Sepia and Eclipse are from Cmasher.")

st.subheader('Publication')

st.markdown("""[**The HI in Ring Galaxies Survey (HI-RINGS) - Effects of the bar on the HI gas in ring galaxies**](https://arxiv.org/pdf/2304.00515.pdf)""")
