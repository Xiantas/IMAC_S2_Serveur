"use strict";

let sessionInfo;

try {
    sessionInfo = JSON.parse(window.name);
    console.log("ok");
    if (!sessionInfo.hasOwnProperty("BIGGIMAC")) {
        console.log("unreadable");
        sessionInfo = {
            BIGGIMAC: true,
            email: undefined,
            pw: undefined,
            order: []};
    }

} catch (error) {
    console.log("not ok");
    sessionInfo = {
        BIGGIMAC: true,
        email: undefined,
        pw: undefined,
        order: []};
}

const data = await fetch("/ingres");
const ingres = await data.json();

function onLoad() {
    const partsHolder = document.getElementsByTagName("parts")[0];


    const partsList = document.createElement("ul");
    console.log(sessionInfo.order);
    for (const ingre of sessionInfo.order) {
        let partOfList = document.createElement("li");
        let truc = ingres.find(e => {return e[0] == ingre;})[1];
        console.log(truc);
        partOfList.innerHTML = truc;
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
