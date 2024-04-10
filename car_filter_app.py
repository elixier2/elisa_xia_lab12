import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv('car_data.csv')

def filter_data(car_name, transmission_type, selling_price_range, year_range):
    filtered_data = data
    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]
    if transmission_type:
        filtered_data = filtered_data[filtered_data['transmission'].isin(transmission_type)]
    filtered_data = filtered_data[
        (filtered_data['selling_price'] >= selling_price_range[0]) &
        (filtered_data['selling_price'] <= selling_price_range[1])
    ]
    filtered_data = filtered_data[
        (filtered_data['year'] >= year_range[0]) &
        (filtered_data['year'] <= year_range[1])
    ]
    return filtered_data

# Sidebar
st.sidebar.header('Filter Options')
car_name = st.sidebar.text_input('Car Name')
transmission_type = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

if st.sidebar.button('Submit'):
    filtered_data = filter_data(car_name, transmission_type, selling_price_range, year_range)
else:
    filtered_data = data

# Main screen
st.write(filtered_data)
