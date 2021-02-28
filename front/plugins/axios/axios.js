export let axios;

export default ({$myAuth, $axios, env}) => {
  // 共通処理

  // 環境変数のAPI_URLをbaseURLにセット
  $axios.defaults.baseURL = env.apiUrl;
  console.log('apiUrl: ' + env.apiUrl);
  // リクエスト作成時にフックされる
  $axios.onRequest(config => {
    // if ($myAuth.loggedIn()) {
    //   console.log('ログイン中のレクエストを作成しています...');
    //   config.headers.common['Authorization'] = `Bearer token`;
    //   config.headers.common['Accept'] = 'application/json';
    // }
    // if (!$myAuth.loggedIn()) {
    //   console.log('未ログイン中のリクエストを作成しています...');
    // }
  });


  // レスポンスが帰ってくると発火する
  $axios.onResponse(response => {
    return Promise.resolve(response);
  })

  // エラーが出ると発火する
  $axios.onError(error => {
    console.log('通信に失敗しました。');
    return Promise.reject(error.response);
  });
  axios = $axios;
}
