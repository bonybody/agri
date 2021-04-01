import api from "~/plugins/api/modules";
export default function ({ env, $axios, $myAuth } ,inject) {
  console.log($myAuth)
  const apiClient = api($axios, $myAuth)
  inject('api', apiClient)
}