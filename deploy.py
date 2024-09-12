import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('new_best_model.pkl')

# Mapping dictionaries for categorical variables with descriptions
categorical_mappings = {
    'Role': {
        'What is your role in the organization?': {
            'Developer': 0,
            'Project Manager': 1,
            'Quality Assurance Engineer': 2,
            'SoftWare Engineer': 3,
            'Technical Consultant': 4,
            'Trainee': 5,
            'UI / UX Designer': 6
        }
    },
    'OrganizationType': {
        'What is your Organization Type?': {
            'Corporate IT department': 0,
            'Federal Ministry': 1,
            'Freelancer': 2,
            'Private Software Company': 3,
            'Public Software Company': 4,
            'Software Development Agency': 5,
            'Solar Technology and Installation Company': 6
        }
    },
    'ProgrammingLanguage': {
        'What Programming Language was Used?': {
            'HTML/JavaScript/PHP': 0,
            'Java': 1,
            'Java, HTML/Javascript/PHP': 2,
            'JavaScript': 3,
            'JavaScript, C#, HTML/Javascript/PHP': 4,
            'JavaScript, HTML/Javascript/PHP': 5,
            'Javascript, ReactJs, PHP': 6,
            'Kotlin': 7,
            'Python': 8,
            'Python, Java, Javascript, C#, HTML/Javascript': 9,
            'Python, Javascript, Node': 10,
            'Typescript/PHP': 11
        }
    }
}

# Title of the app
st.title("Software Cost Estimation App")
st.sidebar.header("Let's Predict the Cost of Your Software")

# Dropdown for selecting Role
role = st.sidebar.selectbox("Select Your Role", list(categorical_mappings['Role']['What is your role in the organization?'].keys()))

# Dropdown for selecting Organization Type
organization_type = st.sidebar.selectbox("Customer Organization Type", list(categorical_mappings['OrganizationType']['What is your Organization Type?'].keys()))

# Dropdown for selecting Programming Language
programming_language = st.sidebar.selectbox("Programming Language Used", list(categorical_mappings['ProgrammingLanguage']['What Programming Language was Used?'].keys()))

# Numeric inputs
estimated_cost = st.number_input("Estimated Cost (Naira)", min_value=0)
software_complexity = st.slider("Software Complexity (1-10)", 1, 10)
team_communication = st.slider("Communication Among Team (1-10)", 1, 10)
income_satisfaction = st.slider("Income Satisfaction (1-10)", 1, 10)

# Mapping the selected categorical inputs to their corresponding numeric values
role_numeric = categorical_mappings['Role']['What is your role in the organization?'][role]
organization_type_numeric = categorical_mappings['OrganizationType']['What is your Organization Type?'][organization_type]
programming_language_numeric = categorical_mappings['ProgrammingLanguage']['What Programming Language was Used?'][programming_language]

# Prediction button
if st.sidebar.button("Estimate Cost"):
    # Prepare the input data as a numpy array
    input_data = np.array([[role_numeric, organization_type_numeric, programming_language_numeric,
                            estimated_cost, software_complexity, team_communication,
                            income_satisfaction]])

    # Make predictions using the model
    prediction = model.predict(input_data)

    # Display the prediction result
    st.success(f"Predicted Software Cost: {prediction[0]:.2f} Naira")

# Footer
st.sidebar.text("By: Saoban Lateefat")
st.sidebar.text("Final Year Project")
