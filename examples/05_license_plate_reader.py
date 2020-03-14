# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_ai import PodAI

pod_ai = PodAI(api_token=API_TOKEN, sc_api_key=SC_API_KEY)
try:
    image = "http://mepatogh.ir/wp-content/uploads/2016/04/5712234300227-mepatogh.ir.jpg"
    print(pod_ai.license_plate_reader(image=image, is_crop=False))
    # OUTPUT
    # [
    #   {
    #     "confidence": 0.9658130407333374,
    #     "text": "23Z31225",
    #     "token": "20200301_075425_628526rqhginwzes",
    #     "xmax": 80,
    #     "xmin": 10,
    #     "ymax": 293,
    #     "ymin": 275
    #   },
    #   {
    #     "confidence": 0.7229224443435669,
    #     "text": "98S947",
    #     "token": "20200301_075425_628526rqhginwzes",
    #     "xmax": 238,
    #     "xmin": 193,
    #     "ymax": 80,
    #     "ymin": 69
    #   },
    #   {
    #     "confidence": 0.9704036712646484,
    #     "text": "11V11427",
    #     "token": "20200301_075425_628526rqhginwzes",
    #     "xmax": 332,
    #     "xmin": 157,
    #     "ymax": 206,
    #     "ymin": 156
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

print("RAW Result : ", pod_ai.raw_result())
