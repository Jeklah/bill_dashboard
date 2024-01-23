import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Generate some data.
data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', '2023-12-31', freq='D'),
    'Electricity': np.random.randint(0, 100, 365),
    'Gas': np.random.randint(0, 50, 365)
})

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


# Sidebar sliders to adjust usage.
electricity_usage = st.sidebar.slider(
    'Electricity Usage', min_value=0, max_value=100, value=50, step=10)
gas_usage = st.sidebar.slider(
    'Gas Usage', min_value=0, max_value=100, value=50, step=10)

# Calculate monthly cost
electricity_rate = 0.15
gas_rate = 0.04

monthly_elec_cost = electricity_usage * electricity_rate
monthly_gas_cost = gas_usage * gas_rate

# Filter data based on slider values
filtered_data = data.copy()
filtered_data['Electricity'] = filtered_data['Electricity'] * \
    electricity_usage / 100
filtered_data['Gas'] = filtered_data['Gas'] * gas_usage / 100

# Select a month to plot
selected_month = st.sidebar.selectbox(
    'Select Month', data['Date'].dt.strftime('%B').unique())

# Group data by month.
monthly_data = filtered_data[data['Date'].dt.strftime('%B') == selected_month]


st.title('Daily Usage')
st.write(f'Usage for {selected_address}')

# Display monthly cost
st.write(f'Monthly Electricity Cost: £{monthly_elec_cost:.2f}')
st.write(f'Monthly Gas Cost: £{monthly_gas_cost:.2f}')

# Arrows to select previous and next month
current_index = df[df['Month'] == selected_month].index[0]
if current_index > 0:
    st.button('Previous Month')
if current_index < len(df) - 1:
    st.button('Next Month')

# Plot bar graphs for each month
fig, ax = plt.subplots()
ax.bar(monthly_data['Date'], monthly_data['Electricity'], label='Electricity')
ax.bar(monthly_data['Date'], monthly_data['Gas'], label='Gas', alpha=0.7)
plt.xlabel('Month')
plt.ylabel('Usage')
plt.title(f'Daily Electricity and Gas Usage for {selected_month}')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
st.pyplot(fig)
