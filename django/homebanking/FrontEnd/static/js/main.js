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

//Detecta el html activo y aplica diferente codigo dependiendo de eso
const htmlDetect = document.querySelector("#htmlID");
switch (htmlDetect.textContent) {
  //------------------------------------------------------------------------
  case "user":
    const form2 = document.querySelector("#loginForm");
    const form3 = document.querySelector("#mainForm");

    const userLogin = document.querySelector("#login-name");
    const passwordLogin = document.querySelector("#login-pass");

    const submitLog = document.querySelector("#login-submit");
    const botonLog = document.querySelector("#main-login-btn");
    const botonReg = document.querySelector("#main-register-btn");
    const errorLog = document.querySelector("#errorLogin");

    botonLog.addEventListener("click", () => {
      form3.style.display = "none";
      form2.style.display = "block";
    });

    botonReg.addEventListener("click", () => {
      window.location.href = "../register/"
    });

    //Login button
    submitLog.addEventListener("click", (e) => {
      e.preventDefault();
      if (verifyLoginFields(userLogin.value, passwordLogin.value)) {
        let data = {
          csrfmiddlewaretoken: document.querySelector('[name="csrfmiddlewaretoken"]').value,
          username: userLogin.value,
          password: passwordLogin.value
        }
        let post = JSON.stringify(data)
        
        const url = "../user/"
        let xhr = new XMLHttpRequest()
        
        xhr.onreadystatechange = function() {
          if (xhr.readyState == XMLHttpRequest.DONE) {
            console.log(JSON.parse(xhr.responseText).success)
            if (JSON.parse(xhr.responseText).success == 'true') {
              window.location.href = JSON.parse(xhr.responseText).url;
            }
            else
            {
              errorLog.style.display = "block";
            }
          }
        }
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
        xhr.setRequestHeader("X-CSRFToken", document.querySelector('[name="csrfmiddlewaretoken"]').value);
        xhr.send(post);
      }
    });

    function verifyLoginFields(username, password) {
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

      return true;
    }
    break;

  //------------------------------------------------------------------------
  case "register":
    const submitReg = document.querySelector("#register-submit");
    const errorReg = document.querySelector("#errorRegister");
    const userRegister = document.querySelector("#register-name");
    const passwordRegister = document.querySelector("#register-pass");
    const fnameRegister = document.querySelector("#register-firstname");
    const lnameRegister = document.querySelector("#register-lastname");
    const dniRegister = document.querySelector("#register-dni");
    const dobRegister = document.querySelector("#register-dob");

    //Register button
    submitReg.addEventListener("click", (e) => {
      e.preventDefault();
      if (verifyRegisterFields(userRegister.value, passwordRegister.value, fnameRegister.value, lnameRegister.value, dniRegister.value, dobRegister.value)) {
        let data = {
          csrfmiddlewaretoken: document.querySelector('[name="csrfmiddlewaretoken"]').value,
          username: userRegister.value,
          password: passwordRegister.value,
          firstname: fnameRegister.value,
          lastname: lnameRegister.value,
          dni: dniRegister.value,
          dob: dobRegister.value
        }
        let post = JSON.stringify(data)
        
        const url = "../register/"
        let xhr = new XMLHttpRequest()
        
        xhr.onreadystatechange = function() {
          if (xhr.readyState == XMLHttpRequest.DONE) {
            console.log(JSON.parse(xhr.responseText).success)
            if (JSON.parse(xhr.responseText).success == 'true') {
              window.location.href = JSON.parse(xhr.responseText).url;
            }
            else
            {
              errorReg.style.display = "block";
            }
          }
        }
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
        xhr.setRequestHeader("X-CSRFToken", document.querySelector('[name="csrfmiddlewaretoken"]').value);
        xhr.send(post);
      }
    });

    function verifyRegisterFields(username, password, firstname, lastname, dni, dob) {
      if (username == "" || password == "" || firstname == "" || lastname == "" || dni == "" || dob == "") {
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
      if (dni.length != 8) {
        alert("Tu dni debe tener 8 caracteres");
        return false;
      }
      if (!dob.match(/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/)) {
        alert("Tu fecha de nacimiento debe estar en el formato yyyy-mm-dd")
        return false;
      }

      return true;
    }
    break;

  //------------------------------------------------------------------------
  case "prestamo":
    const submitPre = document.querySelector("#prestamo-submit");
    const errorPre = document.querySelector("#errorPrestamo");
    const montoPre = document.querySelector("#prestamo-monto");
    const fechaPre = document.querySelector("#prestamo-fecha");
    const tipoPre = document.querySelector("#prestamo-tipo");
    let valorMonto = "0"

    submitPre.addEventListener("click", (e) => {
      e.preventDefault();
      if (verifyPrestamoFields(montoPre.value, fechaPre.value, tipoPre.value)) {
        let data = {
          csrfmiddlewaretoken: document.querySelector('[name="csrfmiddlewaretoken"]').value,
          monto: valorMonto,
          fecha: fechaPre.value,
          tipo: tipoPre.value.toUpperCase()
        }
        let post = JSON.stringify(data)
        
        const url = "../prestamo/"
        let xhr = new XMLHttpRequest()
        
        xhr.onreadystatechange = function() {
          if (xhr.readyState == XMLHttpRequest.DONE) {
            if (JSON.parse(xhr.responseText).success == 'true') {
              alert("Prestamo otorgado con exito")
              window.location.href = JSON.parse(xhr.responseText).url;
            }
            else
            {
              alert("Prestamo no pudo ser otorgado")
              errorPre.style.display = "block";
            }
          }
        }
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
        xhr.setRequestHeader("X-CSRFToken", document.querySelector('[name="csrfmiddlewaretoken"]').value);
        xhr.send(post);
      }
    });

    function verifyPrestamoFields(monto, fecha, tipo) {
      if (monto == "" || fecha == "" || tipo == "") {
        alert("Debes ingresar un valor");
        return false;
      }
      if (monto.match(/^[0-9]+$/)) { //En caso de no poner coma
        valorMonto = monto + ".00"
      }
      else {
        if (monto.match(/^[0-9]+([,.][0-9]{1})?$/)) { //En caso de que ingrese numero con 1 digitos despues de la coma
          valorMonto = monto.replace(',', '.') + "0"; //Poniendolo con punto en vez de coma y metiendole un 0 al final para que el sistema funcione
        }
        else {
          if (monto.match(/^[0-9]+([,.][0-9]{2})?$/)) { //En caso de que ingrese numero con 2 digitos despues de la coma
            valorMonto = monto.replace(',', '.'); //Poniendolo con punto en vez de coma para que el sistema funcione
          }
          else {
            alert("Debe ingresar un numero");
            return false
          }
        }
      }
      if (!fecha.match(/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/)) {
        alert("La fecha debe estar en el formato yyyy-mm-dd")
        return false;
      }
      if (tipo != "personal" && tipo != "hipotecario" && tipo != "prendario") {
        alert("Ese no es un tipo valido")
        return false;
      }

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
      window.location.href="../home";
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

  //------------------------------------------------------------------------
  case "cheques":
    var xhr = null;
    let botonCheques = document.querySelector("#boton-cheques");
    let tablaCheques = document.querySelector("#tabla-cheques");
    let filtroArchivo = document.querySelector("#archivo-cheques");
    let filtroSalida = document.querySelector("#salida-cheques");
    let filtroDNI = document.querySelector("#dni-cheques");
    let filtroTipo = document.querySelector("#tipo-cheques");
    let filtroEstado = document.querySelector("#estado-cheques");
    let filtroFecha = document.querySelector("#fecha-cheques");


    botonCheques.addEventListener("click", (e) => {
      pedirInformacion(filtroArchivo.value, filtroSalida.value, filtroDNI.value, filtroTipo.value, filtroEstado.value, filtroFecha.value)
    });

    function pedirInformacion(baseDatos, salida, dni, tipo, estado, fecha) {
      let pedido = "";
      if (baseDatos != "" && salida != "" && dni != "") {
        pedido = `http://boredcraft.zapto.org:7777/?archivo=${baseDatos}&salida=${salida}&dni=${dni}`;
      }
      else {
        alert("Es necesario pasar un archivo, un DNI, y una salida");
        return;
      }
      if (tipo != "") {
        pedido += `&tipo=${tipo}`;
      }
      if (estado != "") {
        pedido += `&estado=${estado}`;
      }
      if (fecha != "") {
        pedido += `&fecha=${fecha}`;
      }
      
      xhr = getXmlHttpRequestObject();
      xhr.onreadystatechange = dataCallback;

      xhr.open("GET", pedido, true);
      xhr.responseType = 'json';
      // Send the request over the network
      xhr.send(null);
    }

    function getXmlHttpRequestObject() {
      if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
      }
      return xhr;
    };

    function dataCallback() {
      // Check response is ready or not
      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("Data received");
        if (xhr.response.split(':')[0] == "ERROR") {
          alert(xhr.response.split(':')[1]);
        }
        else {
          // Recibio los datos pedidos
          let entradasHTML = "";
          let entradas = xhr.response.split("|##");
          for (let e of entradas) {
            // Por cada entrada
            let entrada = e.replace('|#','').replace('#','').split('|');
            let datosHTML = []
            for (let d of entrada) {
              let dato = d.split(':');
              switch (dato[0]) {
                case "NroCheque":
                  datosHTML[0] = dato[1];
                  break;
                case "CodigoBanco":
                  datosHTML[1] = dato[1];
                  break;
                case "CodigoSucursal":
                  datosHTML[2] = dato[1];
                  break;
                case "NumeroCuentaOrigen":
                  datosHTML[3] = dato[1];
                  break;
                case "NumeroCuentaDestino":
                  datosHTML[4] = dato[1];
                  break;
                case "Valor":
                  datosHTML[5] = dato[1];
                  break;
                case "FechaOrigen":
                  datosHTML[6] = dato[1];
                  break;
                case "FechaPago":
                  datosHTML[7] = dato[1];
                  break;
                case "DNI":
                  datosHTML[8] = dato[1];
                  break;
                case "Tipo":
                  datosHTML[9] = dato[1];
                  break;
                case "Estado":
                  datosHTML[10] = dato[1];
                  break;
                default:
                  alert("Informacion desconocida recibida (" + dato[0] + ")");
                  return;
              }
            }

            entradasHTML += `
            <div class="columnas">
              <p>${datosHTML[0]}</p>
              <p>${datosHTML[1]}</p>
              <p>${datosHTML[2]}</p>
              <p>${datosHTML[3]}</p>
              <p>${datosHTML[4]}</p>
              <p>$${datosHTML[5]}</p>
              <p>${datosHTML[6]}</p>
              <p>${datosHTML[7]}</p>
              <p>${datosHTML[8]}</p>
              <p>${datosHTML[9]}</p>
              <p>${datosHTML[10]}</p>
            </div>
            `
          }

          tablaCheques.innerHTML = entradasHTML;
        }
      }
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