import streamlit as st

import pandas as pd

import plotly.express as px


st.title(

"Overview"

)

df = pd.read_csv(

"risk_data.csv"

)

risk = st.sidebar.selectbox(

"Risk Tier",

[

"All",

"Critical Risk",

"Suspicious",

"Clear"

]

)

filtered_df = df.copy()

if risk!="All":

    filtered_df = filtered_df[

    filtered_df[
    'RiskTier'
    ]==risk

    ]


total = filtered_df.shape[0]


fraud = filtered_df[

'ActualFraud'

].sum()


rate = (

fraud

/

total

)*100


avg = filtered_df[

filtered_df[

'ActualFraud'

]==1

][

'TransactionAmt'

].mean()


c1,c2,c3,c4=st.columns(4)


c1.metric(

"Total Transactions",

total

)


c2.metric(

"Fraud Count",

fraud

)


c3.metric(

"Detection Rate",

f"{rate:.2f}%"

)


c4.metric(

"Average Fraud Amount",

f"{avg:.2f}"

)


fig = px.histogram(

filtered_df,

x='TransactionAmt',

color='ActualFraud',

nbins=50

)

st.plotly_chart(

fig,

use_container_width=True

)

st.dataframe(

filtered_df

)
