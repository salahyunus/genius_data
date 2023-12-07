import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

dark_colors = ['#DC143C', 'coral', 'navy', 'darkgreen', '#A52A2A']

df = pd.read_csv('SalahYunus_Clean.csv')

st.set_page_config(layout="wide")

st.sidebar.title("5 Charts")
chart_option = st.sidebar.selectbox("Select a Chart", ["Courses with Most Responses", "Popular Sources", "Countries", "Courses Outside Egypt", "Importance of Online Learning"])

st.title("Genius Data Visualization")

if chart_option == "Courses with Most Responses":
    st.header("Top 5 Courses with Most Responses in September")
    
    df.iloc[:, 10:] = df.iloc[:, 10:].replace({'tick': True, 0: False})
    df_september = df[df['month'] == 9]
    numeric_columns = df_september.iloc[:, 10:].apply(pd.to_numeric, errors='coerce')
    resp = numeric_columns.sum().nlargest(5)
    
    st.bar_chart(resp)

elif chart_option == "Popular Sources":
    st.header("Most Popular Sources Leading to Genius")
    
    country_responses = df['Who told you about Genius?'].value_counts().nlargest(10)
    
    fig, ax = plt.subplots()
    ax.pie(country_responses, labels=None, startangle=90, autopct='%0.0f%%', colors=dark_colors)
    ax.legend(country_responses.index, title='Source', loc='upper right')
    
    st.pyplot(fig)

elif chart_option == "Countries":
    st.header("Countries with Highest Responses")
    
    country_responses = df['Country'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(country_responses, labels=None, startangle=90, colors=dark_colors)
    ax.legend(country_responses.index, title='Countries', loc='upper right')
    
    st.pyplot(fig)

elif chart_option == "Courses Outside Egypt":
    st.header("Courses with Most Responses Outside Egypt")
    
    df.iloc[:, 10:] = df.iloc[:, 10:].replace({'tick': True, 0: False})
    df_september = df[df['Country'] != 'Egypt']
    numeric_columns = df_september.iloc[:, 10:].apply(pd.to_numeric, errors='coerce')
    respo = numeric_columns.sum()
    
    st.bar_chart(respo)

elif chart_option == "Importance of Online Learning":
    st.header("% of People Thinking That Online Learning is Important")
    
    important_resp = df['Is online learning crucial?'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(important_resp, labels=None, startangle=90, autopct='%0.0f%%', colors=dark_colors)
    ax.legend(important_resp.index, title='Is online learning crucial?', loc='upper right')
    
    st.pyplot(fig)

st.sidebar.markdown("Select a visualization option from the sidebar.")