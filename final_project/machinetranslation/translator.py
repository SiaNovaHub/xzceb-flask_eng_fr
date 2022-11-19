'''
This is the final project for python course
'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# IBM watson translator credentials
apikey = os.environ['apikey']
url = os.environ['url']

# IBM watson translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-19',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    This function take english input and translates it to french text
    '''
    french_text_dic = json.dumps(language_translator.translate(text=english_text, \
     model_id='en-fr').get_result(), indent=2, ensure_ascii=False)
    french_text= json.loads(french_text_dic)
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''
    This function take french input and translates it to english text
    '''
    english_text_dic = json.dumps(language_translator.translate(text=french_text, \
     model_id='fr-en').get_result(), indent=2, ensure_ascii=False)
    english_text= json.loads(english_text_dic)
    return english_text["translations"][0]["translation"]
