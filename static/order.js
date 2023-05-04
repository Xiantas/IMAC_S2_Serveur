"use strict";

function onLoad() {
    console.log("debut script");
    const partsHolder = document.getElementsByTagName("parts")[0];

    let data = await fetch("/order");
    let parts = await data.json();

    const partsList = document.createElement("div");
    for (const part of parts.list) {
        let partOfList = document.createElement("div");
        partOfList.innerHTML = `<input type=\"checkbox\" id=\"${part}\" name=\"${part}\"><label for=\"${part}\">${part}</label>`;
        partsList.appendChild(partOfList);
    }
    partsHolder.appendChild(partsList);
    console.log("fin script");
}

onLoad();
