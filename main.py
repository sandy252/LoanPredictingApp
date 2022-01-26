import streamlit as st
import pickle
# from database import database
import pymongo
from sklearn.preprocessing import MinMaxScaler

# loading our classifier model
def load_predictor_model():
    with open("predictor.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# loading the scaling model
def load_scaler_model():
    with open("scaler.pkl", "rb") as file:
        scaler = pickle.load(file)
    return scaler

# creating an instance of the database
# db_obj = database()

def predict(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, Loan_Amount, Loan_Amount_Term, Credit_History, Property_Area):

    # first feature

    if(Gender == "Male"):
        Gender_Male = 1
    else:
        Gender_Male = 0

    # second feature

    if(Married == "Yes"):
        Married_Yes = 1
    else:
        Married_Yes = 0

    # third feature

    if(Dependents == 1):
        Dependents_1 = 1
        Dependents_2 = 0
        Dependents_3 = 0
    elif(Dependents == 2):
        Dependents_1 = 0
        Dependents_2 = 1
        Dependents_3 = 0
    elif(Dependents == '3+'):
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 1
    else:
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 0

    # fourth feature

    if Education == 'NotGraduate':
        Education_NotGraduate = 1
    else:
        Education_NotGraduate = 0

    # fifth feature

    if(Self_Employed == 'Yes'):
        Self_Employed_Yes = 1
    else:
        Self_Employed_Yes = 0

    # sixth feature

    if(Property_Area == "Urban"):
        Property_Area_Urban = 1
        Property_Area_Semiurban = 0
    elif(Property_Area == "Semi urban"):
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1
    else:
        Property_Area_Urban = 0
        Property_Area_Semiurban = 0

    # seventh feature

    if(Credit_History == "Available"):
        Credit_History= 1
    else:
        Credit_History = 0

    # Eighth feature

    Loan_Amount_Term = int(Loan_Amount_Term)/12

    scaler = load_scaler_model()
    transformed_num_feature = scaler.transform([[ApplicantIncome, Loan_Amount, CoapplicantIncome]])

    # Ninth feature

    ApplicantIncome = transformed_num_feature[0][0]

    # Tenth feature

    Loan_Amount = transformed_num_feature[0][1]

    # Eleventh feature

    CoapplicantIncome = transformed_num_feature[0][2]






    model = load_predictor_model()
    prediction = model.predict([[
                                Loan_Amount_Term,
                                Credit_History,
                                Gender_Male,
                                Married_Yes,
                                Dependents_1,
                                Dependents_2,
                                Dependents_3,
                                Education_NotGraduate,
                                Self_Employed_Yes,
                                Property_Area_Semiurban,
                                Property_Area_Urban,
                                ApplicantIncome,
                                CoapplicantIncome,
                                Loan_Amount
                                ]])
    return prediction


def main():  # Main function for streamlit
    st.title("Loan Eligibility predicting Webapp built with Streamlit")
    html_temp = """
    <div style="background-color: tomato;padding:10px;text-align:center">
    <h2 style="color:white;text-align:center;">Please provide all the details given below</h2>
    </div>
    """

    sex = ("Male",
           "Female")
    marital_status = ("Yes",
                      "No")
    Dependent = ("0",
                 "1",
                 "2",
                 "3+")
    Edu = ("Graduate",
           "NotGraduate")
    Self_emp = ("Yes",
                "No")
    Prop_Area = ("Urban",
                 "Semi urban",
                 "Rural")
    Credit_hist = ("Available",
                   "Not Available")

    st.markdown(html_temp, unsafe_allow_html=True)
    Gender = st.selectbox("Gender", sex)
    Married = st.selectbox("Married", marital_status)
    Dependents = st.selectbox("Dependents", Dependent)
    Education = st.selectbox("Education", Edu)
    Self_Employed = st.selectbox("Self Employed", Self_emp)
    ApplicantIncome = st.text_input("Applicant Income (In USD)")
    CoapplicantIncome = st.text_input("Coapplicant Income (INnUSD)")
    Loan_Amount = st.text_input("Loan Amount (In USD)")
    Loan_Amount_Term = st.text_input("Loan Amount Term (In months)")
    Credit_History = st.selectbox("Credit History", Credit_hist)
    Property_Area = st.selectbox("Property Area", Prop_Area)
    if st.button("Predict"):
        result = predict(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, Loan_Amount, Loan_Amount_Term, Credit_History, Property_Area)
        if result == 'Y':
            # send data to the related collection in mongodb
            # Eligible_records = {"Gender": Gender, "Married": Married, "Dependents": Dependents,
            #                     "Education": Education, "Self_Employed": Self_Employed, "ApplicantIncome":ApplicantIncome,
            #                     "CoapplicantIncome": CoapplicantIncome, "Loan_Amount": Loan_Amount, "Loan_Amount_Term": Loan_Amount_Term,
            #                     "Credit_History": Credit_History, "Property_Area": Property_Area}
            # db_obj.insert_Ele_records(Eligible_records)
            st.success("The customer can take loan")
        else:
            # send data to the related collection in mongodb
            # Not_Eligible_records = {"Gender": Gender, "Married": Married, "Dependents": Dependents,
            #                     "Education": Education, "Self_Employed": Self_Employed,
            #                     "ApplicantIncome": ApplicantIncome,
            #                     "CoapplicantIncome": CoapplicantIncome, "Loan_Amount": Loan_Amount,
            #                     "Loan_Amount_Term": Loan_Amount_Term,
            #                     "Credit_History": Credit_History, "Property_Area": Property_Area}
            # db_obj.insert_not_ele_records(Not_Eligible_records)
            st.success("The customer cannot take loan")


if __name__ == '__main__':
    main()