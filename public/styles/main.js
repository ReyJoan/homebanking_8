/*const boton = document.querySelector('p');

boton.addEventListener('click', updateName);

function updateName() {
    let name = prompt ("Ingresar un nuevo jugador");
    boton.textContent = "Player 1: " + name;
}*/

const form1 = document.querySelector('.register-form');
const form2 = document.querySelector('.logIn-form');
const form3 = document.querySelector('.main-form');

// FORMULARIO REGISTER
const user = document.querySelector('#user');
const password = document.querySelector('#clav');
const botonFormR = document.querySelector('#btn-registro');
// FORMULARIO OPCION
const botonLog = document.querySelector('#Log');
const botonReg = document.querySelector('#Reg');
// FORMULARIO LOGIN
const userLogin = document.querySelector("#user-name");
const passLogin = document.querySelector("#user-pass");
const botonEntry = document.querySelector('#entry');

const storedToDos = localStorage.getItem('User');
let parsedValues = JSON.parse(storedToDos)

botonLog.addEventListener('click', ()=>{
    form3.style.display = 'none';
    form2.style.display = "block";
})

botonReg.addEventListener('click', ()=>{
    form3.style.display = 'none';
    form1.style.display = "block";
})

botonFormR.addEventListener('click',(e)=>{
    let valorUsuario = user.value;
    let valorPassword = user.value;
    e.preventDefault();
    if (valorUsuario == "" || valorPassword == "") {
        alert('Ingrese un valor en el campo');
    }else {
        userData = [valorUsuario, valorPassword];
        localStorage.setItem("User", JSON.stringify(userData));
        form1.style.display = 'none';
        form2.style.display = "block";
    }
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
}) 

botonEntry.addEventListener('click', (e)=> {
    e.preventDefault();
    let valor = localStorage.getItem("User");
    let valorParse = JSON.parse(valor);
    console.log(valorParse)
    let valorUsuario = userLogin.value;
    let valorPassword = passLogin.value;
    if (valorUsuario == valorParse[0] && valorPassword == valorParse[1]) {
        window.location.href = "home.html";  
    }else{
        alert('ERROR EN EL LOGIN, USUARIO INCORRECTO')
    }
})


