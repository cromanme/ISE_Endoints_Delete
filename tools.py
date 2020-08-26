"""Tools module for Main Program"""
__author__ = "Christian Méndez Murillo"
__email__ = "cmendezm@cisco.com"
__copyright__ = """
Copyright 2020, Cisco Systems, Inc. 
All Rights Reserved. 
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE. 
"""
__status__ = "Development"  # Prototype, Development or Production

import json
import requests
import warnings
import sys
import csv
import re
import os

requests.packages.urllib3.disable_warnings()

def _get(uri,username,password,HEADERS):
    response = requests.get(url=uri, auth=(username,password), headers=HEADERS, verify=False)
    if response.ok:
        data = response.json()
    else:
        data = response.status_code
    return data

def _delete(uri,username,password,HEADERS,endpoint_id):
    response = requests.delete(url=uri + endpoint_id, auth=(username,password), headers=HEADERS, verify=False)
    return response.status_code

def verify_mac(mac):
    if mac and re.search(r'([0-9A-F]{2}[:]){5}([0-9A-F]){2}', mac.upper()) is not None:
        return True
    else:
        return False

def get_endpoint_id(mac,username,password,HEADERS):
    uri = "https://10.122.176.10:9060/ers/config/endpoint/name/" + mac
    data = _get(uri,username,password,HEADERS)
    if data == 404:
        endpoint_id = None
    else:    
        endpoint_id = data.get("ERSEndPoint").get("id")
    return endpoint_id

def open_csv(filepath):
    try:
        with open(os.path.expanduser(filepath), newline="") as csvfile:
            csv_content = list(csv.DictReader(csvfile))
            if not csv_content:
                sys.exit(f"File '{filepath}' is empty")
            else:
                return csv_content    

    except OSError as e:
        print(e)
        sys.exit(f"File '{filepath}' was not found!")
