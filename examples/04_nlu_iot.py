# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_ai import PodAI

pod_ai = PodAI(api_token=API_TOKEN, sc_api_key=SC_API_KEY_NLU_IOT)
try:

    text = "شبکه تلویزیون را عوض کن"
    print(pod_ai.nlu_iot(text=text))
    # OUTPUT
    # {
    #   "order": "SWITCH",
    #   "object": "TV",
    #   "location": "DEFAULT",
    #   "timeToGo": 1583319861,
    #   "mode": {}
    # }

    text = "کانال تلویزیون و عوض کن"
    print(pod_ai.nlu_iot(text=text))
    # OUTPUT
    # {
    #   "order": "SWITCH",
    #   "object": "TV",
    #   "location": "DEFAULT",
    #   "timeToGo": 1583319862,
    #   "mode": {}
    # }

    text = "هوا خیلی گرمه"
    print(pod_ai.nlu_iot(text=text))
    # OUTPUT
    # {
    #   "order": "SET",
    #   "object": "AIR",
    #   "location": "DEFAULT",
    #   "timeToGo": 1583319862,
    #   "mode": {
    #     "change": "mode",
    #     "value": "COLD"
    #   }
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

print("RAW Result : ", pod_ai.raw_result())
