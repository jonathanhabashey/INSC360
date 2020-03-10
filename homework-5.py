# Author: Jonathan Habashey
# Date: 03/09/2020
# Description: This program reads in a file and calculates their quarterly earnings while making sure any errors
# are reported and that those errors dont stop the program. It also logs successes, not just errors.

import logging
import datetime
import csv

logging.basicConfig(
    filename='HW5-log' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


counter = 0


with open ('input-data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  next(reader)  # Python next() skips to the next line. So skipping the header row
  for row in reader:
    try:
        counter += 1  # keep track of how many records we have processed.
        sales_total = int(row[1]) + int(row[2]) + int(row[3])
        print("{} - Total first quarter sales for store {}: ${:,}".format(counter, row[0], sales_total))
        logging.info("Sucessfully read in line {}".format(counter))

    except:
      print("Missing element")
      logging.error("Missing a number in line {}".format(counter))

