var countriesStateCode = {}

function createNode(name, value) {
    const option = document.createElement("option");
    option.setAttribute("value", value);
    option.innerText = name;
    return option;
}

let countryFlag;

window.onload = function () {
    countryFlag = document.querySelector("#country-flag");

    fetch("https://restcountries.com/v3.1/all").then(response => response.json()).then(data => {
        const selectField = document.querySelector("select#country");
        selectField.innerHTML = ""
        selectField.appendChild(createNode("None", ""));
        const cc = data.map(d => {
            const name = d.name.common;
            const flag = d.flags.png;
            // const countrycode = d.idd.root + (d.idd.suffixes ? d.idd.suffixes[0] : "");

            const countryCodes = [];
            if (d.idd.suffixes) {
                d.idd.suffixes.forEach(idx => {
                    countryCodes.push(d.idd.root + idx)
                });
            }

            selectField.appendChild(createNode(name, name));
            countriesStateCode[name] = {
                flag: flag,
                countryCodes: countryCodes
            }
        })
        console.log(countriesStateCode);
    })
}

function changecat(value) {
    if (value.length == 0) document.getElementById("country_code").innerHTML = "<option>None</option>";
    else {
        const flag = countriesStateCode[value].flag;
        const codes = countriesStateCode[value].countryCodes
        var catOptions = "";

        for (index in codes) {
            catOptions += "<option>" + codes[index] + "</option>";
        }

        countryFlag.setAttribute("src", flag)
        document.getElementById("country_code").innerHTML = catOptions;
    }
}