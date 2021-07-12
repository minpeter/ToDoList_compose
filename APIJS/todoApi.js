
const userName = "testUSER", passwordH = "userPW", email = "test@email.com"

const toDoForm = document.querySelector(".js-toDoForm"),
toDoInput = toDoForm.querySelector("input"),
toDoList = document.querySelector(".js-toDoList");

// const TODOS_LS = "toDos";

let toDos = [];

function deleteToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  delTodoApi(li.id, 1)
  const cleanToDos = toDos.filter(function(toDo) {
    return toDo.id !== parseInt(li.id);
  });
  toDos = cleanToDos;
  // saveToDos();
  //delTodo()
}

// function saveToDos() {
//   localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
// }

function paintToDo(todo, id) {
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
  paintToDo(currentValue, toDos.length + 1);
  addTodoApi(currentValue);
  //위에 toDos.length + 1이랑 db id 와 차이가 발생해 오류 발생가능 (맨뒤에 id를 삭제할경우)
  toDoInput.value = "";
}


// function loadToDos() {
//   const loadedToDos = localStorage.getItem(TODOS_LS);
//   console.log(loadedToDos)
//   if (loadedToDos !== null) {
//     const parsedToDos = JSON.parse(loadedToDos);
//     console.log(parsedToDos)
//     parsedToDos.forEach(function(toDo) {
//       paintToDo(toDo.text);
//     });
//   }
// }

function init() {
  loadToDos();
  toDoForm.addEventListener("submit", handleSubmit);
}
init();

function addTodoApi(todo) {
  fetch(`http://localhost:7878/addTodo?userId=1&todo=${todo}&endday=1&importance=1`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

function delTodoApi(id, userId) {
  fetch(`http://localhost:7878/delTodo?id=${id}&userId=${userId}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function editTodoApi(id, userId, text) {
  fetch(`http://localhost:7878/editTodo?id=${id}&userId=${userId}&editSel=1&text=${text}`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}
function todoComplete(id, userId) {
  fetch(`http://localhost:7878/todoComplete?id=${id}&userId=${userId}&tf=1`)
  .then((response) => response.json())
  .then((data) => console.log(data));
}

function readTodoApi(userId) {
  return fetch(`http://localhost:7878/readTodo?userId=${userId}`)
 .then((response) => response.json())
 .then((data) => {return(data)});
}

async function loadToDos() {
  const loadedToDos = await readTodoApi(1)
  loadedToDos.forEach(function(toDo) {
    paintToDo(toDo.todo, toDo.id);
  });
}
