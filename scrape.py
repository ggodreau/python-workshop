# I need to first download the page, and i do that by using the Python requests library, then use the import requests
# The requests library will make a GET request to a web server,which will download the HTML contents of a given web page.
# I want to download the japp.nl page for sale property in amsterdam and i'll use the the requests.get method.

import requests

page = requests.get("http://www.jaap.nl/koophuizen/noord+holland/groot-amsterdam/amsterdam")
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Now i want to get the address, post code, price and sqm of each property
#def amsterdam ():
# property_price = soup.find_all
list_of_address = []
for address in soup.find_all(class_="property-address-street"):
            address = address.text.strip()
            list_of_address.append(address)
            print(list_of_address)

list_of_post_code = []
for post_code in soup.find_all(class_="property-address-zipcity"):
        post_code = post_code.text.strip().replace(',  Amsterdam', '')
        list_of_post_code.append(post_code)
        print(list_of_post_code)

list_of_price = []
for price in soup.find_all(class_="property-price"):
        price1 = price.text.strip().replace('€', '')
        price2 = price1.strip().replace('k.k.', '')
        price3 = price2.strip().replace('v.o.n.', '')
        price4 = price3.replace('.', '')
        price4 = int(price4)
        list_of_price.append(price4)
        print(list_of_price)


list_of_type =[]
list_of_rooms =[]
list_of_sqm =[]
for features in soup.find_all('div', {"class": "property-features"}):
        type=(features.contents[1].text.strip())
        rooms = (features.contents[3].text.strip())
        sqm = (features.contents[5].text.strip().replace('ᵐ²', ''))
        sqm = int(sqm)

        list_of_type.append(type)
        list_of_rooms.append(rooms)
        list_of_sqm.append(sqm)




#now im going to put it in tabular form using pandas
import pandas as pd
amsterdam = pd.DataFrame({
        "address": list_of_address,
        "post_code": list_of_post_code,
        "price": list_of_price,
        "type_of_property": list_of_type,
        " number_of_rooms": list_of_rooms,
        "living_area (m2)": list_of_sqm})
  #      "number_of_rooms";
   #     "living_area":

amsterdam
print (amsterdam)

#now im gong to send it to an excel file
#import xlsxwriter
#
#writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
#amsterdam.to_excel(writer,sheet_name='Sheet1')
#writer.save()
