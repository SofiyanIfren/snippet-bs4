# 1. Tag se réfère à une balise XML ou HTML réelle dans le document
# classe et l'id d'une balise en utilisant tag['class'] et tag['id']
# 2. Le texte dans une balise est stocké en tant que NavigableString
# convertir un NavigableString en chaîne unicode en utilisant unicode()
# 3. commentaires dans une page Web, stockés sous forme d'un objet Comment
# 4. BeautifulSoup utilisé pour représenter le document dans son ensemble
import requests
from bs4 import BeautifulSoup
import csv
import codecs

url = "https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France"
req = requests.get(url)

page = req.text
soup = BeautifulSoup(page, "lxml")

en_tetes = [u"nom du roi", u"date de début de règne", u"date de fin de règne", u"description"]
csv_file = codecs.open('data.csv', mode='w', encoding='utf-8')
csv_file.write(";".join(en_tetes)+"\n")

rangs = soup.find_all('tr')
for tr in rangs:
	col = tr.find_all('td')
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
		csv_file.write(donnees)
csv_file.close()