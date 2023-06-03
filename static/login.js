"use strict";

async function login() {
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

    const mail = document.getElementById("mail").value;
    const pw = document.getElementById("pw").value;

    sessionInfo.email = mail;
    sessionInfo.pw = pw;

    const data = await fetch("/login.html", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: sessionInfo
    });

    console.log(data);
    const response = await data.json();
    console.log("b");

    console.log(response)

}

const submit = document.getElementById("submit");
submit.addEventListener("click", login);
