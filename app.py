from flask import Flask, request
import pickle

app = Flask(__name__)

# loading the ML model
model_pickle = open("Train_data/classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@app.route('/')
def hello():
    return "<p>Hello World</p>"

## first sample endpoint
@app.route("/ping", methods=['GET'])
def ping():
    return {"message": "Hi there, the endpoint is working!!!"}


## endpoint to get template request for model inference
@app.route("/template", methods = ['GET'])
def get_template():
    return {
	"Gender": "Male/Female",
	"Married": "Married/Unmarried",
	"ApplicantIncome": "<Numeric Salary>",
	"LoanAmount": "Numeric loan amount",
	"Credit_History": "Cleared Debts / Uncleared Debts"}


##defining the endpoint for the classification
@app.route("/predict", methods=["POST", "GET"])
def prediction():
    """
    Returns the loan application status using ML model.
    """
    loan_req = request.get_json()
    if loan_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1
    if loan_req['Married'] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        credit_status = 0
    else:
        credit_status = 1
    applicant_income = loan_req['ApplicantIncome']
    loan_amt = loan_req['LoanAmount']

    result = clf.predict([[gender, marital_status, applicant_income, loan_amt, credit_status]])

    if result[0] == 0:
        pred = "Rejected"
    else: 
        pred = "Approved"

    return {"loan_approval_status": pred}    





