const toDoForm = document.querySelector(".js-toDoForm"),
toDoInput = toDoForm.querySelector("input"),
toDoList = document.querySelector(".js-toDoList");

let toDos = [];
var currentUserId = 0

function loadId() {
  const currentUserId = localStorage.getItem("currentUserId");
  return(currentUserId)
}

function deleteToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  delTodoApi(li.id, USERID)
  const cleanToDos = toDos.filter(function(toDo) {
    return toDo.id !== parseInt(li.id);
  });
  toDos = cleanToDos;
}

function paintToDo(id, todo) {
  const li = document.createElement("li");
  const delBtn = document.createElement("button");
  const span = document.createElement("span");
  const newId = id;
  delBtn.innerText = "X";
  delBtn.addEventListener("click", deleteToDo);
  span.innerText = todo;
  li.appendChild(delBtn);
  li.appendChild(span);
  li.id = newId;
  console.log(todo,id)
  toDoList.appendChild(li);
  const toDoObj = {
    text: todo,
    id: newId
  };
  toDos.push(toDoObj);
  
}
function handleSubmit(event) {
  event.preventDefault();
  const currentValue = toDoInput.value;
  if(currentValue == "logout") {
    console.log("test logout")
    localStorage.removeItem(ID_LS)
    localStorage.removeItem(USER_LS)
    location.reload()
  }else{
    const nextId = toDos[0] == null ? 1 : toDos[toDos.length-1].id+1
    paintToDo(nextId, currentValue);
    addTodoApi(nextId, USERID, currentValue);
    toDoInput.value = "";
  }
}

function init() {
  USERID = loadId()
  readTodoApi(USERID)
  toDoForm.addEventListener("submit", handleSubmit);
}
init();

function addTodoApi(id, userId, todo) {
  fetch(`${BACKEND_URL}addTodo?id=${id}&userId=${userId}&userId=${userId}&todo=${todo}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

function delTodoApi(id, userId) {
  fetch(`${BACKEND_URL}delTodo?id=${id}&userId=${userId}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function editTodoApi(id, userId, text) {
  fetch(`${BACKEND_URL}editTodo?id=${id}&userId=${userId}&text=${text}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function todoComplete(id, userId, complete) {
  fetch(`${BACKEND_URL}todoComplete?id=${id}&userId=${userId}&complete=${complete}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

function readTodoApi(userId) {
  fetch(
    `${BACKEND_URL}readTodo?userId=${userId}`
      ).then(function(response) {
        return response.json();
      }).then(function(json) {
        var i;
        for (i = 1; i <= json.lastid; i++) {
          if(json[i]!=null){
            console.log(json[i],i)
            paintToDo(json[i].id, json[i].todo);
          }
        }
    })
}
