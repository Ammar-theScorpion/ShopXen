# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# try new, can be deleted 
# from rasa_sdk import Action, Tracker
# import random

# class YourAssistant(Action):
#     def name(self) -> str:
#         return 'Your Assistant'
    
#     async def run(self, dispatcher, tracker, domain):
#         response = None
        
#         # Check if the incoming message contains "product warranty"
#         if 'product_warranty' in tracker.latest_message.get('data', {}):
#             # Randomly generate a positive or negative statement
#             has_warranty = random.choice([True, False])
            
#             if has_warranty:
#                 response = f"Yes, this product comes with a one-year warranty."
#             else:
#                 response = f"No, this product does not come with any warranty."
                
#         return Response(response=response, tracker=tracker)
