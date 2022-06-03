// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-analytics.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  setPersistence,
  browserLocalPersistence, //Usuario recordado hasta que haga sign out
  browserSessionPersistence, //Usuario recordado hasta cerrar la pagina
  inMemoryPersistence, //Usuario borrado al refrescar pagina
  onAuthStateChanged,
} from "https://www.gstatic.com/firebasejs/9.8.1/firebase-auth.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCBQUpEXLHA3ozDxBqFmY4Mjpkdowha7gM",
  authDomain: "itbank-3edb0.firebaseapp.com",
  projectId: "itbank-3edb0",
  storageBucket: "itbank-3edb0.appspot.com",
  messagingSenderId: "102444894055",
  appId: "1:102444894055:web:6f94fd722fd23046a751c2",
  measurementId: "G-2MB6CQWJ18",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth();

(function () {
  document.getElementById("navbar").innerHTML = `
    <div class='nav-logo'> 
      <a href='home.html'> 
        <img class='logo-img' src='../public/img/ITBANK-Blanco.png'/> 
      </a> 
    </div> 
    <div class='nav-links'> 
      <ul class='link-list'> 
        <li class='nav-link'> 
          <a class='link' href='home.html'>Home</a> 
        </li> 
        <li class='nav-link'> 
          <a class='link' href='#'>Turnos</a> 
        </li> 
        <li class='nav-link'> 
          <a class='link' href='#'>Personas</a> 
        </li>
      </ul>
    </div>
    <div class='nav-usuario'> 
      <a class='nav-user' href='user.html' id='nav-username'>....
        <i class='fa-solid fa-user'></i>
      </a>
      <div class='nav-menu'>
        <span class='menu-line1'></span>
        <span class='menu-line2'></span>
        <span class='menu-line3'></span>
      </div>
    </div>
    `;
  document.getElementById("footer").innerHTML = `
    <p class='col-md-4 mb-0 text-muted'>© 2022 Random, Inc.</p>
    <ul class='nav col-md-4 justify-content-end'>
      <li class='nav-item'>
        <a href='home.html' class='nav-link px-2 text-muted'>Home</a>
      </li>
      <li class='nav-item'>
        <a href='user.html' class='nav-link px-2 text-muted'>Usuario</a>
      </li>
      <li class='nav-item'>
        <a href='#' class='nav-link px-2 text-muted'>Turnos</a>
      </li>
      <li class='nav-item'>
        <a href='#' class='nav-link px-2 text-muted'>FAQs</a>
      </li>
      <li class='nav-item'>
        <a href='#'' class='nav-link px-2 text-muted'>About</a>
      </li>
    </ul>
    `;
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // User is signed in, see docs for a list of available properties
        // https://firebase.google.com/docs/reference/js/firebase.User
        document.querySelector("#nav-username").innerHTML = auth.currentUser.email.split('@')[0] + "<i class='fa-solid fa-user'></i>"; // En main.css .nav-usuario define limite de 15 caracteres sin problemas
        console.log("User signed in");
      } else {
        // User is signed out
        console.log("User signed out");
      }
    })
})();

//Detecta el html activo y aplica diferente codigo dependiendo de eso
const htmlDetect = document.querySelector("#htmlID");
switch (htmlDetect.textContent) {
  //------------------------------------------------------------------------
  case "user":
    const form1 = document.querySelector("#registerForm");
    const form2 = document.querySelector("#loginForm");
    const form3 = document.querySelector("#mainForm");

    const userRegister = document.querySelector("#register-name");
    const passwordRegister = document.querySelector("#register-pass");
    const userLogin = document.querySelector("#login-name");
    const passwordLogin = document.querySelector("#login-pass");

    const rememberReg = document.querySelector("#checkReg");
    const rememberLog = document.querySelector("#checkLog");
    const submitReg = document.querySelector("#register-submit");
    const submitLog = document.querySelector("#login-submit");
    const botonLog = document.querySelector("#main-login-btn");
    const botonReg = document.querySelector("#main-register-btn");

    botonLog.addEventListener("click", () => {
      form3.style.display = "none";
      form2.style.display = "block";
    });

    botonReg.addEventListener("click", () => {
      form3.style.display = "none";
      form1.style.display = "block";
    });

    //Register button
    submitReg.addEventListener("click", (e) => {
      e.preventDefault();
      if (verifyUserPass(userRegister.value, passwordRegister.value)) {
        createUserWithEmailAndPassword(
          auth,
          userRegister.value + "@blablaestafas.com",
          passwordRegister.value
        )
          .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            console.log("Register complete");
            if (rememberReg.checked == true) {
              setPersistence(auth, browserLocalPersistence);
            }
            else {
              setPersistence(auth, browserSessionPersistence);
            }
            window.location.href = "home.html";
          })
          .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            if (errorCode == "auth/email-already-in-use") {
              alert("Ya existe una cuenta con ese usuario");
            }
            console.log(
              userRegister.value +
                "@blablaestafas.com" +
                "\n" +
                passwordRegister.value +
                "\n" +
                errorMessage +
                "\n" +
                errorCode
            );
          });
      }
    });

    //Login button
    submitLog.addEventListener("click", (e) => {
      e.preventDefault();
      if (verifyUserPass(userLogin.value, passwordLogin.value)) {
        signInWithEmailAndPassword(
          auth,
          userLogin.value + "@blablaestafas.com",
          passwordLogin.value
        )
          .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            console.log("Login complete");
            if (rememberLog.checked == true) {
              setPersistence(auth, browserLocalPersistence);
            }
            else {
              setPersistence(auth, browserSessionPersistence);
            }
            window.location.href = "home.html";
          })
          .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            if (errorCode == "auth/email-already-in-use") {
              alert("Ya existe una cuenta con ese usuario");
            }
            console.log(
              userRegister.value +
                "@blablaestafas.com" +
                "\n" +
                passwordRegister.value +
                "\n" +
                errorMessage +
                "\n" +
                errorCode
            );
          });
      }
    });

    function verifyUserPass(username, password) {
      if (username == "" || password == "") {
        alert("Debes ingresar un valor");
        return false;
      }
      if (username.match(/[@]/)) {
        alert("Tu usuario no puede contener '@'");
        return false;
      }
      if (password.length < 8) {
        alert("Tu contraseña debe tener al menos 8 caracteres");
        return false;
      }
      if (!password.match(/[$@!%*#?&]/)) {
        alert("Tu contraseña debe tener al menos 1 caracter especial '$@!%*#?&'");
        return false;
      }
      if (!password.match(/[A-Z]/)) {
        alert("Tu contraseña debe tener al menos 1 letra mayuscula");
        return false;
      }
      if (!password.match(/[0-9]/)) {
        alert("Tu contraseña debe tener al menos 1 numero");
        return false;
      }
      if (!password.match(/[a-z]/)) {
        alert("Tu contraseña debe tener al menos 1 letra minuscula");
        return false;
      }
      if (password.includes(username)) {
        alert("Tu contraseña no puede contener tu usuario");
        return false;
      }

      //FALTA VERIFICAR SI EL USUARIO YA ESTA EN USO

      return true;
    }
    break;

  //------------------------------------------------------------------------
  case "home":
    console.log("???");
    break;
  //------------------------------------------------------------------------
  case "saldo":
    console.log("???");
    break;

  //------------------------------------------------------------------------
  case "gastos":
    let nombre = document.querySelector("#nombre");
    let gasto = document.querySelector("#gasto");
    let botonGasto = document.querySelector("#boton-gasto");
    let padreColumna = document.querySelector("#padre-columna");
    let gastosDisplay = document.querySelector("#gastos-display");


    let sumaGastosEntero = 0;
    let sumaGastosDecimal = 0;

    botonGasto.addEventListener("click", (e) => {
      let nombreGasto = nombre.value;
      let gastoValor = gasto.value;
      if (gastoValor.match(/^[0-9]+$/)) { //En caso de no poner coma
        updateSumaGastos(parseFloat(gastoValor), 0);
        crearGasto(nombreGasto, gastoValor);
      }
      else {
        if (gastoValor.match(/^[0-9]+([,.][0-9]{1,2})?$/)) { //En caso de que ingrese numero con 1-2 digitos despues de la coma
          gastoValor = gastoValor.replace(',', '.'); //Poniendolo con punto en vez de coma para que el sistema funcione
          updateSumaGastos(parseFloat(gastoValor.split('.')[0]), parseFloat((gastoValor.split('.')[1] + "00").slice(0, 2)));
          crearGasto(nombreGasto, gastoValor);
        }
        else {
          alert("Debe ingresar un numero");
        }
      }
    });

    function crearGasto(name, valor) {
      let nuevaColumna = document.createElement("div");
      nuevaColumna.classList.add("columnas");
      nuevaColumna.classList.add("columnas-elementos");
      let valorDisplay = "" + valor.replace('.', ',');
      if (valor.match(/^[0-9]+$/)) {
        valorDisplay += ",00";
      }
      else {
        if (valor.match(/^[0-9]+([,.][0-9]{1})?$/)) {
          valorDisplay += "0";
        }
      }
      let valorColumna = `<p> ${name}</p><p>$ ${valorDisplay}</p>`;

      nuevaColumna.addEventListener("click", (e) => {
        updateSumaGastos(-parseFloat(nuevaColumna.innerHTML.split('$')[1].split(',')[0]), -parseFloat((nuevaColumna.innerHTML.split('$')[1].split(',')[1].split('<')[0] + "00").slice(0, 2)));
        nuevaColumna.remove();
      });

      nuevaColumna.innerHTML = valorColumna;
      padreColumna.appendChild(nuevaColumna);
    }

    function updateSumaGastos(entero, decimal) {
      sumaGastosEntero += entero;
      if (sumaGastosDecimal + decimal > 100) {
        sumaGastosDecimal += decimal - 100;
        sumaGastosEntero += 1;
      }
      else {
        if (sumaGastosDecimal + decimal < 0) {
          sumaGastosDecimal += decimal + 100;
          sumaGastosEntero -= 1;
        }
        else {
          sumaGastosDecimal += decimal;
        }
      }

      let displayOutput = sumaGastosEntero + "," + ("00" + sumaGastosDecimal).slice(-2); //Poniendolo con coma en vez de punto y acortando a 2 decimales para mostrarlo a pantalla
      gastosDisplay.innerHTML = "$" + displayOutput;
    }

    break;
}

// Responsive MENU //

let navBtn = document.querySelector(".nav-menu");
let navMenu = document.querySelector(".nav-links");

navBtn.addEventListener("click", () => {
  navBtn.classList.toggle("close-menu");
  navMenu.classList.toggle("nav-links-active");
});
