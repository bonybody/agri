import User from "~/plugins/axios/modules/user";
import { axios } from "~/plugins/axios/axios.js";
import Item from "~/plugins/axios/modules/item";
import ItemTransaction from "~/plugins/axios/modules/item_transaction";
import api from "~/plugins/axios/modules";
export default function ({ env } ,inject) {
  const apiClient = api(axios)
  inject('api', apiClient)
}