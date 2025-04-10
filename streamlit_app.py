import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st
import os



# Set the page title and description
st.title("University Admission Rate Prediction")
st.write("""
This app predicts whether a student will be admitted to UCLA  based on their SAT scores,GPA, and other scores.
""")

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "models", "Neural_model.pkl")


try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    import streamlit as st
    st.error(f"Failed to load model: {e}")



# Prepare the form to collect user inputs
with st.form("user_inputs"):
    st.subheader("Student Details")
    
    # GRE Score input
    GRE_Score= st.number_input("What is the candidate's GRE Score?", 
                                         min_value=0,
                                         max_value=360,
                                         step=10)
    # TOEFL Score input
    TOEFL_Score= st.number_input("What is candidate's Toefl Score?", 
                                         min_value=0, 
                                         max_value=120,
                                         step=10)
    # Strength of purpose letter
    SOP= st.number_input("What is candidate's statement of purpose strength score(1-5)?", 
                                         min_value=0, 
                                         max_value=5,
                                         step=1)
    # Letter of recommendation strength
    LOR= st.number_input("What is candidate's letter of recommendation strength score(1-5)?", 
                                         min_value=0, 
                                         max_value=5,
                                         step=1)
    # GPA Rating
    GPA= st.number_input("What is candidate's GPA?",
                                         min_value=0, 
                                         max_value=10,
                                         step=1)
    # University Rank
    University_Rank= st.number_input("What is candidate's university rank(1-5)?",
                                         min_value=1, 
                                         max_value=5)
    # Research
    Research= st.selectbox("Has the candidate done any research?", 
                options=["Yes", "No"])
    
    # Submit button
    submitted = st.form_submit_button("Predict Admit Chance")


# Handle the dummy variables to pass to the model
if submitted:
  

    # Convert Loan Amount Term and Credit History to integers
    GRE_Score = int(GRE_Score)
    TOEFL_Score = int(TOEFL_Score)
    SOP= int(SOP)
    LOR= int(LOR)
    GPA= float(GPA)
    
    # Create if statements for dummy variables
    if University_Rank == 1:
        University_Rating_1 = 1
        University_Rating_2 = 0
        University_Rating_3 = 0
        University_Rating_4 = 0
        University_Rating_5 = 0
    elif University_Rank == 2:
        University_Rating_1 = 0
        University_Rating_2 = 1
        University_Rating_3 = 0
        University_Rating_4 = 0
        University_Rating_5 = 0
    elif University_Rank == 3:
        University_Rating_1 = 0
        University_Rating_2 = 0
        University_Rating_3 = 1
        University_Rating_4 = 0
        University_Rating_5 = 0
    elif University_Rank == 4:
        University_Rating_1 = 0
        University_Rating_2 = 0
        University_Rating_3 = 0
        University_Rating_4 = 1
        University_Rating_5 = 0
    elif University_Rank == 5:
        University_Rating_1 = 0
        University_Rating_2 = 0
        University_Rating_3 = 0
        University_Rating_4 = 0
        University_Rating_5 = 1
    
    Research_0 = 0 if Research == "Yes" else 1
    Research_0 = 1 if Research == "No" else 0

    Research_1 = 1 if Research == "Yes" else 0
    Research_1 = 1 if Research == "No" else 0

    

    # Prepare the input for prediction. This has to go in the same order as it was trained
    prediction_input = [[GRE_Score, TOEFL_Score, SOP,
        LOR, GPA, University_Rating_1, University_Rating_2,
        University_Rating_3, University_Rating_4, University_Rating_5, Research_0,
            Research_1
    ]]

    # Make prediction
    new_prediction = Nmodel.predict(prediction_input)

    # Display result
    st.subheader("Prediction Result:")
    st.write(f"{new_prediction[0]}")

    '''if new_prediction[0] == 1:
        st.write("You will be admitted!")
    else:
        st.write("Sorry, you are not eligible.")'''
   
st.write(
    """We used a machine learning ,MLPClassifier (Multiple Layer Perceptron Classifier) model to predict your eligibility of getting accepted to UCLA."""
)
