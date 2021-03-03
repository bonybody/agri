import User from "~/plugins/axios/modules/user";
import { axios } from "~/plugins/axios/axios.js";
import Item from "~/plugins/axios/modules/item";
import ItemTransaction from "~/plugins/axios/modules/item_transaction";

export default function (context ,inject) {
  const api = [];
  api['user'] = new User(axios);
  api['item'] = new Item(axios);
  api['item-transaction'] = new ItemTransaction(axios);
  inject('api', api)
}