import requests
import bs4
import time
import tkinter
from tkinter import messagebox

url = 'https://www.apple.com/in/iphone/'

while True:
        site_content = requests.get(url)
        htmlContent = site_content.content
        soup = bs4.BeautifulSoup(htmlContent, 'html.parser')
        prices = []
        for data in soup.findAll('p', {'class': 'typography-body-reduced copy-pricing'}):
            prices.append(data.text)
        proprice = prices[0]
        exact_price = proprice[6]+proprice[8:10]+proprice[11:14]
        print(exact_price)
        if int(exact_price)>100000:
            tkinter.messagebox.showinfo(title='Dont Wait', message= 'Buy Now')
        else:
            tkinter.messagebox.showwarning(title='No Hurries', message= 'Price too high')
        time.sleep(5)
