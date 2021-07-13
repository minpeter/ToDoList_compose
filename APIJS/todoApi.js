
const userName = "testUSER", passwordH = "userPW", email = "test@email.com"

const toDoForm = document.querySelector(".js-toDoForm"),
toDoInput = toDoForm.querySelector("input"),
toDoList = document.querySelector(".js-toDoList");

const USERID = 1

// const TODOS_LS = "toDos";

let toDos = [];

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
  // toDos[toDos.length-1].id+1
  // toDos[0] == null ? 1 : toDos[toDos.length-1].id+1
  const nextId = toDos[0] == null ? 1 : toDos[toDos.length-1].id+1
  paintToDo(nextId, currentValue);
  addTodoApi(nextId, USERID, currentValue);
  toDoInput.value = "";
}

function init() {
  readTodoApi(USERID)
  toDoForm.addEventListener("submit", handleSubmit);
}
init();

function addTodoApi(id, userId, todo) {
  fetch(`http://localhost:7878/addTodo?id=${id}&userId=${userId}&userId=1&todo=${todo}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

function delTodoApi(id, userId) {
  fetch(`http://localhost:7878/delTodo?id=${id}&userId=${userId}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function editTodoApi(id, userId, text) {
  fetch(`http://localhost:7878/editTodo?id=${id}&userId=${userId}&text=${text}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function todoComplete(id, userId, complete) {
  fetch(`http://localhost:7878/todoComplete?id=${id}&userId=${userId}&complete=${complete}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

// function readTodoApi(userId) {
//   return fetch(`http://localhost:7878/readTodo?userId=${userId}`)
//  .then((response) => response.json())
//  .then((data) => {return(data)});
// }

// async function loadToDos() {
//   const loadedToDos = await readTodoApi(USERID)
//   loadedToDos.forEach(function(toDo) {
//   paintToDo(toDo.id, toDo.todo);
//   });
// }

function readTodoApi(userId) {
  fetch(
    `http://localhost:7878/readTodo?userId=${userId}`
      ).then(function(response) {
          return response.json();
      }).then(function(json) {
        var i;
        for (i = 1; i <= json.lastid; i++) {
          console.log(json[i],i)
        }
      })
}