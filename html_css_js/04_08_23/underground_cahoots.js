"use strict";

let resultsDiv = document.querySelector("#information")


let getRequest = () => {

    axios.get("https://api.tfl.gov.uk/Line/Mode/tube/Status")
    .then((response) => {
        displayResult(response.data);
        // console.log(response);
    })
    .catch((err) => {
        console.error(err);
    });

}

let displayResult = (data) => {

for (let entry of data){

    const entryDiv = document.createElement("div");
    entryDiv.setAttribute("class", "entryDiv");
    const text = document.createTextNode(`Name: ${entry.name} | lineStatuses: ${entry.lineStatuses} | Status Desc: ${entry.lineStatuses[0].statusSeverityDescription}`);

    entryDiv.appendChild(text);
    resultsDiv.appendChild(entryDiv);

    }

}

// entry.lineStatuses[0].statusSeverityDescription;