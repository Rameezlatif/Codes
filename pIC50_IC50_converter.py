import streamlit as st
import numpy as np

# Define the function to convert pIC50 to IC50
def pIC50_to_IC50(pIC50):
    # Convert pIC50 to IC50 in molar (M)
    IC50_M = 10**(-pIC50)
    
    # Convert IC50 from molar (M) to nanomoles (nM)
    IC50_nM = IC50_M * 10**9
    
    # Convert IC50 from nanomoles (nM) to micromoles (µM)
    IC50_uM = IC50_nM / 1000
    
    return IC50_nM, IC50_uM

# Define a function to format the output value
def format_value(value):
    if value < 1e-3:
        return "{:.2e}".format(value)
    else:
        return "{:.2f}".format(value)

# Create a Streamlit app
st.title("pIC50 to IC50 Converter")

# Add an input field for the user to enter pIC50 value
pIC50_input = st.number_input("Enter the pIC50 value:", step=0.01)

# Add a button to trigger the conversion
if st.button("Convert"):
    # Convert pIC50 to IC50
    IC50_nM, IC50_uM = pIC50_to_IC50(pIC50_input)

    # Format the values
    IC50_nM_formatted = format_value(IC50_nM)
    IC50_uM_formatted = format_value(IC50_uM)

    # Display the result
    st.write("IC50 in nanomoles (nM):", IC50_nM_formatted)
    st.write("IC50 in micromoles (µM):", IC50_uM_formatted)

