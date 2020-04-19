import requests
import xml.etree.ElementTree as ET
import logging
import xml.dom.minidom

logging.basicConfig(
    filename='HW8-log' + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


webFile = open("hw8-input.txt","r")


for web in webFile:

    web = web.strip()
    r = requests.get(web)
    #rcontent = ET.fromstring(r.content)
    logging.info("Now attempting to get data at: {}".format(web))
    if r.status_code == 200:
        logging.info("200 - Successfully retrieved {}".format(web))
        print("200 - Successfully retrieved {}".format(web))
        rcontent = ET.fromstring(r.content)
        customer_node = rcontent.findall("customer")
        for customer in customer_node:
            cID = customer.find("id").text
            name = customer.find("name").text
            checking = customer.find("checking_account")
            if checking != None:
                check = checking.text
            else:
                check = "\n"
            savings = customer.find("savings_account")
            if savings != None:
                save = savings.text
            else:
                save = "\n"

            print(name, "\n", check, "\n", save)

    elif r.status_code == 404:
        print("404 - Resource not found for {}".format(web))
        logging.info("404 - Resource not found for {}".format(web))
 #   else:
    #   logging.error("")
