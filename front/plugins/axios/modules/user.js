export default class User {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/user/';
    console.log(this.api);
  }

  async signUp(params) {
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
  }
}