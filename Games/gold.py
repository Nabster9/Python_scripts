import requests
from bs4 import BeautifulSoup
import termcolor
import os
from time import sleep
from datetime import datetime


# seller__name-detail
# offer-price-amount
# other_offer-desk-main-box other_offer-div-box

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

URL = "https://www.g2g.com/offer/Trixion---EU-Central?service_id=lgc_service_1&brand_id=lgc_game_23027&region_id=ac3f85c1-7562-437e-b125-e89576b9a38e&fa=lgc_23027_dropdown_17%3Algc_23027_dropdown_17_44715&sort=lowest_price&include_offline=0"

while(True):
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time+" Getting price for 10k gold...")
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	parentDiv = soup.find_all("div", class_="other_offer-desk-main-box other_offer-div-box")
	for number in parentDiv:
	    sellerName = number.find("div", class_="seller__name-detail")
	    sellerPrice = number.find("span", class_="offer-price-amount")
	    price = float(sellerPrice.text)*10000
	    print(str(f"{price:.2f}")+" euros|"+sellerName.text)

	for i in range(9, 0, -1):
	    print("update in "+ str(i)+" mins", end = '\r')
	    sleep(60)
	clearConsole()

