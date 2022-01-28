import streamlit as st
from calc import monthly_compounding

st.title('How Rich Will I Be?')

initial = st.number_input(label='Initial Value (£)', min_value=(0), max_value=(1000000000))

monthly = st.number_input(label='Monthly Contribution (£)', min_value=(0), max_value=(1000000))

years = st.number_input(label='Duration (Years)', min_value=(0), max_value=(1000))

annual_rate = st.slider(label='Interest Rate (%)', min_value=1, max_value=12, step=1)

final_sum = monthly_compounding(initial, monthly, annual_rate, years)

st.markdown(f'After {int(years)} years you would have £{round(final_sum, 2)} :sunglasses:')
