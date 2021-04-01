export default class ItemTransaction {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/item-transaction/';
  }

  async getById(id) {
    const res = await this.api.get(this.prefix, {
      params: {
        id: id
      }
    })
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

  async getByBuyerId(buyer_id) {
    const res = await this.api.get(this.prefix + 'buyer', {
      params: {
        id: buyer_id
      }
    });
    return res
  }
  async getBySellerId(seller_id) {
    const res = await this.api.get(this.prefix + 'seller', {
      params: {
        id: seller_id
      }
    });
    return res
  }
  async getSalesDetailBySellerId(seller_id) {
    const res = await this.api.get(this.prefix + 'seller/detail', {
      params: {
        id: seller_id
      }
    });
    return res
  }
  async getBySellerIdStateSold(seller_id) {
    const res = await this.api.get(this.prefix + 'seller/sold', {
      params: {
        id: seller_id
      }
    });
    return res
  }
}