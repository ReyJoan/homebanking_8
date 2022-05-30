(function() {
  document.getElementById("navbar").innerHTML =(
    "<div class='nav-logo'>" +
      "<a href='home.html'>" +
        "<img class='logo-img' src='../public/img/itbank_logo.jpg'/>" +
      "</a>" +
    "</div>" +
    "<div class='nav-links'>" +
      "<ul class='link-list'>" +
        "<li class='nav-link'>" +
          "<a class='link' href='home.html'>Home</a>" +
        "</li>" +
        "<li class='nav-link'>" +
          "<a class='link' href='#'>Turnos</a>" +
        "</li>" +
        "<li class='nav-link'>" +
          "<a class='link' href='#'>Personas</a>" +
        "</li>" +
      "</ul>" +
    "</div>" +
    "<div class='nav-usuario'>" +
      "<a class='nav-user' href='user.html'>Usuario" +
        "<i class='fa-solid fa-user'></i>" +
      "</a>" +
    "</div>"
  );
  document.getElementById("footer").innerHTML = (
    "<p class='col-md-4 mb-0 text-muted'>© 2022 Random, Inc.</p>" +
    "<ul class='nav col-md-4 justify-content-end'>" +
      "<li class='nav-item'>" +
        "<a href='home.html' class='nav-link px-2 text-muted'>Home</a>" +
      "</li>" +
      "<li class='nav-item'>" +
        "<a href='user.html' class='nav-link px-2 text-muted'>Usuario</a>" +
      "</li>" +
      "<li class='nav-item'>" +
        "<a href='#' class='nav-link px-2 text-muted'>Turnos</a>" +
      "</li>" +
      "<li class='nav-item'>" +
        "<a href='#' class='nav-link px-2 text-muted'>FAQs</a>" +
      "</li>" +
      "<li class='nav-item'>" +
        "<a href='#'' class='nav-link px-2 text-muted'>About</a>" +
      "</li>" +
    "</ul>"
  );
})()



      // Import the functions you need from the SDKs you need
      import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js";
      import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-analytics.js";
      import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-auth.js";
      
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
        measurementId: "G-2MB6CQWJ18"
      };
      
      // Initialize Firebase
      const app = initializeApp(firebaseConfig);
      const analytics = getAnalytics(app);
      const auth = getAuth();
      
      //Sign Out
      signOut(auth).then(() => {
          // Sign-out successful.
        }).catch((error) => {
          // An error happened.
        });
      
      
      //Detecta el html activo y aplica diferente codigo dependiendo de eso
      const htmlDetect = document.querySelector('#htmlID');
      switch(htmlDetect.textContent) {
        //------------------------------------------------------------------------
        case 'user':
          const form1 = document.querySelector('#registerForm');
          const form2 = document.querySelector('#loginForm');
          const form3 = document.querySelector('#mainForm');

          const userRegister = document.querySelector('#register-name');
          const passwordRegister = document.querySelector('#register-pass');
          const userLogin = document.querySelector('#login-name');
          const passwordLogin = document.querySelector('#login-pass');
          
          const submitReg = document.querySelector('#register-submit');
          const submitLog = document.querySelector('#login-submit');
          const botonLog = document.querySelector('#main-login-btn');
          const botonReg = document.querySelector('#main-register-btn');
          
          botonLog.addEventListener('click', ()=>{
              form3.style.display = 'none';
              form2.style.display = "block";
          })
          
          botonReg.addEventListener('click', ()=>{
              form3.style.display = 'none';
              form1.style.display = "block";
          })
          
          //Register button
          submitReg.addEventListener('click',(e)=>{
              e.preventDefault();
              if (userRegister.value == "" || passwordRegister.value == "") {
                  alert('Debes ingresar un valor');
              }
              else {
              createUserWithEmailAndPassword(auth, userRegister.value + "@blablaestafas.com", passwordRegister.value)
              .then((userCredential) => {
                // Signed in 
                const user = userCredential.user;
                console.log("Register complete");
                window.location.href = "home.html";  
              })
              .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                console.log(userRegister.value + "@blablaestafas.com" + "\n" + passwordRegister.value + "\n" + errorMessage);
                // ..
              });
              }
          }) 
          
          //Login button
          submitLog.addEventListener('click', (e)=> {
              e.preventDefault();
              if (userLogin.value == "" || passwordLogin.value == "") {
                  alert('Debes ingresar un valor');
              }
              else {
              signInWithEmailAndPassword(auth, userLogin.value + "@blablaestafas.com", passwordLogin.value)
              .then((userCredential) => {
                // Signed in 
                const user = userCredential.user;
                console.log("Login complete");
                window.location.href = "home.html";  
              })
              .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                console.log(userLogin.value + "@blablaestafas.com" + "\n" + passwordLogin.value + "\n" + errorMessage);
              });
            }
          })
          break;
        //------------------------------------------------------------------------
        case 'home':
          console.log('???');
          break;
        //------------------------------------------------------------------------
        case 'saldo':
          console.log('???');
          break;
      }
          