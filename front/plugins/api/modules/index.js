import User from "@/plugins/api/modules/user";
import Item from "@/plugins/api/modules/item";
import ItemTransaction from "@/plugins/api/modules/item_transaction";
import Koe from "@/plugins/api/modules/koe";
import Favorite from "@/plugins/api/modules/favorite";
import Search from "@/plugins/api/modules/search";
export default function api (axios, $myAuth) {
  const api =[]
  api['user'] = new User(axios, $myAuth);
  api['item'] = new Item(axios, $myAuth);
  api['item-transaction'] = new ItemTransaction(axios, $myAuth);
  api['koe'] = new Koe(axios, $myAuth);
  api['favorite'] = new Favorite(axios, $myAuth);
  api['search'] = new Search(axios, $myAuth);
  return api
};
