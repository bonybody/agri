export default function ({$auth, redirect}, inject) {
  console.log($auth.loggedIn)
  console.log($auth.$storage.getCookies())
  const myAuth = new MyAuth($auth, redirect)
  inject('myAuth', myAuth)
}

class MyAuth {
  constructor(auth, redirect) {
    this.auth = auth
    this.redirect = redirect
  }

  login(email, password) {
    this.auth.loginWith('local', {
      data: {
        username: email,
        password: password
      }
    })
      .then((response) => {
          console.log("成功");
          console.log(response);
          console.log(this.auth.loggedIn);
          console.log(this.auth.user);
          return response
        },
        (error) => {
          return error
        })
  }

  user() {
    return this.auth.user
  }

  loggedIn() {
    return this.auth.loggedIn
  }
}