import requests
import json
import win32com.client


city = input("Which City's weather do you want to know about?\n")

url = f"https://api.weatherapi.com/v1/current.json?key=317be8f521104a58a1163114240806&q={city}"

r= requests.get(url)

# print(r.text)
weather_dic = json.loads(r.text)
w = weather_dic["current"]["temp_c"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

s=f"The current weather in {city} is {w} Degree's Celsius"
print(s)
speaker.Speak(s)


