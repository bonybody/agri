export default class Search {
  constructor(axios, $myAuth) {
    this.api = axios;
    this.prefix = '/search/';
    this.auth = $myAuth
  }

  async getByParams(params) {
    params.user_id = this.auth.user().id
    const res = await this.api.get(this.prefix, {
      params: params
    })
    return res
  }
  async getItemsByUserId(user_id) {
    const res = await this.api.get(this.prefix + 'user', {
      params: {
        user_id: user_id
      }
    })
    return res
  }
  async getNewItems(user_id) {
    const res = await this.api.get(this.prefix + 'new', {
      params: {
        user_id: user_id
      }
    })
    return res
  }

  async getFavoriteItems(user_id) {
    const res = await this.api.get(this.prefix + 'favorite', {
      params: {
        user_id: user_id
      }
    })
    return res
  }


  async post(params) {
    this.api.setHeader('Content-Type', 'multipart/form-data')
    this.api.setHeader('Accept', 'application/json')
    const res = await this.api.post(this.prefix, params);
    return res
  }
}