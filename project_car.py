import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("car_data.csv")

# Sidebar
st.sidebar.title("Filters")
car_name_input = st.sidebar.text_input("Car Name (Optional)")
transmission_options = st.sidebar.multiselect("Transmission", ["Manual", "Automatic"], default=["Manual", "Automatic"])
selling_price_range = st.sidebar.slider("Selling Price Range", 0, 100, (0, 20))
year_range = st.sidebar.slider("Year Range", 2000, 2024, (2000, 2024))
submit_button = st.sidebar.button("Submit")

# Filter the data
filtered_df = df.copy()
if car_name_input:
    filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name_input, case=False)]
if transmission_options:
    filtered_df = filtered_df[filtered_df['Transmission'].isin(transmission_options)]
filtered_df = filtered_df[(filtered_df['Selling_Price'] >= selling_price_range[0]) & (filtered_df['Selling_Price'] <= selling_price_range[1])]
filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]

# Main screen
st.title("Filtered Car Data")
if submit_button:
    st.write(filtered_df)
else:
    st.write(df)