"use strict";

let data = await fetch("/ingres_available"); // récupère la liste des ingrédients à la route /order sur le serv.py
let parts = await data.json();

// devrait créer la liste des éléments à checker sur la page /order.html et l'afficher ; ouvert sur le server.py quand on va sur /order.html 
function onLoad() {
    const partsHolder = document.getElementsByTagName("parts")[0];

    const partsList = document.createElement("div");
    partsList.setAttribute("id", "container");
    for (const part of parts) {
        let partOfList = document.createElement("div");
        partOfList.innerHTML = `<input type=\"checkbox\" id=\"${part[0]}\" name=\"${part[0]}\"><label=\"${part[0]}\">${part[1]} : ${part[2]}€</label>`;
        partsList.appendChild(partOfList);
    }
    partsHolder.appendChild(partsList);
}

// lancée quand on appuie sur le bouton , créer la liste d'id d'ingrédients checkée
function passerCommande() {
    let ingredients = [];
    const boxes = document.getElementById("container").getElementsByTagName("input");
    for (const box of boxes) {
        if (box.checked) {
            ingredients.push(box.id);
        }
    }
    const send = JSON.stringify(ingredients);
    window.name = JSON.stringify({
        infos: parts,
        taken: ingredients
    });
    // renvoit sur le server.py avec la méthode post 
    fetch("/order.html", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: send // donnée envoyée
    })
        .then(_ => window.location.href = "/orderSummary.html");
}

onLoad();
const bouton = document.getElementById("leBouton");
bouton.addEventListener("click", passerCommande);
