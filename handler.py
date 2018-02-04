import sys
import os
import json
from datetime import datetime
import boto3

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

S3_BUCKET = os.environ['S3_BUCKET']
S3_OBJECT_PREFIX = os.environ['S3_OBJECT_PREFIX']

s3_client = boto3.client('s3')

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

    return put_data_to_s3(result)

def get_all_records(headers):
    query = u''
    
    response_record = requests.get(URL + query , headers=headers)
    return json.loads(response_record.text)

def get_form_info(headers):
    
    response_record = requests.get(FORM_URL, headers=headers)
    return json.loads(response_record.text)

def put_data_to_s3(contents):
    date = datetime.now()
    date_str = date.strftime("%Y%m%d%H%M%S")
    tmp_dir = "/tmp/"
    tmp_file = S3_OBJECT_PREFIX + "_" + date_str + ".json"

    with open(tmp_dir + tmp_file, 'w') as file:
        file.write(json.dumps(contents, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))

    s3_client.upload_file(tmp_dir + tmp_file, S3_BUCKET, tmp_file)

    return True
