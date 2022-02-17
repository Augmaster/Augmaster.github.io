/*
	Étudiant 1 : Augustin Renard
	Étudiant 2 : Miguel Fortin
	TECH20711  - Développement d'applications d'affaires
*/

window.addEventListener("load", () => {

	/*
	 * Après le chargement de la page web :
	 *	1- Récupérer le mois et l'année courants
	 *  2- Récupérer la liste déroulante pour la sélection du mois, la remplir dynamiquement avec toutes les options
	 *	   et sélectionner celle représentant le mois courant.
	 *	3- Récupérer dynamiquement la zone de texte du formulaire et lui attribuer la valeur correspondante à l'année
	 *     courante.
	 *	4- Compléter la sous-fonction "updateCalendar" servant de gestionnaire d'évènement et permettant d'attacher
	 *     à la page web le nouvel arbre DOM créé par la fonction "getArbreDOMCalendrier".
	 *  5- Appeler la fonction manuellement pour un affichage initial correspondant à la date sélectionnée.
	 *  6- Inscrire les éléments du formulaire aux différents évènements permettant la mise-à-jour du calendrier.
	 */

	let mois;
	let annee;
	let listeMois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
	let date = new Date()
	let currentMonth = date.getMonth()
	let currentYear = date.getFullYear()
	let selectMonth = document.getElementById("selectMois")
	let inputYear = document.getElementById("inputAnnee")

	mois = currentMonth + 1
	annee = currentYear

	for (let element of listeMois) {
		if (element == listeMois[currentMonth]) {
			let option = document.createElement("option")
			option.setAttribute("selected", "")
			selectMonth.appendChild(option).innerHTML = element
		} else {
			let option = document.createElement("option")
			selectMonth.appendChild(option).innerHTML = element
		}
	}
	inputYear.setAttribute("value", currentYear)
	mois = currentMonth

	getArbreDOMCalendrier(mois + 1, annee)
	selectMonth.addEventListener("change", () => {
		mois = listeMois.indexOf(selectMonth.value) + 1
		let table = document.getElementById("calendrier")
		table.innerHTML = ""
		getArbreDOMCalendrier(mois, annee)
	})
	inputYear.addEventListener("input", () => {
		let table = document.getElementById("calendrier")
		table.innerHTML = ""
		annee = inputYear.value
		getArbreDOMCalendrier(mois, annee)
	})


	//Votre code pour répondre aux points 5 et 6 ici


});