# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_ai import PodAI, ImageProcessingMode

try:
    pod_ai = PodAI(api_token=API_TOKEN, sc_api_key=SC_API_KEY_IMAGE_PROCESSING)

    print(pod_ai.image_processing_authentication(image1=IMAGE_1, image2=IMAGE_2, mode=ImageProcessingMode.NORMAL))
    # OUTPUT
    # {'confidence': None, 'resultStatus': 0}

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
