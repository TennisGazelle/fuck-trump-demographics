#!/usr/bin/python
import requests
import json
import random

def flip_coin():
    return random.randint(0, 1) == 0

num_requests = 1000
url_header = 'https://donate.donaldjtrump.com/the-official-weekly-presidential-approval-poll'
with open ('./names.json', 'r') as f:
    names = json.load(f)

region_index = random.randint(0, len(names))
payload = {
    "utm_source": "dp_fb",
    "utm_medium": "ad",
    "utm_campaign": "20191115_na_approvalpoll_djt_tmagacpros_ocpmycr_bh_audience0255_creative02365_copy00768_us_b_18-65_nf_all_na_lp0004_acq_conversion_static_1_1_na",
    "utm_content": "sur",
    "additional[content_slug]": "rate-trumps-job-performance",
    "additional[issue]": "GOP",
    "additional[topic]": "Surveys"
}
email_domains = [
    'gmail.com',
    'yahoo.com',
    'hotmail.com',
     
]

for i in range(num_requests):
    gender = 'male' if flip_coin() else 'female'
    first_name_index = random.randint(0, len(names[region_index][gender]) - 1)
    last_name_index = random.randint(0, len(names[region_index]['surnames']) - 1)
    email_index = random.randint(0, len(email_domains) - 1)

    payload['firstname'] = names[region_index][gender][first_name_index]
    payload['lastname'] = names[region_index]['surnames'][last_name_index]
    payload['email'] = payload['firstname'] + '_' + payload['lastname'] + '@' + email_domains[email_index]
    payload['zip'] = random.randint(10000, 99999)
    print(json.dumps(payload, indent = 3))

    response = requests.get(url_header, payload)
    print('SENT!' if response.status_code == 200 else 'ERROR NOT SENT', '({})'.format(gender))
