const signup = document.querySelector(".signup");
const signupTitle = signup.querySelector(".signup__title");
const signupInfo = signup.querySelector(".signup__info");
const signupForm = signup.querySelector(".signup__form");

const login = document.querySelector(".login");
const loginTitle = login.querySelector(".login__title");
const loginInfo = login.querySelector(".login__info");
const loginForm = login.querySelector(".login__form");

function centerSignup() {
  const isCentered1 = signup.classList.contains("signup_centered");
  signup.classList.toggle("signup_centered");
  login.classList.toggle("login_hidden");
  if (isCentered1) {
    setTimeout(() => {
	  signupForm.classList.add("signup__form--hiding");
	  signupInfo.classList.remove("signup__info--hiding");
      signupForm.classList.add("signup__form--hidden");
      signupInfo.classList.remove("signup__info--hidden");
  }, 500);
  } else {
    signupForm.classList.remove("signup__form--hiding");
    signupForm.classList.remove("signup__form--hidden");
    signupInfo.classList.add("signup__info--hiding");
    signupInfo.classList.add("signup__info--hidden");
  }
}
signupTitle.addEventListener("click", centerSignup);

function centerLogin() {
  const isCentered2 = login.classList.contains("login_centered");
  login.classList.toggle("login_centered");
  signup.classList.toggle("signup_hidden");
  if (isCentered2) {
    loginForm.classList.add("login__form--hiding");
    loginInfo.classList.remove("login__info--hiding");
    setTimeout(() => {
      loginForm.classList.add("login__form--hidden");
      loginInfo.classList.remove("login__info--hidden");
  }, 500);
  } else {
    loginForm.classList.remove("login__form--hiding");
    loginForm.classList.remove("login__form--hidden");
    loginInfo.classList.add("login__info--hiding");
    loginInfo.classList.add("login__info--hidden");
  }
}
loginTitle.addEventListener("click", centerLogin);
