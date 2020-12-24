
#import streamlit as st
#st.write('hello world')

#x=st.slider('x')
#st.write(x, 'x+x=', x+x)

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# LOADING DATA
DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(100000)

#hour=st.sidebar.number_input('hour',0,23,10)
#data=data[data[DATE_TIME].dt.hour==hour]
#'## Geo Data at %sh' %hour
#st.map(data)
def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.beta_columns((2,3))

with row1_1:
    st.title("NYC Uber Ridesharing Data")
    hour = st.sidebar.slider("Select hour of pickup", 0, 23)

with row1_2:
    st.write(
    """
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """)

# FILTERING DATA BY HOUR SELECTED
data = data[data[DATE_TIME].dt.hour == hour]

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))

# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
la_guardia= [40.7900, -73.8700]
jfk = [40.6650, -73.7821]
newark = [40.7090, -74.1805]
zoom_level = 12
midpoint = (np.average(data["lat"]), np.average(data["lon"]))

with row2_1:
    st.write("**All New York City from %i:00 and %i:00**" % (hour, (hour + 1) % 24))
    map(data, midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**La Guardia Airport**")
    map(data, la_guardia[0],la_guardia[1], zoom_level)

with row2_3:
    st.write("**JFK Airport**")
    map(data, jfk[0],jfk[1], zoom_level)

with row2_4:
    st.write("**Newark Airport**")
    map(data, newark[0],newark[1], zoom_level)
'## Geo Data at %sh' %hour
data