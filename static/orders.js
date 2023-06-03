"use strict";

let data = await fetch("/orders");
const orders = (await data.json()).list;

data = await fetch("/ingres");
const ingres = await data.json();
console.log(ingres);
console.log(orders);
const ordersArray = [];

function onLoad() {
    const partsHolder = document.getElementsByTagName("parts")[0];

    const partsList = document.createElement("div");
    partsList.setAttribute("id", "container");
    for (let i = 0; i < orders.length;)
    {
        const id_order=orders[i][0];
        const orderContent = [];
        for (; i < orders.length && id_order==orders[i][0]; i++) {
            const nomIngre = ingres.find(e => e[0] == orders[i][3]);
            console.log(nomIngre);
            let nomIngre2=nomIngre[1];
            orderContent.push(nomIngre2);
        }
        console.log("orderContent :", orderContent);
        
        ordersArray.push([id_order,orders[i-1][1],orders[i-1][2],orderContent.join(", "),orders[i-1][4]]); 
    }
    console.log(ordersArray);

    for(const [id_order,nom_client,time,ingredients,adresse_client] of ordersArray)
    {
        let partOfList = document.createElement("div");
        partOfList.innerHTML = `<label><input type="checkbox" id="${id_order}" name="${id_order}">n°${id_order} à ${time} à livrer au ${adresse_client} à ${nom_client}: ${ingredients}</label>`;
        partsList.appendChild(partOfList);        
    }
    partsHolder.appendChild(partsList);
}

function supprimmerCommandes() {
    let suppressions = [];
    const boxes = document.getElementById("container").getElementsByTagName("input");
    for (const box of boxes) {
        if (box.checked) {
            suppressions.push(box.id);
        }
    }

    const send = JSON.stringify(suppressions);
    window.name = send;

    fetch("/orders", {
        method: "DELETE",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: send
    })
        .then(_ => window.location.replace("/orders.html"));
}

const bouton = document.getElementById("leBouton");
bouton.addEventListener("click", supprimmerCommandes);

onLoad();
