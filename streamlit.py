import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px


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

st.text("Map is loading (may take a minute...)")


df2 = pd.read_csv("Model/price_median.csv")
df2 = df2.rename(columns={"zip": "zip_codes"})


with open("Data/ca_california_zip_codes_geo.min.json") as f:
    zip_codes = json.load(f)


fig = px.choropleth(df2, geojson=zip_codes, locations="zipcode", color="housing_price", featureidkey="properties.ZCTA5CE10") 

fig.update_geos(fitbounds="locations", visible=True)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig 