|logo|

HI-RINGS
===============

|Streamlit|

This Streamlit web application allows you to interactively explore our sample of Ring Galaxies (HI-RINGS) using: HI intensity data and images from several other surveys: DSS,, DSS2, WISE, 2MASS and GALEX.


Use HI-RINGS localy
--------------------------------

Clone repository and run locally with Streamlit https://streamlit.io/:
::

    $ git clone https://github.com/ringgalaxies/HIRingGalaxies.git
    $ cd HIRingGalaxies
    $ streamlit run 01_Introduction.py


**Requirements:**
-----------------
Code is written in Python 3.9.7, below are the packages which are used in the code:

- ``streamlit == 1.11.0``
- ``matplotlib >= 3.4.3``
- ``astropy >= 4.3.1``
- ``aplpy == 2.1.0``
- ``streamlit_image_comparison == 0.0.2``
- ``cmasher >= 1.6.3``



Structure
---------

.. code-block:: raw
   
   HI-RINGS
   
   ├── 01_introduction.py       # HI-RINGS main file
   ├── side_logo_func.py        # Helper functions

   ├── README.rst
   ├── requirements.txt         # List of used packages
   └── LICENSE                  # To be added
   │
   ├── data
   │   ├── Galaxy Folders        # Individual galaxy data

   │
   ├── pages
   │   ├── 02_Explore_Sample_of_Ring_Galaxies.py        # Explore HI-RINGS page
   │   ├── 03_Literature.py                             # App page with references




.. |logo| image:: https://github.com/ringgalaxies/HIRingGalaxies/blob/main/Logo.png
   :width: 400
   :target: https://github.com/ringgalaxies/HIRingGalaxies
   :alt: HI logo
   
.. |Streamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
   :target: https://hi-rings.streamlitapp.com/
   :alt: Streamlit App