import streamlit as st
import pandas as pd
from indian_startup_func import load_investor_details,load_overall_analysis



df = pd.read_csv('startup_cleaned.csv')


st.set_page_config(layout='wide',page_title='Startup Analysis')

st.sidebar.title('Startup Funding Analysis')




option = st.sidebar.selectbox('Select One',['OverAll Analysis','Startup','Investor'])


if option == 'OverAll Analysis':
	load_overall_analysis()



elif option == 'Startup':
	st.title("Startup Analysis")
	st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
	btn1 = st.sidebar.button('Find Startup Details')


else:
	investor = st.sidebar.selectbox('Select Investor',sorted(set(df['invertor'].str.split(',').sum())))
	btn2 = st.sidebar.button('Find Investor Details')
	if btn2:
		load_investor_details(investor)
