/*
	Étudiant 1 : Augustin Renard
	Étudiant 2 : Miguel Fortin
	TECH20711  - Développement d'applications d'affaires
*/


/*
 * Permet de créer l'arbre DOM représentant le corps de la fenêtre modale d'aide et le retourne.
 * Ce dernier est sous forme d'une liste de définitions (Élément HTML "dl") renfermant la liste des fonctionnalités.
 * Les termes (les éléments "dt" de la liste) représentent les actions de l'utilisateurs alors que leurs définitions
 * (les éléments "dd" de la liste)  représentent le résultat escompté.
*/

const getCorpsFenetreAide = () => {
	let fonctionnalites = [
		{
			action: "Clic sur le mois",
			resultat: "Permet de comparer le total des ventes réalisées au cours du mois de l'année sélectionnés à celui du même mois des années précédentes."
		},
		{
			action: "Clic sur l'année",
			resultat: "Permet de comparer le total des ventes réalisées au cours de l'année sélectionnée à celui des années précédentes"
		},
		{
			action: "Clic sur une date précise",
			resultat: "Permet de comparer le total des ventes réalisées au cours de cette date à celui de la même date des années précédentes"
		},
	];

	let aide = document.getElementById("corps-aide")
	let dl = document.createElement("dl")
	let dt = document.createElement("dt")
	let dd = document.createElement("dd")

	for (element of fonctionnalites) {
		dt = document.createElement("dt")
		dd = document.createElement("dd")
		dt.innerText = element.action
		dd.innerText = element.resultat
		dl.appendChild(dt)
		dl.appendChild(dd)
	}
	aide.appendChild(dl)
};


window.addEventListener("load", () => {
	getCorpsFenetreAide()
});