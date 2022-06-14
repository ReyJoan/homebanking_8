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

// https://firebase.google.com/docs/web/setup#available-libraries
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

//Crear Header y Footer
(function () {
  document.getElementById("navbar").innerHTML = `
    <div class='nav-logo'> 
      <a href='home.html'> 
        <img class='logo-img' src='../public/img/ITBANK-Blanco.png'/> 
      </a> 
    </div> 
    <div class='nav-links'> 
      <ul class='link-list'>
        <li class='nav-link nav-link-usuario'> 
          <a class='nav-link-user link' href='user.html' id='nav-link-username'>
            <i class='fa-solid fa-user'></i>
            ....
          </a>
        </li> 
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
      // En main.css .nav-usuario define limite de 15 caracteres sin problemas
      console.log("User signed in");
      document.querySelector("#nav-username").innerHTML = auth.currentUser.email.split('@')[0] + "<i class='fa-solid fa-user'></i>";
      document.querySelector("#nav-link-username").innerHTML = "<i class='fa-solid fa-user'></i>" + auth.currentUser.email.split('@')[0];
    } else {
      // User is signed out
      console.log("User signed out");
      document.querySelector("#nav-username").innerHTML = "Usuario" + "<i class='fa-solid fa-user'></i>";
      document.querySelector("#nav-link-username").innerHTML = "<i class='fa-solid fa-user'></i>" + "Usuario";
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
          userRegister.value + "@ignore.us",
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
              "@ignore.us" +
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
          userLogin.value + "@ignore.us",
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
              "@ignore.us" +
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
      if (username.match(/[@ ]/)) {
        alert("Tu usuario no puede contener ni espacio ni '@'");
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
 
  case "saldo":
    let valor = document.getElementById('saldo')
    console.log(valor.innerHTML)
    break;

  //------------------------------------------------------------------------
  case "home":
    const url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

    function boxDolar(id, dataIndex, Dolar){
      fetch(url)
        .then(data => data.json())
        .then(data => {
          let boxElement = document.querySelector(id)
          boxElement.innerHTML = ` <h3 class="titulo-D"><b>${Dolar}</b></h3>
          <div class="Box-Content">  
            <p><b>Compra</b>:</p><p class="values">$${data[dataIndex].casa.compra}</p>
            <p><b>Venta</b>:</p><p class="values">$${data[dataIndex].casa.venta}</p>
          </div>`
          console.log(data)
        })
        .catch(err => console.log(err))
    }
    
    boxDolar('#Dolar-Oficial', 0, "Dólar Oficial");
    boxDolar('#Dolar-Bolsa', 4, 'Dólar Bolsa');
    boxDolar("#Dolar-Cont", 3, 'Dólar Contado');
    boxDolar("#Dolar-Soli", 7, 'Dólar Solidario');
    
    // Esto agrega la opcion de comprar dólares llevandonos a un link en otra ventan
    const btnBuy = document.querySelector('#Buy-D');
    btnBuy.addEventListener('click', ()=>{
      window.location.href='home.html';
    })
    break;

  //------------------------------------------------------------------------
  case "gastos":
    let nombre = document.querySelector("#nombre");
    let gasto = document.querySelector("#gasto");
    let botonGasto = document.querySelector("#boton-gasto");
    let padreColumna = document.querySelector("#padre-columna");
    let gastosDisplay = document.querySelector("#gastos-display");
    let distribucionDisplay = document.querySelector("#distribucion-display");


    let sumaGastosEntero = 0;
    let sumaGastosDecimal = 0;
    let cantidadEntradas = 0;

    botonGasto.addEventListener("click", (e) => {
      let nombreGasto = nombre.value;
      let gastoValor = gasto.value;
      if (gastoValor.match(/^[0-9]+$/)) { //En caso de no poner coma
        cantidadEntradas++;
        gastoValor = gastoValor + ".00"
        updateSumaGastos(gastoValor);
        crearGasto(nombreGasto, gastoValor);
      }
      else {
        if (gastoValor.match(/^[0-9]+([,.][0-9]{1})?$/)) { //En caso de que ingrese numero con 1 digitos despues de la coma
          cantidadEntradas++;
          gastoValor = gastoValor.replace(',', '.') + "0"; //Poniendolo con punto en vez de coma y metiendole un 0 al final para que el sistema funcione
          updateSumaGastos(gastoValor);
          crearGasto(nombreGasto, gastoValor);
        }
        else {
          if (gastoValor.match(/^[0-9]+([,.][0-9]{2})?$/)) { //En caso de que ingrese numero con 2 digitos despues de la coma
            cantidadEntradas++;
            gastoValor = gastoValor.replace(',', '.'); //Poniendolo con punto en vez de coma para que el sistema funcione
            updateSumaGastos(gastoValor);
            crearGasto(nombreGasto, gastoValor);
          }
          else {
            alert("Debe ingresar un numero");
          }
        }
      }
    });

    function crearGasto(name, valor) {
      let nuevaColumna = document.createElement("div");
      nuevaColumna.classList.add("columnas");
      nuevaColumna.classList.add("columnas-elementos");
      let valorDisplay = "" + valor.replace('.', ','); //Poniendolo con coma en vez de punto para la lectura
      let valorColumna = `<p>${name}</p><p>$ ${valorDisplay}</p>`;
      
      let valorEntrada = valor;
      nuevaColumna.addEventListener("click", (e) => {
        cantidadEntradas--;
        updateSumaGastos("-" + valorEntrada);
        nuevaColumna.remove();
      });

      nuevaColumna.innerHTML = valorColumna;
      padreColumna.appendChild(nuevaColumna);
    }

    function updateSumaGastos(valor) {
      let entero = parseFloat(valor.split('.')[0]);
      let decimal = (valor[0] == '-' ? -1 : 1) * parseFloat((valor.split('.')[1] + "00").slice(0, 2));
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
      if (cantidadEntradas == 0) {
        displayOutput = "0,00";
      }
      else {
        let tempCountD = Math.floor(((sumaGastosEntero % cantidadEntradas) * 100) / cantidadEntradas) + Math.floor(sumaGastosDecimal / cantidadEntradas);
        let tempCountE = Math.floor(sumaGastosEntero / cantidadEntradas);
        displayOutput = tempCountE + "," + ("00" + tempCountD).slice(-2);
      }
      distribucionDisplay.innerHTML = "$" + displayOutput;
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
  