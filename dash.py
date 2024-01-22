import streamlit as st
import pandas as pd
import numpy as np
import random

def generate_data():
    dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
    usage = [random.randint(0, 100) for _ in range(len(dates))]
    df = pd.DataFrame({'Date': dates, 'Usage': usage})
    return df

def create_monthly_bar_graph(df):
    months = df['Date'].dt.month_name().unique()
    for month in months:
        monthly_data = df[df['Date'].dt.month_name() == month]
        st.subheader(month)
        st.bar_chart(monthly_data.set_index('Date')['Usage'])


def main():
    st.title("Daily Usage")
    df = generate_data()
    create_monthly_bar_graph(df)

if __name__ == '__main__':
    main()
