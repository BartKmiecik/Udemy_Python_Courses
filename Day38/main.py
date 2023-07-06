import requests

nutrition_ID = '6c717fd6'
nutrition_Key = '5d187cc5da6f15a008d8783466c3bc81'
url = 'https://trackapi.nutritionix.com'
check_user = '/v2/users/checkUsername/Bart321231'
natural_exercise = '/v2/natural/exercise'
check_exercise = '/v2/exercise/log/Bart321231'

header = {
    "x-app-id": nutrition_ID,
    'x-app-key': nutrition_Key
}

parameters = {
    'query': "I've been running for 30 min",
    'gender': 'male',
    'weight_kg': 75,
    'height_cm': 172,
    'age': 31
}

sheety_get = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1'
sheety_post = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1'
sheety_put = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/myWorkouts/sheet1/[Object ID]'

# # request = requests.get(url=url, params=check_user)
#
# request = requests.post(url=f'{url}{natural_exercise}', json=parameters, headers=header)
# # print(request.text)
# request = requests.get(url=f'{url}{check_exercise}', headers=header, params=check_user)
# print(request.json())


request = requests.get(url=sheety_get)
print(request.json())

