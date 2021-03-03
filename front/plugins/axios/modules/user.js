export default class User {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/user/';
    console.log(this.api);
  }

  async signUp(params) {
    this.api.setHeader('Content-Type', 'multipart/form-data')
    this.api.setHeader('Accept', 'application/json')
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
  }
}