# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

import base64
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

class About(Action):
	def name(self):
		return "action_about"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ['I am a chatbot. I am here to help you.',
                    'I am your virtual assistant to guide you through this app.']
		reply = random.choice(messages)
		dispatcher.utter_message(text = reply)
		return []

class OutOfScope(Action):
	def name(self):
		return "action_out_of_scope"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		dispatcher.utter_message(text=reply)
		return [UserUtteranceReverted()]

class ActionDefaultFallback(Action):
	def name(self) -> Text:
		return "action_handle_fallback"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		dispatcher.utter_message(text=reply)
		return [UserUtteranceReverted()]

class Greeting(Action):
	def name(self):
		return "action_greeting"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Hi there. It's such a pleasure to have you here 🤗. How can I help you.",
					"Hello 👋😃 How can I assist you."]
		reply = random.choice(messages)
		dispatcher.utter_message(text = reply)
		return []

class AfterGreeting(Action):
	def name(self):
		return "action_after_greet"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["I am fine. 🤟😎🤟",
                    "Better than ever 😎"]
		reply = random.choice(messages)
		dispatcher.utter_message(text=reply)
		return []

class Goodbye(Action):
	def name(self):
		return "action_goodbye"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ['Thank you, I am happy to help you 😎',
					'I hope I was helpful for you 🤗']
		reply = random.choice(messages)
		dispatcher.utter_message(text=reply)
		return []

class ActionAfterAffirm(Action):

    def name(self) -> Text:
        return "action_after_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = ["Yes, it is."]
        response = random.choice(messages)
        dispatcher.utter_message(text=response)
        return []

class AfterNo(Action):
	def name(self):
		return "action_after_deny"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Ok sir. Are there any ways in which we can help you?","Ok sir. Is there anything more you want to know?"]
		reply = random.choice(messages)
		dispatcher.utter_message(text=reply)
		return []

class RegisterCustomer(Action):
    def name(self):
        return "action_register_customer"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "Follow the steps to register a customer: -",
            "Go to the Screen 'mDabali Customer Registration - 12114'",
            "Click on New",
            "Enter the customer code/ customer name, mobile number and tag the concerned account to access the transaction. If you want to allow fund transfer to the respective account, then choose Yes. Then click on plus icon.",
            "After adding the details click on save and approve the customer registration.",
            "After approving the customer registration, go to the screen 'mDabali PIN Verification – 12435'",
            "Click on New",
            "Enter the customer code/ customer name and send the PIN",
            "After sending the PIN, enter the PIN no. sent to the concerned member and click on verify PIN",
            "After PIN verification, the customer is successfully registered in CBS"
        ]
        with open("images/register_customer.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())

        with open("images/register_customer_2.png","rb") as image_file:
            image_base64_2 = base64.b64encode(image_file.read())
        images = [str(image_base64),str(image_base64_2)]

        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class ChangeNumber(Action):
    def name(self):
        return "action_change_pin_mobile_number"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        entity_type = tracker.get_latest_entity_values('feature')
        entity_list=[]
        for item in entity_type:
            entity_list.append(item)
        print (f"The entities are: {entity_list}")
        try:
            if 'pin' in entity_list:
                steps = [
                    "Please follow the steps: -",
                    "Go to the Screen 'mDabali Reset PIN - 12436'",
                    "Click on New",
                    "Enter the customer code/ customer name and click on reset and send new PIN."
                ]
                with open("images/reset_pin.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                print("running the steps to change pin number")

            elif 'mobile' in entity_list:
                steps = [
                    "Please follow the steps: -",
                    "Go to the Screen 'mDabali Mobile Number Change – 11614'",
                    "Click on New",
                    "Enter the customer code/ customer name and enter the new mobile number",
                    "After changing the mobile number click on save and approve."
                ]
                with open("images/reset_mobile.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                print("running the steps to change mobile number")

            images = [str(image_base64)]        
            attachment = {
                "query_response": steps,
                "data":[{"image": images}],
                "type":"message_with_image",
                "data_fetch_status": "success"
            }
        except:
            messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
            reply = random.choice(messages)
            dispatcher.utter_message(text=reply)
            return [UserUtteranceReverted()]
        dispatcher.utter_message(attachment=attachment)
        return []

class TransactionMobile(Action):
    def name(self):
        return "action_transaction_from_mobile"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "Follow these steps: -",
            "Go to the Screen 'mDabali Mobile Facility Update - 11616'",
            "Click on New",
            "Enter the customer code / customer name",
            "After viewing the details, you can find out edit, delete and plus icons.",
            "To add the accounts, you need to add the account number and click the plus icon.",
            "If you want to remove the account number tagged, click on the delete icon.",
            "If you want to edit the details, then click on edit icon."
        ]
        
        with open("images/add_remove_account.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())

        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class CloseMobileBanking(Action):
    def name(self):
        return "action_close_mobile_banking_service"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "Follow the steps to close mobile banking: -",
            "Go to the Screen 'Mobile Banking Service Closure - 12282'",
            "Click on New",
            "Enter the customer code/ customer name and click on save & approve."
        ]
        
        with open("images/close_mobile_banking.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())

        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class SendBulkMessage(Action):
    def name(self):
        return "action_send_bulk_message"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "To send messages in bluk, follow the steps: -",
            "Go to the Screen 'SMS Send Maintenance - 12118'",
            "Choose the destination or if you have the number in excel sheet then import excel sheet",
            "Enter the text message and click on send.",
            "Please be noted that the number in destination is seen if the number has been saved in mobile number for alert in 'Customer Information Maintenance-01024'"
        ]

        with open("images/send_bulk_message.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())
        
        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []


class ComposeFeature(Action):
    def name(self):
        return "action_compose_features"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        entity_type = tracker.get_latest_entity_values('feature')
        entity_list=[]
        for item in entity_type:
            entity_list.append(item)
        print (f"The entites are: {entity_list}")
        try:
            if 'news' in entity_list or 'events' in entity_list:
                steps = [
                    "Follow the given steps: -",
                    "Go to the Screen 'News And Event Category Setup - 12462'",
                    "Click on New",
                    "Fill up Category Name, Category Name (Local) and Display Order",
                    "Click save and approve the setup",
                    "After that go to the screen 'News And Events Compose – 12256'",
                    "Click on New, then choose Category Type, Language and fill up publish days, News Title and Body. If you have any image related to news then browse the image.",
                    "Click on save & approve."
                ]
                with open("images/compose_news_events.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                with open("images/compose_news_events_2.png","rb") as image_file:
                    image_base64_2 = base64.b64encode(image_file.read())
                images = [str(image_base64),str(image_base64_2)]
                print ("running the steps to compose news or events")
            
            elif 'advertisement' in entity_list:
                steps = [
                    "Follow the steps: -",
                    "Go to the Screen 'Advertisement Category Setup - 12461'",
                    "Click on New",
                    "Fill up Category Name, Category Name (Local) and Display Order",
                    "Click save and approve the setup",
                    "After that go to the screen 'Advertisement Compose - 12463'",
                    "Click on New, then choose Category Type and fill up publish days. If you have any image related to advertisement, then browse the image or you can add the web address too.",
                    "Finally Click on save & approve."
                ]
                with open("images/compose_advertisement.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())            
                with open("images/compose_advertisement_2.png","rb") as image_file:
                    image_base64_2 = base64.b64encode(image_file.read())
                images = [str(image_base64), str(image_base64_2)]
                print ("running the steps to compose advertisement")
        

            attachment = {
                "query_response": steps,
                "data":[{"image": images}],
                "type":"message_with_image",
                "data_fetch_status": "success"
            }
        except:
            messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
            reply = random.choice(messages)
            dispatcher.utter_message(text=reply)
            return [UserUtteranceReverted()]
        dispatcher.utter_message(attachment=attachment)
        return []


class ComposeMessage(Action):
    def name(self):
        return "action_compose_message"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        entity_type = tracker.get_latest_entity_values('feature')
        entity_list = []
        for item in entity_type:
            entity_list.append(item)
        print (f"The entities are: {entity_list}")
        try:
            if 'login' in entity_list:
                steps = [
                    "Follow the given steps: -",
                    "Go to the Screen 'mDabali Login Message Compose - 12460'",
                    "Click on New",
                    "Write the message in both Nepali and English",
                    "If you have any image, then you can browse the image",
                    "After that click on save, then the message will be appearing while logging the application."
                ]
                with open("images/compose_login_message.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                images = [str(image_base64)]
                print ("running the steps to compose login message")

            elif 'mobile' in entity_list:
                steps = [
                    "Follow the  given procedures: -",
                    "Go to the Screen 'Mobile Message Compose - 12471'",
                    "Click on New, then fill up display till days, display order and message in both English and Nepali.",
                    "Then Click on Save and Approve."
                ]
                with open("images/compose_mobile_message.png","rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                images = [str(image_base64)]
                print ("running the steps to compose mobile message")
            
            attachment = {
                "query_response": steps,
                "data":[{"image": images}],
                "type":"message_with_image",
                "data_fetch_status": "success"
            }
        except:
            messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
            reply = random.choice(messages)
            dispatcher.utter_message(text=reply)
            return [UserUtteranceReverted()]
        dispatcher.utter_message(attachment=attachment)
        return []


class SettleCommission(Action):
    def name(self):
        return "action_settle_commission_infodevelopers"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "Follow the given procedure to settle the comission: -",
            "Go to the Screen 'Mobile Service Commission Settlement - 1225'",
            "Click on New",
            "Enter the amount send from the InfoDevelopers",
            "Choose Advance in Tax treatment Method and adjustment in Payment",
            "Write the description and verify the voucher i.e. \nCommission Receivable \t Cr. \nRecharge and Advance \t Dr. \nAdvance Tax \t Dr.",
            "After verification, click on save."
        ]
        with open("images/settle_commission.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())
        images = [str(image_base64)]

        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []


class ApprovePinRequest(Action):
    def name(self):
        return "action_approve_pin_request"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "Follow the steps to approve the pin request: -",
            "Go to the Screen 'Mobile PIN Reset Request Approval - 12474'",
            "If there is any request sent, then the request will be displayed the screen. You can view the customer details and approve the request if the details are correct.",
            "Please noted that the Approval of this PIN Reset request falls completely on your responsibility."
        ]
        with open("images/approve_pin_request.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())

        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []


class PublishDocument(Action):
    def name(self):
        return "action_publish_document"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "To publish document, follow the procedures: -",
            "Go to the Screen 'Mobile Document Publish - 12485'",
            "Click on New and fill up the Document Title, Document Title (Local) and Publish till days. If you want to allow download then tick on the box and choose the pdf document or web URL to publish the document.",
            "Then Click on Save and Approve. The document can be viewed by the mobile banking users in view document of mobile banking."
        ]
        with open("images/publish_document.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())
        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []


class LimitBankTransfer(Action):
    def name(self):
        return "action_limit_inter_bank_transfer"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "The process of limit the inter bank transfer are: -",
            "Go to the Screen 'DFS Service Scope Based Transaction Limit Setup - 12479'",
            "Click on New, Select the service scope, and fill up per transaction minimum amount, maximum amount, daily, weekly and monthly transaction amount & count.",
            "Then Click on Save and Approve."
        ]
        with open("images/limit_bank_transfer.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())
        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []


class VerifyComissionAmount(Action):
    def name(self):
        return "action_verify_commission_amount"

    def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        steps = [
            "The process to verify the commission amount are: -",
            "Go to the Screen 'Commission Balance Report-12272'",
            "Filter the date",
            "Choose the actual date from report option and print the data",
            "Then you can verify by deducting the opening balance from closing balance."
        ]
        with open("images/verify_commission.png","rb") as image_file:
            image_base64 = base64.b64encode(image_file.read())
        images = [str(image_base64)]
        attachment = {
            "query_response": steps,
            "data":[{"image": images}],
            "type":"message_with_image",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []