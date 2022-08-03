from bs4 import BeautifulSoup
import requests
import csv
import datetime

# variables
url = 'https://suzuki.com.co/motocicletas/categoria/sport'
gixxer_150_abs_id = 'carrusel-moto-806'
precio_class = 'precio'
rows = ['price', 'date', 'time']
csv_name = 'precio.csv'

#get the current date and time
now = datetime.datetime.now()

# Get the HTML from the URL
page_html = requests.get(url)

# Parse the HTML
page = BeautifulSoup(page_html.content, 'html.parser')
gixxer_150_abs = page.find(id=gixxer_150_abs_id)

# Get the data
price = gixxer_150_abs.find(class_=precio_class).text

# remove the dollar sign and comma and convert to float
price = int(price.replace('$', '').replace(',', ''))

# create csv file if it doesn't exist and appends data to it
with open(csv_name, 'a') as csv_file:
    # create a csv writer object
    writer = csv.writer(csv_file)

    # check if the file is empty
    if csv_file.tell() == 0:
        # write the headers
        writer.writerow(rows)

    # write the price as a row
    writer.writerow([price, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
    csv_file.close()
