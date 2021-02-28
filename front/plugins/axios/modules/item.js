export default class Item {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/item/';
    console.log(this.api);
  }

  async post(params) {
    this.api.setHeader('Content-Type', 'multipart/form-data')
    this.api.setHeader('Accept', 'application/json')
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
    return res
  }
}