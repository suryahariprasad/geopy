import streamlit as st
from geopy.geocoders import Nominatim

st.title("Geocoding and Reverse Geocoding App")

option=st.radio(label="Select Mode:",options=["Reverse Geocoding (Lat, Lon->Address)",
                               "Forward Geocoding (Address->Lat, Lon)"])

geolocator = Nominatim(user_agent="geocoding_app")

if option=="Reverse Geocoding (Lat, Lon->Address)":
    lat = st.text_input('Enter Latitude:')
    lon = st.text_input('Enter Longitude:')

    if st.button("Enter:"):
       if lat and lon:
          try:
               lat=float(lat)
               lon=float(lon)
               location=geolocator.reverse((lat,lon))

               if location:
                   st.success(f"Address: {location.address}")
               else:
                   st.warning("No address found")
          except:
              st.error("Please enter a valid latitude and longitude")
       else:
           st.warning("Please enter a valid latitude and longitude")

else:
    address=st.text_input("Enter Address:")

    if st.button("Enter:"):
        if address:
            loc=geolocator.geocode(address)
            if loc:
                st.success(f"Longitude: {loc.longitude}, Latitude: {loc.latitude}")

            else:
                st.error("No address found")

        else:
            st.warning("Please enter a valid address")
