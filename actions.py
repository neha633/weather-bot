from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        params = {
          'access_key': '3ef566d5fbe860f06c2582b65b1d60b0', # Put your API key
          'query': loc
        }
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()
        response = 'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
        #response = "weather is absolutely fantastic in %s" %loc
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]