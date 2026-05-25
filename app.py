
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(
page_title="Fraud Dashboard",
layout="wide"
)

df=pd.read_csv(
"risk_data_small.csv"
)

st.title(
"Fraud Dashboard"
)

risk=st.sidebar.selectbox(

"Risk Tier",

[
"All",
"Critical Risk",
"Suspicious",
"Clear"
]

)

filtered_df=df.copy()

if risk!="All":

    filtered_df=filtered_df[

    filtered_df[
    'RiskTier'
    ]==risk

    ]

total=filtered_df.shape[0]

fraud=filtered_df[
'ActualFraud'
].sum()

rate=(

fraud

/

total

)*100

avg=filtered_df[

filtered_df[
'ActualFraud'
]==1

][
'TransactionAmt'
].mean()

c1,c2,c3,c4=st.columns(4)

c1.metric(
"Transactions",
total
)

c2.metric(
"Fraud",
fraud
)

c3.metric(
"Detection Rate",
f"{rate:.2f}%"
)

c4.metric(
"Avg Fraud Amount",
f"{avg:.2f}"
)

fig=px.histogram(

filtered_df,

x='TransactionAmt',

color='ActualFraud'

)

st.plotly_chart(
fig
)

st.dataframe(
filtered_df
)
