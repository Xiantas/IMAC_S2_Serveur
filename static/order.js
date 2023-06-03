"use strict";

let sessionInfo;

try {
    sessionInfo = JSON.parse(window.name);
    if (!sessionInfo.hasOwnProperty("BIGGIMAC")) {
        sessionInfo = {
            BIGGIMAC: true,
            email: undefined,
            pw: undefined,
            order: []};
    }

} catch (_) {
    sessionInfo = {
        BIGGIMAC: true,
        email: undefined,
        pw: undefined,
        order: []};
}

let data = await fetch("/ingres_available");
let parts = await data.json();

function onLoad() {
    const partsHolder = document.getElementsByTagName("parts")[0];

    const partsList = document.createElement("div");
    partsList.setAttribute("id", "container");
    for (const part of parts) {
        let partOfList = document.createElement("div");
        partOfList.innerHTML = `<label><input type=\"checkbox\" id=\"${part[0]}\" name=\"${part[0]}\">${part[1]} : ${part[2]}€</label>`;
        partsList.appendChild(partOfList);
    }
    partsHolder.appendChild(partsList);
}

function passerCommande() {
    sessionInfo.order = [];
    const boxes = document.getElementById("container").getElementsByTagName("input");
    for (const box of boxes) {
        if (box.checked) {
            sessionInfo.order.push(box.id);
        }
    }
    const send = JSON.stringify(sessionInfo.order);
    window.name = JSON.stringify(sessionInfo);
    fetch("/order.html", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: window.name
    })
        .then(_ => window.location.href = "/orderSummary.html");
}

onLoad();
const bouton = document.getElementById("leBouton");
bouton.addEventListener("click", passerCommande);
