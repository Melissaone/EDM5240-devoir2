# coding: utf-8

### Bonjour Mélissa! N'oublie pas d'ajouter «.py» à tes nom de scripts :)
### Plusieurs problèmes, malheureusement, dans ton script. Je te réfère au corrigé pour une solution complète et détaillée.

import json
import csv 
import requests

fichier = "banq.csv"
i = 0

entete = {
	"User-Agent":"Tiffany Toussaint",
	"From":"cg491001@ens.uqam.ca"
}

for n in range(1000,2001):
	### Ici, au premier passage de la boucle, i += n donne 1000
	### Au 2e, par contre, puisque i = 1001, i += n donne 2001
	### Au 3e, ça donne 3003, et ainsi de suite...
	i += n 

	url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

	k = str(i)
	j = url + k 
	m = j.strip( )
	print(m) ### J'ai ajouté cela pour voir la valeur de «m»
	### Il est plus facile de construire ton URL ainsi:
	url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/" + str(n)

	req = requests.get(m,headers=entete)

	print(req)

	for music in req : 
		if "audio" in req :
		
			infos = []

			infos.append(music["titre : "	])
			infos.append(music["interprété par"])

			for music in annee.values():
				infos.append(music["annee"])

				infos.append(description["lien"])
				print(infos)
				i -= n
