const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const USER_LS = "currentUser",
    SHOWING_CH = "showing";

function saveName(text) {
    localStorage.setItem(USER_LS, text);
}

function handleSubmit() {
    event.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue);
    saveName(currentValue);
}

function askForName() {
    form.classList.add(SHOWING_CH);
    form.addEventListener("submit",handleSubmit);
}

function paintGreeting(text) {
    form.classList.remove(SHOWING_CH);
    greeting.classList.add(SHOWING_CH);
    greeting.innerHTML = `Hello ${text}`;
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        askForName();
    }else{
        paintGreeting(currentUser);
    }
}

function init() {
    loadName();
}
init();


function addTodoApi(userName) {
    fetch(`http://localhost:7878/addUser?userName=${userName}&passwordH=1&email=1`)
    .then((response) => response.json())
    .then((data) => console.log(data));
  }

  function login(userName) {
    fetch(`http://localhost:7878/login?userName=${userName}&passwordH=1`)
    .then((response) => response.json())
    .then((data) => console.log(data));
  }