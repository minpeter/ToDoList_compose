const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const TESTPW = "testpw",
    SHOWING_CH = "showing";

const USER_LS = "currentUser",
    ID_LS = "currentUserId";

function handleSubmit(event) {
    event.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue);
    saveName(currentValue);
    loginJson(currentValue);
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
        loginApi(currentUser);
    }
}

function init() {
    loadName();
}
init();


function addUserApi(userName) {
    fetch(`http://localhost:7878/addUser?userName=${userName}&password=${TESTPW}`)
    .then((response) => response.json())
    .then((data) => console.log(data));
  }

  function loginApi(userName) {
      fetch(
        `http://localhost:7878/login?userName=${userName}&password=${TESTPW}`
      ).then(function(response) {
          return response.json();
      }).then(function(json) {
          if(json.userid!=null){
            saveId(json.userid)
              console.log(`${json.msg} userid : ${json.userid}`)
          }else{
              console.log(json.msg)
          }
      })
  }
  async function loginJson(name){
      await loginApi(name).forEach(function(msg) {
          saveId(msg.msg)
      })
  }
  
function saveId(text) {
    localStorage.setItem(ID_LS, text);
}
function saveName(text) {
    localStorage.setItem(USER_LS, text);
}