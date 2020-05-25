from win10toast import ToastNotifier
import requests
import json
toaster = ToastNotifier()
from time import sleep

toaster.show_toast("My Personal Convid 19 Tracker",
                   "Bobby Feeno",
                   icon_path="custom.ico",
                   duration=10)

"""
toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
"""
apiData_get = requests.get('https://corona.lmao.ninja/v2/countries/ghana')

apiData_toJSON = apiData_get.json()
text =  f'Confirmed Cases : {apiData_toJSON ["cases"]}\nTotal Deaths: {apiData_toJSON ["deaths"]}'

while True:
  toaster.show_toast("Convid 19 Ghana",text,duration=30,icon_path="virus.ico")
  sleep(3600)