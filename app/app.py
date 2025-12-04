import streamlit as st
from predict import predict

st.title("Iris Species Predictor")
st.write(
    "App to predict the species of an Iris flower "
    "based on its sepal and petal parameters."
)

st.header("Enter Flower Parameters (cm)")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length", min_value=0.0, max_value=10.0, value=0.0, step=0.1
    )
    sepal_width = st.number_input(
        "Sepal Width", min_value=0.0, max_value=10.0, value=0.0, step=0.1
    )

with col2:
    petal_length = st.number_input(
        "Petal Length", min_value=0.0, max_value=10.0, value=0.0, step=0.1
    )
    petal_width = st.number_input(
        "Petal Width", min_value=0.0, max_value=10.0, value=0.0, step=0.1
    )


if st.button("Predict Species"):

    features = [sepal_length, sepal_width, petal_length, petal_width]
    
    predicted_species = predict(features)
    
    st.success(f"The predicted species is: **{predicted_species.capitalize()}**")