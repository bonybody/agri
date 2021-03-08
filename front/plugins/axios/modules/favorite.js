export default class Favorite {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/favorite/';
    console.log(this.api);
  }

  async getItemsByUserId(id) {
    const res = await this.api.get(this.prefix + 'item', {
      params: {
        id: id
      }
    })
    return res
  }
  async changeFavorite(user_id, item_id) {
    const res = await this.api.post(this.prefix + 'item', {
      user_id: user_id,
      item_id: item_id
    })
  }

  async postItem(user_id, item_id) {
    const res = await this.api.post(this.prefix + 'item',
      {
        user_id: user_id,
        item_id: item_id
      })
  }

  async postKoe(user_id, koe_id) {
    const res = await this.api.post(this.prefix + 'koe')
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
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
    return res
  }

  async getByPostUser(user_id) {
    const res = await this.api.get(this.prefix + 'post-user', {
      params: {
        id: user_id
      }
    });
    console.log(res);
    return res
  }

  async getByCatchUser(user_id) {
    const res = await this.api.get(this.prefix + 'catch-user', {
      params: {
        id: user_id
      }
    });
    console.log(res);
    return res
  }

  async getByItem(item_id) {
    const res = await this.api.get(this.prefix + 'item', {
      params: {
        id: item_id
      }
    });
    console.log(res);
    return res
  }
}