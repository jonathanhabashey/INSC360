import requests
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    filename='HW8-log' + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

webFile = open("hw8-input.txt", "r")

for web in webFile:

    web = web.strip()
    r = requests.get(web)
    logging.info("Now attempting to get data at: {}".format(web))
    print("Now attempting to get data at: {}".format(web))
    if r.status_code == 200:
        logging.info("200 - Successfully retrieved {}".format(web))
        print("200 - Successfully retrieved {}".format(web))
        print("\n")
        rcontent = ET.fromstring(r.content)

        customer_node = rcontent.findall("customer")

        for customer in customer_node:
            cID = customer.find("id").text
            logging.info("Now processing customer ID {}".format(cID))
            name = customer.find("name").text
            print(name, "\n")
            checkNodes = customer.findall("checking_account")
            for cNode in checkNodes:
                print("Checking Account: ", cNode.text, "\n")
            savNodes = customer.findall("savings_account")
            for sNode in savNodes:
                print("Savings Account: ", sNode.text, "\n")

    elif r.status_code == 404:
        print("404 - Resource not found for {}".format(web))
        logging.info("404 - Resource not found for {}".format(web))
        print("\n")
    else:
        logging.error("A problem occured while retrieveing info from {}".format(web))
