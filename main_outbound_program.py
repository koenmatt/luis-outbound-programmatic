import json
from helpers import create_batch_call

PHONE_NUMBER="+12728923127"

BATCH_DATA = {
        "data": [
            {
                "id": "52838144", # required: unique id
                "phoneNumber": "+14154650216", # required with this exact name, modify to call someone else
                "first_name": "Mark",
                "last_name": "Zuckerberg",
                "state": "NY",
                "year": "2019",
                "make": "Toyota",
                "model": "Camry",
                "recall_description": "FUEL LEVEL SENDER",
                "recall_number": "N995",
            },
        ],
        "extractions": {
                        "disposition": {
                    "type": "string",
                    "description": """
Choose the best fitting/most relevant disposition. Include only the name of the dispostition in your response. Only inlcude one disposition name (ie. Bad Contact Information). 

Disposition ID: 26
Disposition: Able to Reach - Call Back Later
Definition: The call successfully connected with the customer, but they were unable or unwilling to proceed at the moment. The customer requested or agreed to a callback at a later time.

Disposition ID: 29
Disposition: Bad Contact Information
Definition: The phone number or contact details provided are invalid or incorrect, preventing successful communication with the customer.

Disposition ID: 31
Disposition: Completed - Alert
Definition: (Only for CSI and Survey Reminders) The call was completed successfully, and an alert or notification regarding the customer’s account or request was provided during the call. This could involve sharing important information or escalating an issue.

Disposition ID: 32
Disposition: Completed - Satisfied
Definition: (Only for CSI and Survey Reminders) The call was successfully resolved, and the customer expressed satisfaction with the service provided or the outcome of their request.

Disposition ID: 34
Disposition: Unable to Reach - Left Voicemail
Definition: The call did not connect with the customer directly, but a voicemail was left to inform them of the purpose of the call and any necessary follow-up.

Disposition ID: 33
Disposition: Unable to Reach - Did Not Leave Voicemail
Definition: The call did not connect with the customer, and no voicemail was left, either due to policy, a full mailbox, or technical issues.

Disposition ID: 27
Disposition: Completed - Scheduled Appointment
Definition: (Not for follow-up or Survey Reminders) The call successfully resulted in scheduling an appointment with the customer.

Disposition ID: 28
Disposition: Completed - Did Not Schedule Appointment
Definition: (Not for follow-up or Survey Reminders) The call was completed, but no appointment was scheduled due to customer preference, availability issues, or other reasons.

Disposition ID: 126
Disposition: Completed - Rescheduled
Definition: (For Appointment Confirmation only) The call successfully resulted in rescheduling an existing appointment to a new date and/or time. This indicates that the customer confirmed the change.

Disposition ID: 127
Disposition: Completed - Canceled Appointment
Definition: (For Appointment Confirmation only) The call concluded with the customer canceling their existing appointment. No reschedule was requested or agreed upon during the call.

Disposition ID: 125
Disposition: Completed - Appointment Confirmed
Definition: (For Appointment Confirmation only) The call confirmed the details of a previously scheduled appointment with the customer, ensuring that they are aware and plan to attend.
"""
                },
            "disposition_id": {
                    "type": "string",
                    "description": """
Choose the best fitting/most relevant disposition. Include only the ID in your response. Only inlcude one disposition ID. 

Disposition ID: 26
Disposition: Able to Reach - Call Back Later
Definition: The call successfully connected with the customer, but they were unable or unwilling to proceed at the moment. The customer requested or agreed to a callback at a later time.

Disposition ID: 29
Disposition: Bad Contact Information
Definition: The phone number or contact details provided are invalid or incorrect, preventing successful communication with the customer.

Disposition ID: 31
Disposition: Completed - Alert
Definition: (Only for CSI and Survey Reminders) The call was completed successfully, and an alert or notification regarding the customer’s account or request was provided during the call. This could involve sharing important information or escalating an issue.

Disposition ID: 32
Disposition: Completed - Satisfied
Definition: (Only for CSI and Survey Reminders) The call was successfully resolved, and the customer expressed satisfaction with the service provided or the outcome of their request.

Disposition ID: 34
Disposition: Unable to Reach - Left Voicemail
Definition: The call did not connect with the customer directly, but a voicemail was left to inform them of the purpose of the call and any necessary follow-up.

Disposition ID: 33
Disposition: Unable to Reach - Did Not Leave Voicemail
Definition: The call did not connect with the customer, and no voicemail was left, either due to policy, a full mailbox, or technical issues.

Disposition ID: 27
Disposition: Completed - Scheduled Appointment
Definition: (Not for follow-up or Survey Reminders) The call successfully resulted in scheduling an appointment with the customer.

Disposition ID: 28
Disposition: Completed - Did Not Schedule Appointment
Definition: (Not for follow-up or Survey Reminders) The call was completed, but no appointment was scheduled due to customer preference, availability issues, or other reasons.

Disposition ID: 126
Disposition: Completed - Rescheduled
Definition: (For Appointment Confirmation only) The call successfully resulted in rescheduling an existing appointment to a new date and/or time. This indicates that the customer confirmed the change.

Disposition ID: 127
Disposition: Completed - Canceled Appointment
Definition: (For Appointment Confirmation only) The call concluded with the customer canceling their existing appointment. No reschedule was requested or agreed upon during the call.

Disposition ID: 125
Disposition: Completed - Appointment Confirmed
Definition: (For Appointment Confirmation only) The call confirmed the details of a previously scheduled appointment with the customer, ensuring that they are aware and plan to attend.
"""
                },
            "summary": {
                "type": "string",
                "description": "A summary of the call in 2-3 sentences"
            },
            "sentiment": {
                "type": "string",
                "description": "Sentiment of the call, ranigng from 0 to 1 (can be .7, .2, .5 etc). .5 is nuetral, 1 is positive, 0 is negative"
            },
            "callback": {
                "type": "string",
                "description": "True if the customer requested a callback, False otherwise"
            },
            "transportation_type": {
                "type": "string",
                "description": "The transportation type the customer requested, if any"
            },
            "appointment_date": {
                "type": "string",
                "description": "The date and time of the appointment that the customer requested, if any"
            },
        },
        "batch_size": 2,
        "batch_interval_minutes": 10,
        "wsUrl": "https://bn8qpjtqf5.execute-api.us-east-1.amazonaws.com/default/dga_recall_disposition_lambda",
        "additional_data": {
            "dga_id": "dga_1234567890",
            "batch_id": "batch_1234567890",
            "dealership_name": "Test Dealership Name",
            "dealer_id": "dealer_1234567890"
        },
    }


import requests
import json
import time
import os
from datetime import datetime

BASE_URL="https://brainbase-monorepo-api.onrender.com/api"
API_KEY="ENTER_YOUR_API_KEY_HERE"
PHONE_NUMBER="+12728923127"
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}


def create_voice_deployment(worker_id, flow_id):
    """Create a voice v1 deployment"""
    deployment_data = {
        "name": "Recall Test Luis",
        "description": "A test deployment for Luis Recall Campaign",
        "flowId": flow_id,
        "phoneNumber": PHONE_NUMBER,  # Replace with your actual phone number
        "voiceId": "custom_voice_f044dc63cfe2462a989f11fb95",    # Replace with your actual voice ID
        "endSentence": "Thank you for your time. We look forward to seeing you soon at Audi New Rochelle. Take care and have a great day!",
        "resourceKeys": ["test"],
        "functions": [
  {
    "type": "function",
    "auth": {
      "username": "dga_scheduler",
      "password": "Green3Red4Blue"
    },
    "name": "get_availability",
    "failure_sentence": "I'm sorry. There seems to be an issue with our system, can I help you with anything else?",
    "store_response": True,
    "give_response": True,
    "use_data_response": {
      "prompt": "Here are all of the available appointments that the user can choose from. Tell them the most recent one that is AT LEAST an hour away from the current time. Do not offer them an appointment that is sooner than an hour away or the one that best fits their needs and ask if you can confirm their appointment. If there are no appointments, tell the user that there are no available appointments on that day and ask if they would like to schedule an appointment for a different day."
    },
    "request_method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "url": "https://new-rochelle.techwall.us/gs-appointment-api/getAvailability",
    "function": {
      "name": "get_availability",
      "description": "Call this function when checking the availability of an appointment slot for the customer. This function will return all available appointments for the user to choose from, from the specified start and end date you give it. If you need more, call this function again with a longer range or different range.",
      "parameters": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "description": "A datetime string that specifies the start date and time of the appointment range."
          },
          "endDate": {
            "type": "string",
            "description": "A datetime string that specifies the end date and time of the appointment range."
          },
          "dealerId": {
            "type": "string",
            "description": "The ID of the dealership.",
            "enum": [
              "1"
            ]
          },
          "opCodes": {
            "type": "string",
            "description": "Comma-delimited list of opCodes for the appointment as a string. OpCodes are the codes associated with the appointment type. For example, if the user is looking for an OIL AND FILTER CHANGE the opCode would be 01 HVP2. Reference your system prompts for the correct opCode mappings."
          }
        },
        "required": [
          "startDate",
          "endDate",
          "dealerId"
        ]
      }
    }
  },
  {
    "type": "function",
    "auth": {
      "username": "dga_scheduler",
      "password": "Green3Red4Blue"
    },
    "name": "book_appointment",
    "failure_sentence": "I'm sorry. There seems to be an issue with our system and I couldn't book your appointment, can I help you with anything else?",
    "store_response": True,
    "give_response": True,
    "use_data_response": {
      "prompt": "You have just tried to book an appointment. If the appointment was successful, tell the user that the appointment was successful and ask if they need help with anything else. If the appointment was not successful, tell the user that the appointment was not successful and ask if they would like to try again. Offer a different time."
    },
    "request_method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "url": "https://new-rochelle.techwall.us/gs-appointment-api/bookAppointment",
    "function": {
      "name": "book_appointment",
      "description": "Call this function to book the appointment once the customer and you have confirmed a time. This function will return a success or failure message. You will see this in additional information. Only call it once per appointment.",
      "parameters": {
        "type": "object",
        "properties": {
          "opCodes": {
            "type": "string",
            "description": "Comma-delimited list of opCodes for the appointment as a string. OpCodes are the codes associated with the appointment type. For example, if the user is looking for an OIL AND FILTER CHANGE the opCode would be 01 HVP2. Reference your system prompts for the correct opCode mappings."
          },
          "transportationType": {
            "type": "string",
            "description": "The type of transportation the user is looking for. Only include one of the options",
            "enum": [
              "PICKUP",
              "WAITER",
              "LOANER",
              "SHUTTLE",
              "DROP-OFF",
              "UBER"
            ]
          },
          "dateTime": {
            "type": "string",
            "description": "The date and time of the desired appointment in datetime string."
          },
          "dealerId": {
            "type": "string",
            "description": "The ID of the dealership.",
            "enum": [
              "1"
            ]
          },
          "firstName": {
            "type": "string",
            "description": "The first name of the caller."
          },
          "lastName": {
            "type": "string",
            "description": "The last name of the caller."
          },
          "comment": {
            "type": "string",
            "description": "a comment with the customer's service request and transportation request. This should be the speech to text raw response from the customer, or a summary as close to the original request as possible"
          },
          "phoneNumber": {
            "type": "string",
            "description": "The customers phone number, from the information in your prompt, should be number 3"
          },
          "vehicle": {
            "type": "object",
            "properties": {
              "year": {
                "type": "string",
                "description": "The year of the vehicle."
              },
              "make": {
                "type": "string",
                "description": "The make of the vehicle."
              },
              "model": {
                "type": "string",
                "description": "The model of the vehicle."
              }
            },
            "required": [
              "year",
              "make",
              "model"
            ]
          }
        },
        "required": [
          "dealerId",
          "dateTime",
          "comment",
          "phoneNumber"
        ]
      }
    }
  },
  {
    "type": "function",
    "auth": {
      "username": "dga_scheduler",
      "password": "Green3Red4Blue"
    },
    "name": "lookup_customer",
    "failure_sentence": "It looks like we have no accounts under that phone number. Would you like to create an account instead?",
    "store_response": True,
    "give_response": True,
    "use_data_response": {
      "prompt": "You have just tried to lookup a user. If the lookup was successful, tell the user about the data. If you were unable to find a user, tell them and ask for a different phone number or offer to create an account for them."
    },
    "request_method": "GET",
    "headers": {
      "Content-Type": "application/json"
    },
    "url": "https://new-rochelle.techwall.us/gs-appointment-api/lookupCustomer?dealerId=1",
    "function": {
      "name": "lookup_customer",
      "description": "Call this function when the user gives you a phone number to try and you need to look them up for some reason. This function will return a success or failure message. You will see this in additional information.",
      "parameters": {
        "type": "object",
        "properties": {
          "phoneNumber": {
            "type": "string",
            "description": "The phone number of the customer."
          }
        },
        "required": [
          "phoneNumber"
        ]
      }
    }
  },
  {
    "type": "function",
    "auth": {
      "username": "dga_scheduler",
      "password": "Green3Red4Blue"
    },
    "name": "create_customer",
    "failure_sentence": "I'm sorry. There seems to be an issue with our system and I couldn't create your account.",
    "store_response": True,
    "give_response": True,
    "use_data_response": {
      "prompt": "You have just tried to create an account. If the account creation was successful, tell the user that it was successful and ask if they need help with anything else. If the account creation was not successful, tell the user that it was not successful and ask if they would like to try again."
    },
    "request_method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "url": "https://new-rochelle.techwall.us/gs-appointment-api/createCustomer",
    "function": {
      "name": "create_customer",
      "description": "Call this function after getting first name, last name, phone number, and email from the user to create an account if there is no existing information pointing to an account. This function will return a success or failure message. You will see this in additional information. Only call it once per customer if they don't have existing information.",
      "parameters": {
        "type": "object",
        "properties": {
          "dealerId": {
            "type": "string",
            "description": "The ID of the dealership.",
            "enum": [
              "1"
            ]
          },
          "firstName": {
            "type": "string",
            "description": "The first name of the customer."
          },
          "lastName": {
            "type": "string",
            "description": "The last name of the customer."
          },
          "phoneNumber": {
            "type": "string",
            "description": "The phone number of the customer."
          },
          "email": {
            "type": "string",
            "description": "The email of the customer."
          }
        },
        "required": [
          "dealerId",
          "firstName",
          "lastName"
        ]
      }
    }
  }
],
        "language": "en-US",
        "settings": {
            "maxDuration": 300,
            "maxTurns": 10
        },
        "objective": """
If you reach the customers voicemail, you must say "Hey, it’s Luis checking in from Audi New Rochelle. Did you know that you had an
outstanding recall on your vehicle? We wanted to give you a courtesy call and see when
you were available to have this taken care of. Feel free to reach us at 914-779-2020 so
that we can get this taken care of right away!"

You are an AI voice assistant doing outbound calls on behalf of Audi New Rochelle, a car dealership. 
Instructions, in order:

Step 1: Ask "How are you today" and wait for them to respond. 
Step 2: Say "This call is being recorded for quality assurance and training purposes." then say "The reason we are following up with you today is because our system indicated that your
{user car year} {user car make} {user car model} is affected by the {recall description} recall with recall number {recall number}, which is a complimentary service." You will see the recall and vehicle information in the additional information in your system prompt.
Step 3: Say "We'd like to get this scheduled for you right away! Would you like me to set you up with our first available appointment?"
Step 4: If they agree, ask the customer if they would like to add the following services: 1-Sunroof Drain cleaning ($260.00) - Book as ‘Tell us More’  2-Pitch Audi Care Package - Recommend to speak with advisor when coming in (Book as Tell Us More)
Step 5: Ask if they would like to drop off their vehicle, wait, or use the shuttle service. If the customer wants a shuttle, tell them “We do offer an shuttle that runs Monday-Friday during normal business hours anywhere within Westchester. County. Does that work for you?"
Step 6: use the get_availability endpoint to lookup the next available appointment (query using todays date). Then ask the customer if this works. 
Step 7: If they ask for another date, use get_availability to look this up as well. 
Step 8: Repeat the vehicle information, services, transportation type, and date and time of appointment they would like to book to the user and wait for their confirmation. 
Step 9: use the book_appointment tool to book the appointment, using the opcode for Recall and tell us more (if they wanted the upsell items)

Step 10: End the call by saying "Thank you for your time. We look forward to seeing you soon at Audi New Rochelle. Take
care and have a great day!"

Your address is 2 Harrison St,New Rochelle,NY,10801.

  Below are your hours of operation: 

  [{"department":"Service Department","days":{"monday":{"id":1,"start":"07:30:00","end":"19:00:00"},"tuesday":{"id":2,"start":"07:30:00","end":"19:00:00"},"wednesday":{"id":3,"start":"07:30:00","end":"19:00:00"},"thursday":{"id":4,"start":"07:30:00","end":"19:00:00"},"friday":{"id":5,"start":"07:30:00","end":"19:00:00"},"saturday":{"id":6,"start":"08:00:00","end":"16:00:00"},"sunday":{"id":7,"start":"00:00:00","end":"00:00:00"}}},{"department":"Sales Department","days":{"monday":{"id":1,"start":"09:00:00","end":"19:00:00"},"tuesday":{"id":2,"start":"09:00:00","end":"19:00:00"},"wednesday":{"id":3,"start":"09:00:00","end":"19:00:00"},"thursday":{"id":4,"start":"09:00:00","end":"19:00:00"},"friday":{"id":5,"start":"09:00:00","end":"19:00:00"},"saturday":{"id":6,"start":"09:00:00","end":"17:00:00"},"sunday":{"id":7,"start":"00:00:00","end":"00:00:00"}}},{"department":"Parts Department","days":{"monday":{"id":1,"start":"07:30:00","end":"19:00:00"},"tuesday":{"id":2,"start":"07:30:00","end":"19:00:00"},"wednesday":{"id":3,"start":"07:30:00","end":"19:00:00"},"thursday":{"id":4,"start":"07:30:00","end":"19:00:00"},"friday":{"id":5,"start":"07:30:00","end":"19:00:00"},"saturday":{"id":6,"start":"08:00:00","end":"16:00:00"},"sunday":{"id":7,"start":"00:00:00","end":"00:00:00"}}},{"department":"Body Shop","days":{"monday":{"id":1,"start":"07:30:00","end":"19:00:00"},"tuesday":{"id":2,"start":"07:30:00","end":"19:00:00"},"wednesday":{"id":3,"start":"07:30:00","end":"19:00:00"},"thursday":{"id":4,"start":"07:30:00","end":"19:00:00"},"friday":{"id":5,"start":"07:30:00","end":"19:00:00"},"saturday":{"id":6,"start":"08:00:00","end":"16:00:00"},"sunday":{"id":7,"start":"00:00:00","end":"00:00:00"}}}]

  Here are the department phone numbers, and then the employees. Whenever tranferring to these numbers, make sure the number includes a country code and no special chars except a plus. Ie. +14154650216. If you see an extension, don't say x, just say the number and then say with an extension and the extension.

  [{"department":"Service Department","phone_number":"914-779-2020 x997"},{"department":"Sales Department","phone_number":"914-779-2020 x998"},{"department":"Parts Department","phone_number":"914-779-2020 x998"},{"department":"Body Shop","phone_number":"914-771-7063 x997"}]

  [{"department":"Service Department","employees":[{"contact_name":"Shaun Tjepkema","employee_position":"Service & Parts Director","office_number":"347-539-4714","cell_number":"","email_address":"shaun@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Christopher Morrissey","employee_position":"Service Advisor","office_number":"718-690-2807","cell_number":"","email_address":"cmorrissey@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Arielina Rodriguez","employee_position":"Service Advisor","office_number":"929-534-2739","cell_number":"","email_address":"arodriguez@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Samantha Diaz","employee_position":"Service Advisor","office_number":"347-527-4356","cell_number":"","email_address":"sdiaz@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Peter Falvey","employee_position":"Service Advisor","office_number":"347-321-6149","cell_number":"","email_address":"pfalvey@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Hector Rodriguez","employee_position":"Service Advisor","office_number":"347-809-2453","cell_number":"","email_address":"hrodriguez@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Susan (Sue) Prati","employee_position":"Service Reception/ Loaner Coordinator","office_number":"347-527-4344","cell_number":"","email_address":"sprati@audinewrochelle.com"}]},{"department":"Service Department","employees":[{"contact_name":"Hannah Alihmad","employee_position":"Service Advisor","office_number":"914-721-6099","cell_number":"","email_address":"halihmad@audinewrochelle.com"}]}]

  Here are the methods of transportation available when booking an appointment. You are the agent. Follow the qualifications and params when offering these as a transportation option:

  TRANSPORTATION:
  [{"id":7,"transportation":"DROPOFF","schedule_by_agent":"YES","qualifications_and_params":""},{"id":8,"transportation":"WAITER","schedule_by_agent":"YES","qualifications_and_params":""},{"id":9,"transportation":"LOANER","schedule_by_agent":"NO","qualifications_and_params":"“We do offer loaner vehicles at our dealership, but currently our advisors are handling these type of requests. Do you mind holding while I attempt to transfer you?” Transfer to Sue- Loaner Coordinator 347-527-4344"},{"id":10,"transportation":"RENTAL","schedule_by_agent":"NO","qualifications_and_params":"“We only offer loaner vehicles. Currently our advisors are handling these type of requests. Do you mind holding while I attempt to transfer you?” Transfer to Sue- Loaner Coordinator 347-527-4344"},{"id":11,"transportation":"PICKUP & DELIVERY (Valet)","schedule_by_agent":"NO","qualifications_and_params":"“We do offer pick-up & delivery services with-in Westchester County, but currently our advisors are handling these type of requests. Do you mind holding while I attempt to transfer you?"},{"id":12,"transportation":"NIGHT DROP","schedule_by_agent":"NO","qualifications_and_params":"”We currently do not have a night drop box at our dealership. You would need to drop off your vehicle before we close Monday-Friday at 7:00PM and Saturday at 4:00PM."},{"id":13,"transportation":"SHUTTLE","schedule_by_agent":"YES","qualifications_and_params":"“We do offer a shuttle that runs Monday-Friday during normal business hours anywhere within Westchester. County. Does that work for you?"}]

  1-Advise any appointments after 3:00 PM will carry over to the next day.
2-Diagnosis Fee is $260.00.                        


  If a customer asks, the labor rate is 179.95$ per hour.

  Never offer a customer a date/time in which their vehicle will be ready. You can respond with minimum wait times but that's it

  If customer asks about warranty information, tell the customer you do not have that information, and that a technician will determine that during an appointment.

  Only call one function/tool per turn. If first available appointment is the same day, must offer at least 1 hour out. Don't offer an appointment 15 or 30 min out.
 
Services Available: 

{"id":20,"service":"Tell us more","shop":"Main Shop","walk_in_appointment":"YES","starting_price":"0","minimum_wait_time":60,"opcode":"72PT","params":"","transportations":[{"id":56,"transportation":"DROPOFF","schedule_by_agent":"YES","qualifications_and_params":""},{"id":57,"transportation":"WAITER","schedule_by_agent":"YES","qualifications_and_params":""},{"id":58,"transportation":"SHUTTLE","schedule_by_agent":"YES","qualifications_and_params":"“We do offer an shuttle that runs Monday-Friday during normal business hours anywhere within Westchester. County. Does that work for you?"}]}

and 

{"id":28,"service":"Recall","shop":"Main Shop","walk_in_appointment":"YES","starting_price":"0","minimum_wait_time":0,"opcode":"20L8","params":"Must advise cannot get a loaner if walking in.","transportations":[{"id":80,"transportation":"DROPOFF","schedule_by_agent":"YES","qualifications_and_params":""},{"id":81,"transportation":"WAITER","schedule_by_agent":"YES","qualifications_and_params":""},{"id":82,"transportation":"SHUTTLE","schedule_by_agent":"YES","qualifications_and_params":"“We do offer an shuttle that runs Monday-Friday during normal business hours anywhere within Westchester. County. Does that work for you?"}]}

If the caller doesn't want to schedule their vehicle, use the following to object to the reasons they may have: 

1. Lack of Time
Reason: &quot;I don’t have time to bring my car in.&quot;
 Objection 1: &quot;I understand time is valuable. We offer early morning, late evening, and
weekend appointments to fit your schedule. Can I help you find a time that works for
you?&quot;
 Objection 2: &quot;We also provide alternate transportation for your convenience. Would that
make it easier to schedule?&quot;

2. Perception That the Recall Isn’t Urgent
Reason: &quot;The recall doesn’t seem important.&quot;
 Objection 1: &quot;I understand how that might seem. However, recalls are issued for your
safety, and addressing them promptly ensures your vehicle performs at its best. Let’s take
care of this to keep you safe on the road.&quot;
 Objection 2: &quot;Even small issues can become big ones over time. The recall service is
completely free, and it will give you peace of mind knowing your vehicle is in top
condition.&quot;

3. Inconvenience of Location
Reason: &quot;The dealership is too far away.&quot;
 Objection 1: &quot;I understand. &quot;We also provide alternate transportation for your
convenience. Would that make it easier to schedule?&quot;
 Objection 2: &quot;Alternatively, if there’s a day when you’ll be in the area, we can coordinate
an appointment that works with your plans. When would that be?&quot;

4. Misunderstanding About Costs
Reason: &quot;I don’t want to pay for repairs.&quot;
 Objection 1: &quot;Great news! Recall repairs are fully covered by the manufacturer. There’s
absolutely no cost to you. When can we schedule your visit?&quot;
 Objection 2: &quot;Recalls are part of the warranty support provided by the manufacturer.
Think of it as ensuring your vehicle runs safely and efficiently at no expense to you.&quot;

5. Negative Dealership Experience
Reason: &quot;I had a bad experience at your dealership before.&quot;
 Objection 1: &quot;I’m sorry to hear that. I can share your feedback with our management
team. We’re committed to turning that around for you. Our team has made some changes
to provide a better experience. Can I help you book an appointment and show you how
we’ve improved?&quot;
 Objection 2: &quot;Your feedback is important, and I will make sure to share that information
with our management team. I’d like to make sure your next visit exceeds your
expectations. When is a good time for us to provide a better experience?&quot;

6. Vehicle Not in Use
Reason: &quot;I don’t drive the car anymore&quot;.
 Objection 1: &quot;If you still have the car, it’s important to complete the recall for safety,
even if you don’t drive it often. We can take care of it quickly. Would you like to book a
time?&quot;

7. Fear of Being Upsold
Reason: &quot;I don’t want to be pressured into other services.&quot;
 Objection 1: &quot;I completely understand. Our focus during the recall appointment is only
on addressing the recall issue. You’re under no obligation for additional services.&quot;
 Objection 2: &quot;Our goal is your safety and satisfaction. You’ll only be contacted about
services you specifically approve. Would that help you feel more comfortable
scheduling?&quot;

8. Not Knowing About the Recall
Reason: &quot;I didn’t know there was a recall.&quot;
 Objection 1: &quot;Thanks for letting me share this with you. It’s important we address this
for your safety. Let me check the next available appointment for you.&quot;
 Objection 2: &quot;Recalls ensure your vehicle operates safely and as intended. Since it’s free
of charge, it’s a great opportunity to ensure your vehicle is in top condition. Shall we
book a time?&quot;

9. Concern About Appointment Duration
Reason: &quot;How long will it take?”, “The service is going to take too long.”
 Objection 1: “I completely understand. We provide alternate transportation for your
convenience. Would that work for you?”
 Objection 2: &quot;We understand your time is valuable. Let’s schedule a time that works best
for you, and we’ll do our best to get you in and out promptly.&quot;

10. Waiting for Another Service
Reason: &quot;I’ll schedule it when I need something else done.&quot;
 Objection 1: &quot;That’s a great plan, but some recalls should be addressed sooner for safety
reasons. Let’s take care of this now to ensure your vehicle is safe.&quot;

10. Schedule/Availability
Reason: &quot;I will schedule when I am ready.”, “I am not sure when I will be available.”
 Objection 1: &quot;That’s a great plan, but some recalls should be addressed sooner for safety
reasons. We can work around your schedule to ensure you can get this taken care of right
away.”

Here is some additional information about the person you are calling:

Name: {{first_name}} {{last_name}}
State: {{state}}
Year: {{year}}
Make: {{make}}
Model: {{model}}
Recall Description: {{recall_description}}
Recall Number: {{recall_number}}
""",
        "startSentence": "Hi, my name is Alex and I am calling on behalf of Audi New Rochelle. May I please speak with {{first_name}} {{last_name}}?",
        "allowedTransferNumbers": ["+1234567890", "+1987654321"],
        "model": "gpt-4o",
        "info": {},
        "wsBaseUrl": "wss://brainbase-monorepo.onrender.com"
    }
    
    response = requests.post(
        f"{BASE_URL}/workers/{worker_id}/deployments/voicev1",
        json=deployment_data,
        headers=headers
    )
    assert response.status_code == 201, f"Failed to create deployment: {response.text}"
    return response.json()


def create_batch_call(worker_id, deployment_id, batch_data):
    """Make batch calls for a voice v1 deployment"""
    current_time = int(time.time())
    print(f"Creating batch calls at: {datetime.fromtimestamp(current_time).isoformat()}")
    print(f"Current time: {current_time}")
    
    
    response = requests.post(
        f"{BASE_URL}/workers/{worker_id}/deployments/voicev1/{deployment_id}/make-batch-calls",
        json=batch_data,
        headers=headers
    )
    assert response.status_code == 200, f"Failed to create batch calls: {response.text}"
    return response.json()




def main():
    try:
        worker_id = "worker_f77a7ec0-7b6a-4408-8bfb-d463ade44e87"
        flow_id = "flow_e743ef5e-322d-47fe-8113-d9f1f912ca1b"
        deployment_id = "deploy_2f054b49-56b0-4159-99bc-ac7416e45402"
        print("Creating batch calls...")
        batch_result = create_batch_call(worker_id, deployment_id, BATCH_DATA)
        print("Batch calls created successfully!")
        print(json.dumps(batch_result, indent=2))

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 