const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const USER_LS = "currentUser",
    SHOWING_CH = "showing";

function paintGreeting(text) {
    form.classList.remove(SHOWING_CH);
    greeting.classList.add(SHOWING_CH);
    greeting.innerHTML = `Hello ${text}`;
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        
    }else{
        paintGreeting(currentUser);
    }
}

function init() {
    loadName();
}
init();