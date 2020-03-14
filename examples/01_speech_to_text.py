# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_ai import PodAI

try:
    pod_ai = PodAI(api_token=API_TOKEN, sc_api_key=SC_API_KEY_SPEECH_TO_TEXT)

    print(pod_ai.speech_to_text(link_file=VOICE_LINK))
    # OUTPUT
    # {'phonetic': None, 'text': 'داریم تست می کنیم', 'duration': 4}

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
