import User from "~/plugins/axios/modules/user";
import Item from "~/plugins/axios/modules/item";
import ItemTransaction from "~/plugins/axios/modules/item_transaction";
import Koe from "~/plugins/axios/modules/koe";

export default function api (axios) {
  const api =[]
  api['user'] = new User(axios);
  api['item'] = new Item(axios);
  api['item-transaction'] = new ItemTransaction(axios);
  api['koe'] = new Koe(axios);
  return api
};