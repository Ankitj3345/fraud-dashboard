import streamlit as st

import pandas as pd

import shap

import joblib

import matplotlib.pyplot as plt


st.title(

"SHAP Explainer"

)


model = joblib.load(

"model.pkl"

)


df = pd.read_csv(

"risk_data_small.csv"

)


explainer = shap.TreeExplainer(

model

)


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

        x = row.drop(

        [

        'FraudProbability',

        'RiskTier',

        'ActualFraud'

        ],

        axis=1,

        errors='ignore'

        )


        shap_values = explainer.shap_values(

        x

        )


        fig = plt.figure()


        shap.plots.waterfall(

        shap.Explanation(

        values=

        shap_values[0],

        base_values=

        explainer.expected_value,

        data=

        x.iloc[0],

        feature_names=

        x.columns

        ),

        show=False

        )


        st.pyplot(

        fig

        )


        prob = row[

        'FraudProbability'

        ].iloc[0]


        st.metric(

        "Fraud Probability",

        f"{prob:.3f}"

        )


        if prob>=0.75:

            st.error(

            "Critical fraud risk."

            )

        elif prob>=0.40:

            st.warning(

            "Suspicious transaction."

            )

        else:

            st.success(

            "Legitimate transaction."

            )


        st.write(

        "High SHAP features increased fraud probability."

        )
