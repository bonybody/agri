export default ({$axios, env}) => {
  $axios.defaults.baseURL = env.apiUrlServer;
}
