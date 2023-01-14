import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year



def load_investor_details(name):
	st.title(name)

	#load recent investment
	st.subheader('Recent Investments')
	recent_df = df[df['invertor'].str.contains(name)].sort_values(by='date',ascending=False)[['date','startup','vertical','city','round','amount']].head(3)
	st.dataframe(recent_df)


	col1,col2 = st.columns(2)

	with col1:
		#biggest investments
		st.subheader('Biggest Investments')
		top_investment_df = df[df['invertor'].str.contains(name)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(3)
		fig,ax = plt.subplots()
		ax.bar(top_investment_df.index,top_investment_df.values)
		st.pyplot(fig)


	with col2:
		#investment verticals
		st.subheader('Investment verticals')
		vertical_df = df[df['invertor'].str.contains(name)].groupby('vertical')['amount'].sum()
		fig1,ax1 = plt.subplots()
		ax1.pie(vertical_df,labels=vertical_df.index,autopct="%0.01f%%")
		st.pyplot(fig1)


	
	col3,col4 = st.columns(2)


	with col3:
		#investment verticals
		st.subheader('Investment Stage')
		vertical_df = df[df['invertor'].str.contains(name)].groupby('round')['amount'].sum()
		fig1,ax1 = plt.subplots()
		ax1.pie(vertical_df,labels=vertical_df.index,autopct="%0.01f%%")
		st.pyplot(fig1)


	with col4:
		#investment verticals
		st.subheader('Invested Cities')
		vertical_df = df[df['invertor'].str.contains(name)].groupby('city')['amount'].sum()
		fig1,ax1 = plt.subplots()
		ax1.pie(vertical_df,labels=vertical_df.index,autopct="%0.01f%%")
		st.pyplot(fig1)



	col5,col6 = st.columns(2)

	with col5:
		st.subheader('YoY Investments')
		df['year'] = df['date'].dt.year
		yoy_df = df[df['invertor'].str.contains(name)].groupby('year')['amount'].sum()
		fig2,ax2 = plt.subplots()
		ax2.plot(yoy_df.index,yoy_df.values)
		st.pyplot(fig2)



def load_overall_analysis():
	st.title("OverAll Analysis")

	col1,col2,col3,col4 = st.columns(4)

	# total invested amt
	total = round(df['amount'].sum())
	col1.metric('Total Money Invested',str(total) + 'Cr.')

	max_investment = round(df['amount'].max())
	col2.metric('Max Amt. Invested',str(max_investment) + 'Cr.')


	average_investment = round(df['amount'].mean())
	col3.metric('Average Invested Amount',str(average_investment) + 'Cr.')


	total_funded_startups = df['startup'].nunique()
	col4.metric('Total Startups Funded',total_funded_startups)


	#mom investments
	st.header("MoM Investments")
	option = st.selectbox('Select Type',['Total','Count'])

	if option == 'Total':
		temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
		temp_df['xaxis'] = temp_df['year'].astype('str') + '-' + temp_df['month'].astype('str')
		temp_df[['amount','xaxis']]

		fig3,ax3 = plt.subplots()
		ax3.plot(temp_df['xaxis'],temp_df['amount'])
		st.pyplot(fig3)

	if option == 'Count':
		temp_df = df.groupby(['year','month'])['startup'].count().reset_index()
		temp_df['xaxis'] = temp_df['year'].astype('str') + '-' + temp_df['month'].astype('str')
		temp_df[['startup','xaxis']]

		fig4,ax4 = plt.subplots()
		ax4.plot(temp_df['xaxis'],temp_df['startup'])
		st.pyplot(fig4)
