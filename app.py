import streamlit as st
import matplotlib as plt
import pandas as pd
from backend import load_data, get_summary, plot_sales_over_time

def main():
    st.title('Supermarket Sales Dashboard')

    # Load data 
    data = load_data()
    pr_lines_lst = data['Product line'].unique()
    cities_lst = data['City'].unique()
   

    # Interactive widgets
    st.sidebar.header('Controls')
    min_rating = st.sidebar.slider('Minimum Rating', min_value=0, max_value=10, value=5, step=1)
    line = st.sidebar.multiselect("Product line", options =pr_lines_lst, default=pr_lines_lst)
    cities = st.sidebar.multiselect('City', options=cities_lst, default= cities_lst)
    gender= st.sidebar.radio('Gender', options=["Male", "Female"])
    cust_type= st.sidebar.radio('Customer type', options=["Member", "Normal"])
    
    # Filter by rating
    filtered_data = data[
    (data['Rating'] >= min_rating) & 
    (data['Product line'].isin(line)) & 
    (data['City'].isin(cities)) & 
    (data['Customer type']==cust_type) &
    (data['Gender']==gender)
]

    # Summary statistics
    updated_summary = get_summary(filtered_data)
    st.write("### Summary Statistics")
    st.table(updated_summary)


    # Plotting
    st.write("### Sales Over Time")

    # chart_data = filtered_data(), columns=["a", "b", "c"])
    data['Date'] = pd.to_datetime(data['Date'])
    sales_over_time = data.groupby(data['Date'].dt.date)['Total'].sum()
    st.line_chart(sales_over_time)


    #plt = plot_sales_over_time(filtered_data)
    # st.pyplot(plt)



     # Display raw data
    st.write("### Raw Data")
    st.dataframe(filtered_data)


if __name__ == '__main__':
    main()