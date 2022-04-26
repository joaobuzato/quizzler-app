import requests
params = {
    "amount": 20,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=params).json()
question_data = response['results']
