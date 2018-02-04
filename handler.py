import sys
import os
import json

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))
import requests

KINTONE_BASE_URL = os.environ['KINTONE_URL']
KINTONE_FORM_BASE_URL = os.environ['KINTONE_FORM_BASE_URL']
URL = KINTONE_BASE_URL.format(
    kintone_domain=os.environ['KINTONE_DOMAIN'],
    kintone_app=os.environ['KINTONE_APP']
)
FORM_URL = KINTONE_FORM_BASE_URL.format(
    kintone_domain=os.environ['KINTONE_DOMAIN'],
    kintone_app=os.environ['KINTONE_APP']
)
HEADERS_KEY = os.environ['KINTONE_HEADERS_KEY']
API_KEY = os.environ['KINTONE_API_KEY']

def run(event, context):
    
    headers = {HEADERS_KEY: API_KEY}
    record_data = get_all_records(headers)
    records = record_data['records']

    form_data =get_form_info(headers)
    forms = form_data['properties']

    result = {
        "records": records,
        "properties": forms
    }

    return result

def get_all_records(headers):
    query = u''
    
    response_record = requests.get(URL + query , headers=headers)
    return json.loads(response_record.text)

def get_form_info(headers):
    
    response_record = requests.get(FORM_URL, headers=headers)
    return json.loads(response_record.text)
