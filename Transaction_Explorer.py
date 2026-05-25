import streamlit as st

import pandas as pd


st.title(

"Transaction Explorer"

)

df = pd.read_csv(

"risk_data_small.csv"

)

risk = st.sidebar.selectbox(

"Risk Filter",

[

"All",

"Critical Risk",

"Suspicious",

"Clear"

]

)

if risk!="All":

    df = df[

    df[
    'RiskTier'
    ]==risk

    ]


transaction = st.text_input(

"Enter TransactionID"

)


if transaction:

    row = df[

    df[
    'TransactionID'
    ].astype(str)

    == transaction

    ]

    if row.shape[0]>0:

        score = row[

        'FraudProbability'

        ].iloc[0]

        st.metric(

        "Risk Score",

        f"{score:.3f}"

        )

        st.dataframe(

        row

        )


st.dataframe(

df

)
