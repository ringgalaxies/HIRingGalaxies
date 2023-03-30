import streamlit as st
import requests
from astropy.io import fits
from astropy import units as u
import aplpy

import matplotlib.pyplot as plt
import matplotlib.font_manager

#import numpy as np
#import seaborn as sns
from pathlib import Path
from side_logo_func import add_logo, add_logo_t
import cmasher as cmr
#import sys

import io
from io import BytesIO

from streamlit_image_comparison import image_comparison
from PIL import Image

import urllib.request as urllib2

# Set to "True" if you want to use this app locally 
local_use = "False" 

# set page config
st.set_page_config(page_title="HI-RINGS", layout="centered")
st.title("The HI in Ring Galaxies Survey")

if local_use == "False":
    image_logo = "https://raw.githubusercontent.com/ringgalaxies/ringgalaxies.github.io/main/images/RingLogoMini.png"

    add_logo(image_logo)
    add_logo_t()
else:
    add_logo("./images/Logo.png")

# Plotting parameters
matplotlib.rcParams.update(
    {#'text.usetex': True, - not using latex as it slows down plotting
    'font.size': 20, 'xtick.major.size': 10, 'ytick.major.size': 10, 
    'ytick.minor.size': 5, 'xtick.minor.size': 5, 'xtick.direction': 'in', 
    'ytick.direction': 'in', 'xtick.minor.size': 5, 'ytick.minor.size': 5,
    'xtick.major.size': 12, 'ytick.major.size': 12, 'xtick.top': True, 'ytick.right': True })


# Our sample of Ring galaxies
galaxies = ['ESO269-57','ESO215-31','NGC1326','NGC3358','IC5267','NGC1302','NGC1398','NGC2217',
        'NGC7020','NGC1291','NGC1371','ESO179-IG013','NGC2369','NGC1350','NGC7098','NGC1543',
        'NGC1433','NGC1079','NGC1808','NGC5101','NGC7531','NGC6300','IC5240', 'NGC1533']

# Distances that we are using for the Ring galaxy sample
distances = [43.24, 35.20, 14.95, 38.30, 21.26, 11.21, 19.79, 21.87, 29.40, 4.40, 23.79, 10.90, 
             35.30, 18.83, 29.10, 17.19, 9.47, 25.20, 9.29, 17.23, 22.22, 12.26, 25.37, 20.20]

# List of available surveys
used_surveys = ['DSS', 'DSS2 Blue', 'DSS2 Red', 'DSS2 IR','WISE 3.4', 'WISE 4.6', 
        'WISE 12', 'WISE 22', 'GALEX Far UV', 'GALEX Near UV', '2MASS-J', '2MASS-H', '2MASS-K']

# Survey images are obtained through astropy vizier, thus have numbers in their names
# 2, 3 were generaly missing so they are excluded
used_survey_numbers = ['1', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']


# Select ring galaxy - Streamlig
optionImage = st.selectbox('Select Ring Galaxy', (galaxies))

for i, galaxy in enumerate(galaxies):
    if galaxy == f'{optionImage}':
        distance = distances[i]

# Show name of the Selected Ring galaxy
st.markdown(f"# {optionImage}")

# Show 3 links to the databases
database_one, database_two, database_three = st.columns(3)
with database_one:
    st.write(f"NED: [{optionImage}](https://ned.ipac.caltech.edu/byname?objname={optionImage}&hconst=67.8&omegam=0.308&omegav=0.692&wmap=4&corr_z=1)")
with database_two:
    st.write(f"Simbad: [{optionImage}](https://simbad.u-strasbg.fr/simbad/sim-id?Ident={optionImage}&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id)")
with database_three:
    st.write(f"HyperLeda: [{optionImage}](http://leda.univ-lyon1.fr/ledacat.cgi?o={optionImage})")


# Moment 0 fits file
#fits_image =f'./data/{optionImage}_2_mom0.fits'

# HI file
if local_use == "False":
    fits_NHI = f'https://github.com/ringgalaxies/HIRingGalaxies/blob/main/data/{optionImage}/{optionImage}_NHI.fits?raw=true'
else:
    fits_NHI = f'./data/{optionImage}/{optionImage}_NHI.fits'

def get_survey_image(optionImage, survey_number):
    """
    optionImage - string, galaxy name
    survey_number - each number from 1 to 15 represents particular survey data
    """
    if local_use == "False":
        # Need to check if file exist
        path_to_check = f'https://github.com/ringgalaxies/HIRingGalaxies/blob/main/data/{optionImage}/{optionImage}_{survey_number}.fits?raw=true'

        r = requests.get(path_to_check, stream=True)
        if r.status_code == 200:

            survey_image = f'https://github.com/ringgalaxies/HIRingGalaxies/blob/main/data/{optionImage}/{optionImage}_{survey_number}.fits?raw=true'
        else:
            st.warning("Sorry, selected survey file doesn't exist, please try different survey.")
            st.stop()   
    else:
        # Need to check if file exist
        path_to_check = f'./data/{optionImage}/{optionImage}_{survey_number}.fits'
        path = Path(path_to_check)

        if path.is_file():
            survey_image = f'./data/{optionImage}/{optionImage}_{survey_number}.fits'
        else:
            st.warning("Sorry, the particular file is missing, please try different.")
            st.stop()

    return survey_image


# Sort colormap dictionary - so that we get nice names in the selectbox
cmap_dict = {'cmr.neutral': 'Neutral',
             'cmr.amber': 'Amber',
             'cmr.horizon': 'Horizon',
             'cmr.gem': 'Gem',
             'cmr.toxic': 'Toxic',
             'cmr.ocean': 'Ocean',
             'cmr.bubblegum': 'Bubblegum',
             'cmr.rainforest': 'Rainforest',
             'cmr.sepia': 'Sepia',
             'cmr.eclipse': 'Eclipse',
             'viridis': 'Viridis',
             'magma': 'Plasma'}

def format_func(option):
    """ Will be use to extract cmap from dictionary"""
    return cmap_dict[option]


with st.sidebar:
    st.info('### Background image options')
    survey_number = st.selectbox("Background Image From Survey", (used_surveys))
    
    # Connect survey to survey number in order to show selected one
    for i, surv in enumerate(used_surveys):
        if survey_number == surv:
            survey_image = get_survey_image(optionImage, used_survey_numbers[i])

# Image radius options
with st.sidebar:
    select_radius = st.radio("Image Radius [arcmin]", ("9", "6", "3"), horizontal=True)
    if select_radius=="9":
        radius = 0.15
    if select_radius=="6":
        radius = 0.1
    if select_radius=="3":
        radius = 0.05

# Open selected suvey image with aplpy
backgr_im = fits.open(survey_image)
img = aplpy.FITSFigure(backgr_im)

# Options how to display selected survey image
with st.sidebar:
    im_type = st.radio("Background Image Display Option", 
        ("Grayscale", "Custom"))

    
    if im_type == "Grayscale":
        img.show_grayscale(vmin=None, vmid=None, vmax=None)

    if im_type == "Custom":
        with st.sidebar:
            cmap_or_reverse = st.radio("Image Colormap Direction", 
                                ("Regular", "Reversed"), horizontal=True)

        one_prop, two_prop = st.columns([1.5,1])

        # Show colormaps - parse whether they are regular or reversed
        with one_prop:
            if cmap_or_reverse=="Regular":
                cmap = st.selectbox('Select Colormap', cmap_dict.keys(), 
                                    format_func=lambda x:cmap_dict[x])
            if cmap_or_reverse=="Reversed":
                cmap = st.selectbox('Select Colormap', cmap_dict.keys(), 
                                    format_func=lambda x:cmap_dict[x])+'_r'

        # Show selected options for image stretch
        with two_prop:
            stretch = st.selectbox("Select Stretch", ('linear', 'log', 'sqrt', 'arcsinh', 'power'))

        # Show image in selected colormap and stretch
        img.show_colorscale(stretch=stretch, vmin=None, vmid=None, vmax=None, cmap=cmap)
 

def get_hi_densities():
    """
    Checkboxes for the particular HI densities.
    There are two rows with 3, 2 columns - just to display them nicely on the sidebar.
    """
    # Possible HI column density options
    select_hi = ['0.5e+20', '1e+20', '3e+20', '5e+20','7e+20']
    # Only selected ones will be appended below and parsed to be displayed
    selected_hi = [] 

    one_hi, two_hi, three_hi = st.sidebar.columns(3)
    with one_hi:
        ch1 = st.checkbox(select_hi[0])
        if ch1:
            selected_hi.append(0.5e+20)
    with two_hi:
        # Setting one contour as true to avoid UserWarning that there are no contours
        ch2 = st.checkbox(select_hi[1], value=True) 
        if ch2:
            selected_hi.append(1e+20)
    with three_hi:
        ch3 = st.checkbox(select_hi[2])
        if ch3:
            selected_hi.append(3e+20)

    four_hi, five_hi, six_hi = st.sidebar.columns(3)

    with four_hi:
        ch4 = st.checkbox(select_hi[3])
        if ch4:
            selected_hi.append(5e+20)
    with five_hi:
        ch5 = st.checkbox(select_hi[4])
        if ch5:
            selected_hi.append(7e+20)

    return selected_hi

with st.sidebar:
    st.write("")
    st.info('### HI contour options')
    st.write(r"HI Column Density [cm$^{−2}$]")

# Checkboxes
selected_hi_densities = get_hi_densities()


# Options to select particular colormap for HI contours
with st.sidebar:
    cmap_or_reverse = st.radio("Contour Colormap Direction", ("Regular","Reversed"),
                                 horizontal=True)
    if cmap_or_reverse=="Regular":
        cmap_hi = st.selectbox('Select Contour Colormap', cmap_dict.keys(), 
                            format_func=lambda x:cmap_dict[x])
        # Get sub colormap and not the full range
        cmap_hi = cmr.get_sub_cmap(cmap_hi, 0.35, 0.8)

    if cmap_or_reverse=="Reversed":
        cmap_hi = st.selectbox('Select Contour Colormap', cmap_dict.keys(), 
                            format_func=lambda x:cmap_dict[x])+'_r'
        cmap_hi = cmr.get_sub_cmap(cmap_hi, 0.1, 0.8)


# Read fits file, data and header
def get_hi_fits_properties(fits_NHI):
    hdul = fits.open(fits_NHI)
    hdr = hdul[0].header

    # Get synthesised beam size parameters
    bmaj = hdr['BMAJ'] # in deg
    bmin = hdr['BMIN'] # in deg
    pa = hdr['BPA'] # in deg


    # Scalebar calculation 10kpc
    scalebar_size = (10.*206265.)/(distance*1e3)
    ra = hdr['CRVAL1']
    dec = hdr['CRVAL2']
    hdul.close()

    return bmaj, bmin, pa, scalebar_size, ra, dec

bmaj, bmin, pa, scalebar_size, ra, dec = get_hi_fits_properties(fits_NHI)

#img.set_system_latex(True)
img.recenter(x=ra, y=dec, radius=radius)

img.frame.set_linewidth(2)
img.frame.set_color('gray')

# Add scalebar to the Figure
img.add_scalebar(scalebar_size * u.arcsec, color='white', 
                corner='bottom right', label='10 kpc')
img.scalebar.set_linewidth(3)
img.scalebar.set_font_size(20)

# Use BitesIO to temp save image so that we can parse it to the image_comparison tool
# This one will be without HI colum density contours
buf = BytesIO()
img.savefig(buf)


# Plot the HI contours using NHI fits file
hdul = fits.open(fits_NHI)
#img = aplpy.FITSFigure(hdul)
img.show_contour(hdul, levels=selected_hi_densities, cmap=cmap_hi)
#img.show_grayscale(vmin=None, vmid=None, vmax=None)

# Add beam 
img.add_beam(major=bmaj, minor=bmin, angle=pa, frame=True, facecolor='black')
#img.ticks.set_color('white')

# Ignore warning of not parsing fig into st.pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

# Second image to be parsed to the image_comparison tool
# This one is with HI column density contours
buf2 = BytesIO()
img.savefig(buf2)

# Show one plot or display image comparison
show_plot_or_comparison = st.radio("", 
                        ("Show Survey Image & HI Contours", 
                         "Compare Two Images"), horizontal=True)


def advanced_display_selection(img2):
    """ Chose colormap and stretch for the comparsion image """

    advanced = st.checkbox("Advanced Display For Comparison Image")
    if advanced:

        cmap_or_reverse = st.radio("Colormap Direction", 
                                ("Regular", "Reversed"), horizontal=True)
        one_prop, two_prop = st.columns([1.5,1])
        # Show colormaps - parse whether they are regular or reversed
        with one_prop:
            if cmap_or_reverse=="Regular":
                cmap = st.selectbox('Colormap', cmap_dict.keys(), 
                                    format_func=lambda x:cmap_dict[x])
            if cmap_or_reverse=="Reversed":
                cmap = st.selectbox('Colormap', cmap_dict.keys(), 
                                    format_func=lambda x:cmap_dict[x])+'_r'
        with two_prop:
            stretch = st.selectbox("Stretch", ('linear', 'log', 'sqrt', 'arcsinh', 'power'))

        # Show image in selected colormap and stretch
        img2.show_colorscale(stretch=stretch, vmin=None, vmid=None, vmax=None, cmap=cmap)
    return


def comparison_fits_images(selected_option):
    """ 
    Display for either with or without HI contours on the comparison image.
    The difference is whether to show or not the HI contours and beam size.

    """
    img2 = fits.open(survey_image2)

    img2 = aplpy.FITSFigure(img2)
    img2.show_grayscale(vmin=None, vmid=None, vmax=None)
    
    img2.recenter(x=ra, y=dec, radius=radius)
    img2.add_scalebar(scalebar_size * u.arcsec, color='white', 
            corner='bottom right', label='10 kpc')
    img2.scalebar.set_linewidth(3)
    img2.scalebar.set_font_size(20)

    if selected_option == 'only_survey':
        advanced_display_selection(img2)

        buf3 = BytesIO()
        img2.savefig(buf3)
        img2.close()

    else:

        advanced_display_selection(img2)
        hdul = fits.open(fits_NHI)
        #img2 = aplpy.FITSFigure(hdul)
        img2.show_contour(hdul, levels=selected_hi_densities, cmap=cmap_hi)       
        img2.add_beam(major=bmaj, minor=bmin, angle=pa, frame=True, facecolor='black')

        buf3 = BytesIO()
        img2.savefig(buf3)
        img2.close()

    return buf3

# Streamlit options
if show_plot_or_comparison == "Show Survey Image & HI Contours":
    st.pyplot()
    img.close()
if show_plot_or_comparison == 'Compare Two Images':

    # Multiple options for Image comparison
    compare_selection = st.radio("Options:", 
            ("Compare Selected Image With & Without HI", 
             "Compare Selected Image With HI and Image From Another Survey",
             "Compare Images From Two Surveys, Both Having HI Contours"))

    if compare_selection=='Compare Selected Image With & Without HI':
        image_comparison(
            img1=Image.open(buf2).convert('RGB'),
            img2=Image.open(buf).convert('RGB'),
            label1=f"{survey_number}",
            label2=f"{survey_number}",
        )

    if compare_selection=='Compare Selected Image With HI and Image From Another Survey':
        survey_number_comp = st.selectbox("Comparison Background Image", (used_surveys))
        
        for i, surv in enumerate(used_surveys):
            if survey_number_comp == surv:
                survey_image2 = get_survey_image(optionImage, used_survey_numbers[i])


        buf3 = comparison_fits_images('only_survey')

        image_comparison(
            img1=Image.open(buf2).convert('RGB'),
            img2=Image.open(buf3).convert('RGB'),
            label1=f"{survey_number}",
            label2=f"{survey_number_comp}",
        )



    if compare_selection=='Compare Images From Two Surveys, Both Having HI Contours':
        survey_number_comp = st.selectbox("Background Image On The Right", (used_surveys))
        
        for i, surv in enumerate(used_surveys):
            if survey_number_comp == surv:
                survey_image2 = get_survey_image(optionImage, used_survey_numbers[i])

        buf3 = comparison_fits_images('twoHI')

        image_comparison(
            img1=Image.open(buf2).convert('RGB'),
            img2=Image.open(buf3).convert('RGB'),
            label1=f"{survey_number}",
            label2=f"{survey_number_comp}",
        )
        
st.button("Refresh Image")