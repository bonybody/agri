import User from "~/plugins/axios/modules/user";
import { axios } from "~/plugins/axios/axios.js";
export default function (context ,inject) {
  const api = [];
  api['user'] = new User(axios);
  inject('api', api)
}