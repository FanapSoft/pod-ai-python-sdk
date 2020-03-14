# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_ai import PodAI

pod_ai = PodAI(api_token=API_TOKEN, sc_api_key=SC_API_KEY_NLU_BANKING)
try:

    text = "از حساب 1004.8000.12345678.1 مبلغ 2000000 ریال به حساب 1004.70000.15645465.5 انتقال بده"
    print(pod_ai.nlu_banking(text=text))
    # OUTPUT
    # {
    #   "intent": "Transfer",
    #   "subIntent": "AccountToAccount",
    #   "originAccount": "حساب 10048000123456781 مبلغ",
    #   "destinationAccountHolder": "حساب 100470000156454655",
    #   "amount": 2000000
    # }

    text = "۵ میلیون بفرست به کارت 6037997256803041"
    print(pod_ai.nlu_banking(text=text))
    # OUTPUT
    # {
    #   "intent": "Transfer",
    #   "subIntent": "AccountToAccount",
    #   "destinationAccountHolder": "کارت 6037997256803041",
    #   "amount": 50000000
    # }

    text = "5000تومن شارژ ایرانسل"
    print(pod_ai.nlu_banking(text=text))
    # OUTPUT
    # {
    #   "intent": "BUYPHONECHARGE",
    #   "subIntent": "PHONECHARGE",
    #   "operatorName": "ایرانسل",
    #   "mobileOperator": "MTN",
    #   "chargeType": 1,
    #   "amount": 50000
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

print("RAW Result : ", pod_ai.raw_result())
