/*const boton = document.querySelector('p');

boton.addEventListener('click', updateName);

function updateName() {
    let name = prompt ("Ingresar un nuevo jugador");
    boton.textContent = "Player 1: " + name;
}*/

const form1 = document.querySelector('.register-form');
const form2 = document.querySelector('.logIn-form');
const form3 = document.querySelector('.main-form');

const user = document.querySelector('#user');
const password = document.querySelector('#clav');
const botonFormR = document.querySelector('#btn-registro');
const botonLog = document.querySelector('#Log');
const botonReg = document.querySelector('#Reg');
const botonEntry = document.querySelector('#entry');

const storedToDos = localStorage.getItem('User');


botonLog.addEventListener('click', ()=>{
    form3.style.display = 'none';
    form2.style.display = "block";
})

botonReg.addEventListener('click', ()=>{
    form3.style.display = 'none';
    form1.style.display = "block";
})

function guardarDatos (){
    if (user.value == "" || password.value == "") {
        alert('Debes ingresar un valor');
    }
    else {
        let valorUsuario = user.value;
        let valorPassword = password.value;
        userData = [valorUsuario, valorPassword];
        localStorage.setItem("User", JSON.stringify(userData));
        form1.style.display = 'none';
        form2.style.display = "block";
    }
    return userData
}

botonFormR.addEventListener('click',(e)=>{
    e.preventDefault();
    // Podríamos usar un while mas adelante
    // if (user.value == "" || password.value == "") {
    //     alert('Debes ingresar un valor');
    // }
    // else {
    //     let valorUsuario = user.value;
    //     let valorPassword = password.value;
    //     keys.push(valorUsuario);
    //     keys.push(valorPassword);
    //     form1.style.display = 'none';
    //     form2.style.display = "block";
    // }
    // return keys
    // window.location.href = 'file:///C:/Users/Lenovo/Desktop/ITBA/homebanking_8/views/home.html' Link para enlazar a otras paginas de forma local
    guardarDatos()
}) 

botonEntry.addEventListener('click', (e)=> {
    e.preventDefault();
    guardarDatos();
    let valorUsuario = user.value;
    let valorPassword = password.value;
    if (valorUsuario == storedToDos[0] && valorPassword == storedToDos[1]) {
      window.location.href = "home.html";  
    }
})


console.log(JSON.parse(storedToDos)) 
for (let i = 0; i < localStorage.length; i++) {
    let key = localStorage.key(i);
    let valor = localStorage.getItem(key);
    console.log(key);
    console.log(valor);
}








