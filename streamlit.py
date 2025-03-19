import streamlit as st
import pandas as pd
import numpy as np


# Set the title of the app
st.title("California Housing Prices")

df = pd.read_csv("Model/price_median.csv")

zip_code = st.text_input("Zip Code", "", )
if zip_code != "":
  zip_code = int(zip_code)
  if zip_code in df.zipcode.values:
    st.write("The average housing price in", str(zip_code), "is $", str(int(df.loc[df.zipcode == zip_code,'housing_price'].values[0]*100000)))
  else:
    st.write("Zip code not found in the dataset.")





# from urllib.request import urlopen
# import json

# with open("Data/Zip_Codes.geojson") as f:
#     zip_codes = json.load(f)


# import plotly.graph_objects as go

# df2 = pd.DataFrame({"zipcode": ["90210", "90069"], "housing_price": [10,50]})

# st.write(df2.loc[0,"zipcode"])

# fig = go.Figure(go.Choroplethmap(geojson=zip_codes, locations=df2.zipcode, z=df2.housing_price,
#                                     colorscale="Viridis", zmin=0, zmax=12,
#                                     marker_opacity=0.5, marker_line_width=0))
# fig.update_layout(map_style="carto-positron",
#                   map_zoom=3, map_center = {"lat": 37.0902, "lon": -95.7129})
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()


import pandas as pd
from urllib.request import urlopen
import json


df2 = pd.read_csv("Model/price_median.csv")
df2 = df2.rename(columns={"zip": "zip_codes"})


with open("Data/ca_california_zip_codes_geo.min.json") as f:
    zip_codes = json.load(f)

import plotly.express as px

fig = px.choropleth(df2, geojson=zip_codes, locations="zipcode", color="housing_price", featureidkey="properties.ZCTA5CE10") 

fig.update_geos(fitbounds="locations", visible=True)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig 
