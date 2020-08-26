# -*- coding: utf-8 -*-
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

import tools

ise_host = "10.122.176.10"
ise_user = "apiadmin"
ise_passwd = "Ise1234!"
HEADERS = {
        'Accept': "application/json",
        'Content-Type': "application/json",
}
filename = "cvs/endpoint.csv"
uri = "https://10.122.176.10:9060/ers/config/endpoint/"

data = tools.open_csv(filename)

for row in data:
    mac = row["MAC"]
    if tools.verify_mac(mac):
        endpoint_id = tools.get_endpoint_id(mac,ise_user,ise_passwd,HEADERS)
    else:
        print("Invalid MAC Address")
        continue
    if endpoint_id:
        if tools._delete(uri,ise_user,ise_passwd,HEADERS,endpoint_id) == 204:
            print("Succcesfully deleted MAC Address:",mac)
    else:
        print("MAC Address:",mac," is not in the database")
print("Script completed successfully")
