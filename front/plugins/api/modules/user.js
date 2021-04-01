export default class User {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/user/';
  }

  async signUp(params) {
    this.api.setHeader('Content-Type', 'multipart/form-data')
    this.api.setHeader('Accept', 'application/json')
    const res = await this.api.post(this.prefix, params);
  }
}