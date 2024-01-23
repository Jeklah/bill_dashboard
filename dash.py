import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
usage = np.random.randint(0, 100, len(dates))
df = pd.DataFrame({'Date': dates, 'Usage': usage})

st.title('Daily Usage')
st.sidebar.title('Sidebar')

addresses = ['114, Basingstoke Road, Reading',
             '15 Grage Avenue, Reading',
             '38 Swainstone Road, Reading',
             '132, Flat 1, Basingstoke Road',
             '33 Grange Avenue, Reading',
             '7, St Edwards Road, Reading',
             '3, St Edwards Road, Reading',
             '5, St Edwards Road, Reading']
selected_address = st.sidebar.selectbox('Select Address', addresses)

st.write(f'Usage for {selected_address}')
usage_adjustment = st.sidebar.slider(
    'Adjust Usage', min_value=0, max_value=100, value=50)

df['Adjusted Usage'] = df['Usage'] * (usage_adjustment / 100)

df['Month'] = df['Date'].dt.month_name()
monthly_data = df.groupby(['Month', df['Date'].dt.day])[
    'Adjusted Usage'].sum().reset_index()

months = df['Month'].unique()
for month in months:
    data = monthly_data[monthly_data['Month'] == month]
    plt.figure(figsize=(10, 5))
    plt.bar(data['Date'], data['Adjusted Usage'])
    plt.xlabel('Day')
    plt.ylabel('Usage')
    plt.title(f'Daily Usage - {month}')
    plt.xticks(rotation=45)
    st.pyplot(plt)


st.subheader('Example Data')
st.dataframe(df)
