import os
import html
from google.cloud import translate_v2 as translate

# Get the value of the environment variable
google_application_credentials = os.environ.get(
    "GOOGLE_APPLICATION_CREDENTIALS")

client = translate.Client()


# Function to translate text using Google Translate
def analyze_translate(text):
    raw_translation_data = client.translate(text, target_language="en")
    # .translate() function output has multiple items, so specify which is needed
    # translatedText has HTML errors on output, so import html and use unescape to fix
    decoded_translation_output = html.unescape(
        raw_translation_data['translatedText'])
    return decoded_translation_output
