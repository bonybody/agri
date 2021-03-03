export default function ({$auth, redirect}, inject) {
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
  async logout() {
    return await this.auth.logout()
  }

  getToken() {
    return this.auth.strategy.token.get()
  }
}