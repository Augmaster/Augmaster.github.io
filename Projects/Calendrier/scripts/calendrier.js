/*
	Étudiant 1 : Augustin Renard
	Étudiant 2 : Miguel Fortin
	TECH20711  - Développement d'applications d'affaires
*/


/*
 * Retourne la correspondance en lettres du mois passé en paramètre.
 *		1  -> Janvier
 *		2  -> Février
 *		...
 *		12 -> Décembre
 */
const moisEnLettres = (numMois) => {
	let mois = {
		1: "Janvier",
		2: "Février",
		3: "Mars",
		4: "Avril",
		5: "Mai",
		6: "Juin",
		7: "Juillet",
		8: "Aout",
		9: "Septembre",
		10: "Octobre",
		11: "Novembre",
		12: "Décembre"
	}
	return mois[numMois]
}

/*
 * Calcule et retourne le nombre de jours du mois de l'année (passés en paramètres).
 *	1  -> 31
 *	2  -> (29 ou 28) Selon si l'année est bissextile ou pas
 *	3  -> 31
 *	4  -> 30
 *	...
 *	12 -> 31
 */
const getNbJours = (mois, annee) => {
	let isBissextile = false
	let jourMois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if ((annee % 4 == 0 && annee % 100 > 0) || (annee % 400 == 0)) {
		isBissextile = true
	} else {
		isBissextile = false
	}

	if (isBissextile) {
		if (mois == 2) {
			return jourMois[mois - 1] + 1
		} else {
			return jourMois[mois - 1]
		}
	} else {
		return jourMois[mois - 1]
	}
}

/*
 * Calcule et retourne un chiffre [0,6] représentant le jour de la semaine correspondant à la date
 * passée en paramètre (jour, mois, année) :
 *		0 -> Dimanche
 *		1 -> Lundi
 *		2 -> Mardi
 *		3 -> Mercredi
 *		4 -> Jeudi
 *		5 -> Vendredi
 *		6 -> Samedi
 */
const jourDeSemaine = (jour, mois, annee) => {
	let j = jour
	let m = mois
	let a = annee
	let a1 = 0
	let m1 = 0
	if (m >= 3) {
		m1 = m - 2
		a1 = a
	} else if (m < 3) {
		m1 = m + 10
		a1 = a - 1
	}
	a1 = String(a1)
	let aS = parseInt(a1.substring(2, 4))
	let nS = parseInt(a1.substring(0, 2))
	let f = j + aS + ~~(aS / 4) - 2 * nS + ~~(nS / 4) + ~~((26 * m1 - 2) / 10)
	if (f < 0) {
		return (f + 7) % 7
	}
	else {
		return f % 7
	}
}

/*
 * Calcule et retourne un chiffre [0,6] représentant le jour de la semaine correspondant au premier jour
 * du mois et de l'année passés en paramètres.
 * ! Pensez à appeler la fonction jourDeSemaine() définie précédemment au lieu de réinventer la roue.
 */
const premierJourDuMois = (mois, annee) => {
	let premJour = jourDeSemaine(1, mois, annee)
	return premJour
}

/*
 * Construit et retourne un tableau JS (Array) contenant les dates du mois de l'année passés en paramètre
 * Exemple :
 * 	Pour les valeurs ci-dessous (passées en paramètre) 
 * 		mois  = 1
 *		annee = 2020
 *	la fonction retournera le tableau (Array) à deux dimensions ci-dessous représentant 
 *  les dates organisées en semaines :
 *
 *	[[undefined, undefined, undefined, 1, 2, 3, 4],
 *	 [ 5,  6,  7,  8,  9, 10, 11]
 *	 [12, 13, 14, 15, 16, 17, 18]
 *	 [19, 20, 21, 22, 23, 24, 25]
 *	 [26, 27, 28, 29, 30, 31, empty]]
 * 
 */
const getTableauCalendrier = (mois, annee) => {
	let tab = []
	let fstday = premierJourDuMois(mois, annee)
	let count = 0
	let total = fstday + getNbJours(mois, annee)
	let WeekNum = Math.ceil(total / 7)

	for (let y = 0; y < WeekNum; y++) {
		tab.push([])
	}
	for (let z = 0; z < fstday; z++) {
		tab[count].push(undefined)
	}
	console.log(tab)
	for (let i = 1; i <= getNbJours(mois, annee); i++) {
		if (tab[count].length == 7) {
			count += 1
			tab[count].push(i)
		} else {
			tab[count].push(i)
		}
	}
	while (tab[tab.length - 1].length < 7) {
		tab[tab.length - 1].push(undefined)
	}
	return tab
}

/*
 * Construit le sous-arbre DOM du document représentant un tableau (table) correspondant au calendrier du mois de
 * l'année passés en paramètres et retourne le noeud racine représentant cet arbre.
 */


const getArbreDOMCalendrier = (mois, annee) => {
	let calendrier = document.getElementById("calendrier")
	let weekList = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
	let table = document.createElement("table")
	let caption = document.createElement("caption")
	let thead = document.createElement("thead")
	let tbody = document.createElement("tbody")
	let tr = document.createElement("tr")
	let th = document.createElement("th")


	calendrier.appendChild(table)
	table.appendChild(caption)
	table.appendChild(thead)
	table.appendChild(tbody)
	thead.appendChild(tr)

	table.className = "table table-bordered table-light table-striped caption-top text-center col-lg-6 mx-auto mb-0"
	caption.className = "bg-dark text-light text-center font-weight-bold"
	caption.innerHTML = `${moisEnLettres(mois)} ${annee}`
	thead.className = "thead-dark"
	for (element of weekList) {
		let th = document.createElement("th")
		tr.appendChild(th).innerHTML = element
	}


	th = document.createElement("th")
	let td = document.createElement("td")
	let tableau = getTableauCalendrier(mois, annee)

	for (element of tableau) {
		tr = document.createElement("tr")
		for (item of element) {
			let td = document.createElement("td")
			let span = document.createElement("span")
			span.className = "badge badge-pill badge-light"
			if (item == undefined) {
				span.innerHTML = ""
			}
			else {
				span.innerHTML = item
			}
			td.appendChild(span)
			tr.appendChild(td)
		}
		tbody.appendChild(tr)
	}

}
