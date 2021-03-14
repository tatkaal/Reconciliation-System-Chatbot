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
from langdetect import detect

class About(Action):
	def name(self):
		return "action_about"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
			messages = ['म च्याटबट हुँ। मैले तपाईंलाई मदत गर्न यहाँ छु।','यस अनुप्रयोग मार्फत मार्गदर्शन गर्न म तपाईंको भर्चुअल सहायक हुँ।']
		else:
			messages = ['I am a chatbot. I am here to help you.',
						'I am your virtual assistant to guide you through this app.']
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class OutOfScope(Action):
	def name(self):
		return "action_out_of_scope"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ["माफ गर्नुहोस्, मैले तपाईंलाई बुझ्न सक्दिन के तपाई यसलाई फेरि दोहोर्याउन सक्नुहुन्छ?", "म यसलाई बुझ्न सक्दिन, कृपया तपाईले यसलाई दोहोर्याउनुहुन्छ?", "मैले यो एकदम अस्पष्ट पाए। के तपाई मलाई फेरि केहि स्पष्ट बताउन सक्नुहुन्छ? 🧐"]
		else:
			messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
					"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return [UserUtteranceReverted()]

class ActionDefaultFallback(Action):
	def name(self):
		return "action_handle_fallback"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ["माफ गर्नुहोस्, म तपाईंलाई बुझ्न सक्दिन के तपाई यसलाई फेरि दोहोर्याउन सक्नुहुन्छ?", "म यसलाई बुझ्न सक्दिन, कृपया तपाईले यसलाई दोहोर्याउनुहुन्छ?", "मैले यो एकदम अस्पष्ट पाए। के तपाई मलाई फेरि केहि स्पष्ट बताउन सक्नुहुन्छ? 🧐"]
		else:
			messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
					"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return [UserUtteranceReverted()]

class Greeting(Action):
	def name(self):
		return "action_greeting"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ["नमस्ते। तपाईलाई यहाँ पाउँदा खुसी लाग्यो 🤗 म तपाईलाई कसरी मद्दत गर्न सक्छु।","नमस्कार 👋😃 म कसरी मद्दत गर्न सक्छु।"]
		else:
			messages = ["Hi there. It's such a pleasure to have you here 🤗. How can I help you.",
						"Hello 👋😃 How can I assist you."]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class AfterGreeting(Action):
	def name(self):
		return "action_after_greet"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ["म ठिक छु। 🤟😎🤟", "पहिलेभन्दा राम्रो"]
		else:
			messages = ["I am fine. 🤟😎🤟",
						"Better than ever 😎"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class Goodbye(Action):
	def name(self):
		return "action_goodbye"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ['धन्यबाद, म तपाईंलाई सहयोग गर्न खुसी छु 😎', 'मलाई आशा छ कि म तपाईंको लागि सहयोगी थिए 🤗']
		else:
			messages = ['Thank you, I am happy to help you 😎',
						'I hope I was helpful for you 🤗']
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ActionAfterAffirm(Action):
	def name(self):
		return "action_after_affirm"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ['तपाईं ठिक हुनुहुन्छ']
		else:
			messages = ["Yes, it is."]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class AfterNo(Action):
	def name(self):
		return "action_after_deny"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		latest_msg = tracker.latest_message['text']
		if(detect(latest_msg) in ['hi' ,'ne']):
				messages = ["ठीक छ सर। के त्यहाँ कुनै उपायहरू छन् जुन हामी तपाईंलाई मद्दत गर्न सक्दछौं?", "ठीक छ सर। त्यहाँ केहि अरू पनि तपाईंले जान्न चाहानुहुन्छ?"]
		else:
			messages = ["Ok sir. Are there any ways in which we can help you?","Ok sir. Is there anything more you want to know?"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class IntroductionQA(Action):
	def name(self):
		return "action_what_is"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		entity_type = tracker.get_latest_entity_values('attr')
		entity_list=[]
		for item in entity_type:
			entity_list.append(item)
		print (f"The entities are: {entity_list}")
		try:
			if 'Reconciliation system' in entity_list:
				latest_msg = tracker.latest_message['text']
				if(detect(latest_msg) in ['hi' ,'ne']):
						messages = ''
				else:
					message = "Reconciliation is an accounting process that compares two or more sets of records to identify whether those figures are correct and in agreement or not. It is particularly useful for explaining the difference between two or more sets of financial records or account balances. To facilitate the comparison of such transactions basically done daily and suggest the matched and unmatched transactions, the Comprehensive Reconciliation System (CRS) has been introduced."

			elif 'ATM Transaction Reconciliation' in entity_list:
				message = "ATM reconciliation is required to know the difference between ATM balance as per book and as per actual. Moreover to find the reasons of this difference and supply new cash in ATM for smooth customers' transactions.It also enables real-time representation of transactions in a bank’s balance sheets for audits and faster fraud detection and refund in case of technical machine problems."
			
			elif 'Nostro Account' in entity_list:
				message = "A nostro account refers to an account that a bank holds in another bank (can be either local or foreign bank)"
				
			elif 'Nostro Reconciliation' in entity_list:
				message = "Nostro Reconciliation deals with the reconciliation of the entries of an external statement with that of the corresponding entries in the Nostro account. "
			
			attachment = {
					"query_response": message,
					"data":[],
					"type":"normal_message",
					"data_fetch_status": "success"
				}

		except:
			messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]
		dispatcher.utter_message(attachment=attachment)
		return []

class DiffQA(Action):
	def name(self):
		return "action_differences_questions"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		entity_type = tracker.get_latest_entity_values('diff')
		entity_list=[]
		for item in entity_type:
			entity_list.append(item)
		print (f"The entities are: {entity_list}")
		try:
			if 'Onus transaction and Offus transaction' in entity_list:
				message = "A transaction carried out at ATM of card issuing bank is called Onus transaction whereas a transaction carried out at ATM of bank which is different from card issuing bank is called Offus transaction."

			attachment = {
				"query_response": message,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
		except:
			messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]
		dispatcher.utter_message(attachment=attachment)
		return []

class SystemFeatures(Action):
	def name(self):
		return "action_system_features"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		reply = "Admin have access to the whole system"
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class SetupModule(Action):
	def name(self):
		return "action_setup_module"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		entity_type = tracker.get_latest_entity_values('setup')
		entity_list=[]
		for item in entity_type:
			entity_list.append(item)
		print (f"The entities are: {entity_list}")
		try:
			if 'Transaction data source' in entity_list:
				message = "User can setup transaction data sources like CBS, EJ, Visa,etc. "
			elif 'Reconciliation category' in entity_list:
				message = "User can setup Reconciliation category such as ATM acquiring Onus, ATM acquiring Offus Visa, etc"
			attachment = {
				"query_response": message,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
		except:
			messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]
		dispatcher.utter_message(attachment=attachment)
		return []

class ReconciliationDataSource(Action):
	def name(self):
		return "action_reconciliation_data_source"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User can setup transaction data source required for each reconciiliation category through this setup screen"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ReconciliationFieldComparision(Action):
	def name(self):
		return "action_reconciliation_field_comparision"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User can configure fields/column of  different data sources that are required to be compared during reconciliation process such as reference number, transaction amount, etc. "
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ReconciliationPayableSetup(Action):
	def name(self):
		return "action_reconciliation_payable_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "This setup screen is required for Visa receivable/payable reconciliation. User need to setup this screen to import Visa issuing and Visa acquiring files. "
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class BankSetup(Action):
	def name(self):
		return "action_bank_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Bank setup is required for Nostro Reconciliation."
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class RBBBranchSetup(Action):
	def name(self):
		return "action_RBB_branch_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Different branch of RBB is setup."
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class Terminal_type_setup(Action):
	def name(self):
		return "action_Terminal_type_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Transaction is done either thourgh POS or ATM  is setup in this screen"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class vendor_setup(Action):
	def name(self):
		return "action_vendor_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Vendor like Diebold or NCR can be setup"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class merchant_setup(Action):
	def name(self):
		return "action_merchant_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Merchant setup is required for POS terminal type transaction"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class terminal_setup(Action):
	def name(self):
		return "action_terminal_setup"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Terminal information for different RBB branch is setup"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class data_source_location(Action):
	def name(self):
		return "action_data_source_location"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User can configure path location of different data sources files/folder"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class dynamic_file_field_select(Action):
	def name(self):
		return "action_dynamic_file_field_select"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User will map the fields/column name of different data sources files with data base table that shall be displayed during import."
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class import_module(Action):
	def name(self):
		return "action_import_module"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User extract data files or folder from different transaction data sources such as CBS, EJ, Switch,VISA,etc from the designated ftp path and upload in the reconciliation system server"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class process_import_file(Action):
	def name(self):
		return "action_process_import_file"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "1. At first go to the transaction data source file location screen and configure path for various data sources <br><br>2.Now go to import screen of each data source and click import button"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []



class reconciliation_module(Action):
	def name(self):
		return "action_reconciliation_module"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User carries out reconciliation process  of various reconciliation category such as ATM reconciliation, Nostro reconciliation, etc"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class report_module(Action):
	def name(self):
		return "action_report_module"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "User can view and download different types of report in excel,csv format generated after reconciliation."
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class usermanagement_module(Action):
	def name(self):
		return "action_usermanagement_module"

	def run(self, dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
		message = "Admin user can create and assign new user with role, module setup and privilege setup"
		attachment = {
			"query_response": message,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []
