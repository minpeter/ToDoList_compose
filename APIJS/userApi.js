const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const TESTPW = "testpw",
    SHOWING_CH = "showing";

const USER_LS = "currentUser",
    ID_LS = "currentUserId";

const BACKEND_URL = "http://minpeter.ml:8787/"
//"http://localhost:7878/"

function handleSubmit(event) {
    // event.preventDefault();
    const currentValue = input.value;
    saveName(currentValue);
    location.reload()
    //dd
}

function askForName() {
    form.classList.add(SHOWING_CH);
    form.addEventListener("submit",handleSubmit);
}

function paintGreeting(text) {
    form.classList.remove(SHOWING_CH);
    greeting.classList.add(SHOWING_CH);
    //dd
    greeting.innerHTML = `Hello ${text}`;
}

function addUserApi(userName) {
    fetch(`${BACKEND_URL}addUser?userName=${userName}&password=${TESTPW}`)
    .then((response) => response.json())
    .then((data) => console.log(data));
    location.reload()
  }

function loginApi(userName) {
    fetch(
    `${BACKEND_URL}login?userName=${userName}&password=${TESTPW}`
    ).then(function(response) {
        return response.json();
    }).then(function(json) {
        if(json.userid!=null){
        saveId(json.userid)
        console.log(`${json.msg} userid : ${json.userid}`)
        location.reload()
        }else{
        console.log(json.msg)
        addUserApi(userName)
        }
    })
}


function saveId(text) {
    localStorage.setItem(ID_LS, text);
}
function saveName(text) {
    localStorage.setItem(USER_LS, text);
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        askForName();
    }else{
        paintGreeting(currentUser);
        const currentUserId = localStorage.getItem(ID_LS);
        if(currentUserId === null){
            loginApi(currentUser);
        }
        //dd
    }
}

function init() {
    loadName();
}
init();
