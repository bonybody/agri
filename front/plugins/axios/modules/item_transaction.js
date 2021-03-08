export default class ItemTransaction {
  constructor(axios) {
    this.api = axios;
    this.prefix = '/item-transaction/';
    console.log(this.api);
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
    console.log(params);
    const res = await this.api.post(this.prefix, params);
    console.log(res);
    return res
  }

  async getByBuyerId(buyer_id) {
    console.log(buyer_id);
    const res = await this.api.get(this.prefix + 'buyer', {
      params: {
        id: buyer_id
      }
    });
    console.log(res);
    return res
  }
  async getBySellerId(seller_id) {
    console.log(seller_id);
    const res = await this.api.get(this.prefix + 'seller', {
      params: {
        id: seller_id
      }
    });
    console.log(res);
    return res
  }
  async getSalesDetailBySellerId(seller_id) {
    console.log(seller_id);
    const res = await this.api.get(this.prefix + 'seller/detail', {
      params: {
        id: seller_id
      }
    });
    console.log(res);
    return res
  }
  async getBySellerIdStateSold(seller_id) {
    console.log(seller_id);
    const res = await this.api.get(this.prefix + 'seller/sold', {
      params: {
        id: seller_id
      }
    });
    console.log(res);
    return res
  }
}