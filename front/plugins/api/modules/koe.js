export default class Koe {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/koe/';
  }

  async getById(id) {
    const res = await this.api.get(this.prefix, {
      params: {
        id: id
      }
    })
    return res
  }
  async getByNew() {
    const res = await this.api.get(this.prefix + 'new')
    return res
  }

  async receive(id) {
    const res = await this.api.patch(this.prefix + 'receive', {
      id: id
    })
    return res
  }
  async shipment(id) {
    const res = await this.api.patch(this.prefix + 'shipment', {
      id: id
    })
    return res
  }


  async post(params) {
    const res = await this.api.post(this.prefix, params);
    return res
  }

  async getByPostUser(user_id) {
    const res = await this.api.get(this.prefix + 'post-user', {
      params: {
        id: user_id
      }
    });
    return res
  }

  async getByCatchUser(user_id) {
    const res = await this.api.get(this.prefix + 'catch-user', {
      params: {
        id: user_id
      }
    });
    return res
  }

  async getByItem(item_id) {
    const res = await this.api.get(this.prefix + 'item', {
      params: {
        id: item_id
      }
    });
    return res
  }
}