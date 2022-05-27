
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
      
      
      
      
      const form1 = document.querySelector('.register-form');
      const form2 = document.querySelector('.logIn-form');
      const form3 = document.querySelector('.main-form');
      const userRegister = document.querySelector('#user');
      const passwordRegister = document.querySelector('#clav');
      
      const userLogin = document.querySelector('#user-name');
      const passwordLogin = document.querySelector('#user-pass');
      const botonFormR = document.querySelector('#btn-registro');
      const botonLog = document.querySelector('#Log');
      const botonReg = document.querySelector('#Reg');
      const botonEntry = document.querySelector('#entry');
      
      botonLog.addEventListener('click', ()=>{
          form3.style.display = 'none';
          form2.style.display = "block";
      })
      
      botonReg.addEventListener('click', ()=>{
          form3.style.display = 'none';
          form1.style.display = "block";
      })
      
      
      
      //Register button
      botonFormR.addEventListener('click',(e)=>{
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
      botonEntry.addEventListener('click', (e)=> {
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
          