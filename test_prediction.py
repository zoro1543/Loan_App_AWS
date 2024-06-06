from app import app
import pytest
import json

@pytest.fixture()
def client():
    return app.test_client()

def test_pinger(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.json == {"message": "Hi there, the endpoint is working!!!"}

def test_prediction(client):
    test_data = {
    "Gender": "Male",
    "Married": "Unmarried",
    "ApplicantIncome": 50000,
    "Credit_History": "Cleared Debts",
    "LoanAmount": 500000
     }
    res = client.post('/predict', json = test_data)
    assert res.status_code == 200
    assert res.json == {
    "loan_approval_status": "Rejected"}
