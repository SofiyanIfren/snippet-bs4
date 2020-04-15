# 1. Tag se réfère à une balise XML ou HTML réelle dans le document
# classe et l'id d'une balise en utilisant tag['class'] et tag['id']
# 2. Le texte dans une balise est stocké en tant que NavigableString
# convertir un NavigableString en chaîne unicode en utilisant unicode()
# 3. commentaires dans une page Web, stockés sous forme d'un objet Comment
# 4. BeautifulSoup utilisé pour représenter le document dans son ensemble
# Examples: 
# soup.select('div') All elements named <div>
# soup.select('#author') The element with an id attribute of author
# soup.select('.notice') All elements that use a CSS class attribute named notice
# soup.select('div span') All elements named <span> that are within an element named <div>
# soup.select('div > span') All elements named <span> that are directly within an element named <div>, with no other element in between
# soup.select('input[name]') All elements named <input> that have a name attribute with any value
# soup.select('input[type="button"]') All elements named <input> that have an attribute named type with value button
import requests
from bs4 import BeautifulSoup
import time
import csv
import codecs

# BS4 boucles :Création CSV monarques de France
url = "https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France"
req = requests.get(url)

page = req.text
soup = BeautifulSoup(page, "lxml")

en_tetes = [u"nom du roi", u"date de début de règne", u"date de fin de règne", u"description"]
csv_file = codecs.open('data.csv', mode='w', encoding='utf-8')
csv_file.write(";".join(en_tetes)+"\n")

rangs = soup.select('tr > td')
for col in rangs:
	print(col.text)
	'''col = tr.find_all('td')
	if (len(col) > 4
		and len(col[1].get_text()) != 0
		and len(col[2].get_text()) != 0
		and len(col[3].get_text()) != 0
		and len(col[4].get_text()) != 0):
		nom_roi = col[1].get_text()
		debut_regne = col[2].get_text()
		fin_regne = col[3].get_text()
		description = col[4].get_text()
		donnees = str(nom_roi) + "; " + str(debut_regne) + "; " + str(fin_regne) + "; " + str(description) + "\n"
		csv_file.write(donnees)'''
csv_file.close()

# BS4 Simple: Calendrier Solaire/lunaire en console
# Gregorian Calendar
now = time.strftime('%d/%m/%Y')
print ("***** Le " + str(now) + " *****")

# Hijri Calendar
url = "http://www.ummulqura.org.sa/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

day = soup.find("span", {"id": "ContentPlaceHolder1_homepage1_lblHDay"})
month = soup.find("span", {"id": "ContentPlaceHolder1_homepage1_lblHMonthNumber"})
month_text = soup.find("span", {"id": "ContentPlaceHolder1_homepage1_lblHMonthE"})
year = soup.find("span", {"id": "ContentPlaceHolder1_homepage1_lblHYear"})

print ("-> Jour  : " + str(day.text) + "\n-> Mois  : " + str(month_text.text) + " (" + str(month.text) + ")\n-> Année : " + str(year.text))

# Zakat OR & ARGENT
url = 'http://www.24hgold.com/francais/cours_or_argent.aspx?money=EUR'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

gramme_or = soup.find("span", {"id": "ctl00_BodyContent_lbDevGramPrice"})
gramme_argent = soup.find("span", {"id": "ctl00_BodyContent_Span48"})
gramme_or_float = (gramme_or.text).replace(",", ".")
gramme_argent_float = (gramme_argent.text).replace(",", ".")
nissab_or = float(gramme_or_float) * 85
nissab_argent = float(gramme_argent_float) * 595

print (round(nissab_or, 2))
print (round(nissab_argent, 2))

##############################################################################
##############################################################################
##############################################################################
# In Python 3, you can use the sep= and end= parameters of the print function:
# To not add a newline to the end of the string:
# print('.', end='')
# To not add a space between all the function arguments you want to print:
# print('a', 'b', 'c', sep='')
url = "https://fr.wikipedia.org/wiki/Liste_des_califes"
req = requests.get(url)

page = req.text
soup = BeautifulSoup(page, "lxml")
myDiv = soup.find("div", {"id": "mw-content-text"})
myTr = myDiv.select("div > table > tbody > tr")
for i in myTr:
	if (len(i) > 4):
		if (i.find("th") != None and i.find("th").attrs.get("class") != "navbox-group"):
			print("", end='')
		else:
			print(i.text, end='')
		print("**************************************************************")
