import requests
import datetime as dt
import os
import pprint

# Get the list of user's
# environment variables

nutrition_ID = '6c717fd6'
os.environ['nutrition_ID'] = '6c717fd6'
nutrition_Key = '5d187cc5da6f15a008d8783466c3bc81'
os.environ['nutrition_Key'] = '5d187cc5da6f15a008d8783466c3bc81'
url = 'https://trackapi.nutritionix.com'
check_user = '/v2/users/checkUsername/Bart321231'
natural_exercise = '/v2/natural/exercise'
check_exercise = '/v2/exercise/log/Bart321231'

header = {
    "x-app-id": os.environ['nutrition_ID'],
    'x-app-key': os.environ['nutrition_Key']
}

sheety_get = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1'
sheety_post = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1'
sheety_put = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1/[Object ID]'

# # request = requests.get(url=url, params=check_user)
exercised = input('Tell me what did you do today?')

parameters = {
    'query': exercised,
    'gender': 'male',
    'weight_kg': 75,
    'height_cm': 172,
    'age': 31
}

request = requests.post(url=f'{url}{natural_exercise}', json=parameters, headers=header)
exercises = request.json()['exercises']
print(exercises)
exercises_list = []
for exercise in exercises:
    exer = {'Exercise': exercise['user_input']}
    dur = {'Duration': exercise['duration_min']}
    cal = {'Calories': exercise['nf_calories']}
    temp = (exer, dur, cal)
    exercises_list.append(temp)

# request = requests.get(url=f'{url}{check_exercise}', headers=header, params=check_user)
# print(request.json())
now = dt.datetime.now()

exe_date = {'Date': now.strftime("%d/%m/%Y")}
exe_time = {'Time': now.strftime("%H:%M:%S")}
print(exercises_list[0][0]['Exercise'])
print(exe_date)


for e in exercises_list:
    body = {
         'sheet1': {
             'date': exe_date['Date'],
             'time': exe_time['Time'],
             'exercise': e[0]['Exercise'],
             'duration': e[1]['Duration'],
             'calories': e[2]['Calories'],
        }
    }
    request = requests.post(url=f'{sheety_post}', json=body)
    print(request.json())


#
# data = {
#     "sheet1": {
#         "a": "X",
#         "b": "Y",
#     }
# }
#
# response = requests.post(url=sheety_post, json=data)
print("response.status_code =", request.status_code)
# print("response.text =", request.text)

