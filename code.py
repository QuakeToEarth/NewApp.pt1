from tkinter import *
from django.http import response
import requests
from tkinter import messagebox
root = Tk()
root.title('News App')
root.geometry('1700x500')
def fetchcountrycode():
    countryName = country_text.get()
    response = requests.get("https://api.printful.com/countries")
    data = response.json()
    results = data["result"]
    cc = 'none'
    for r in results:
        if r['name'].lower() == countryName.lower():
            cc = r['code']

    if cc == 'none' :
        messagebox.showerror('Error :(', 'country is not found {}'.format(countryName))
    else:
        print(cc)
        fetchNews(cc)

def fetchNews(cc):
    pass
country_text = StringVar()
country = Entry(root,textvariable = country_text)
country.pack()
searchButton = Button(root,text = "Get News",width=12, command= fetchcountrycode)
searchButton.pack()
root.mainloop()