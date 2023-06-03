"use strict";

function onLoad() {
    const partsHolder = document.getElementsByTagName("parts")[0];
    console.log(window.name)
    const commande = JSON.parse(window.name);
    console.log(commande);


    const partsList = document.createElement("ul");
    for (const ingre of commande.taken) {
        let partOfList = document.createElement("li");
        partOfList.innerHTML = commande.infos.find(e => {return e[0] == ingre;})[1];
        partsList.appendChild(partOfList);
    }
    partsHolder.appendChild(partsList);
}

function annulerCommande() {
    bouton.innerHTML = "Trop tard, la commande est déjà passée";
}

const bouton = document.getElementById("leBouton");
bouton.addEventListener("click", annulerCommande);

onLoad();
