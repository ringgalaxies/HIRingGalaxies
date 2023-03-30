|logo|

HI-RINGS
===============

|Streamlit|

This Streamlit web application allows you to interactively explore our sample of Ring Galaxies (HI-RINGS) using: HI intensity data and images from several other surveys: DSS,, DSS2, WISE, 2MASS and GALEX.


App description:
===============

There are two options for data display within the web application: 
1) Display a survey image and HI contours; 
2) Compare two images. 

App allows you to make these adjustments to the display: image radius, display color options (gray-scale or custom colour map)and image stretch. Next, it is possible to adjust the HI contour display options, choosing which density contours you would like to display and which colour map scheme you want to use. 


Use HI-RINGS localy
--------------------------------

Clone repository and run locally with Streamlit https://streamlit.io/:
::

    $ git clone https://github.com/ringgalaxies/HIRingGalaxies.git
    $ cd HIRingGalaxies
    $ streamlit run 01_Introduction.py

Before you run the App, you will have to make one change in the code to run it locally. 
In the file: ``./pages/02_Explore_Sample_of_Ring_Galaxies.py`` change line 26 ``local_use = "False"`` to ``"True"``.


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


Community guidelines
--------------------
...
...


.. |logo| image:: https://github.com/ringgalaxies/HIRingGalaxies/blob/main/Logo.png
   :width: 200
   :target: https://github.com/ringgalaxies/HIRingGalaxies
   :alt: HI logo
   
.. |Streamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
   :target: https://hi-rings.streamlitapp.com/
   :alt: Streamlit App