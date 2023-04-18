import requests
from datetime import datetime

APP_ID="e73aeb08"
APP_KEY= "35c407a9276ba70346999a517cc03707"
GENDER="MALE"
WEIGHT = 68
HEIGHT = 172
AGE = 23

WORKOUT=input("which workout did you do today: ")

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint="https://api.sheety.co/81c10cfbdcd16803a080ca053e6729df/myWorkouts/workouts"

user_data={
    "query":WORKOUT,
     "gender":GENDER,
     "weight_kg":WEIGHT,
     "height_cm":HEIGHT,
     "age":AGE,
}
headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}
exercise=requests.post(url=exercise_endpoint,json=user_data,headers=headers)
result = exercise.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
print(exercise["duration_min"])
sheet_response = requests.post(url=sheets_endpoint, json= sheet_inputs ,headers=headers)



