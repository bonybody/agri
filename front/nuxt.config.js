export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  ssr: false,
  head: {
    title: 'agri',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
    ]
  },

  router: {
    middleware: ['auth']
  },
  loading: {
    color: 'green',
    failedColor: 'red',
    height: '5px'
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    '@assets/css/destyle.css',
    '@assets/css/common.scss'
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    // '~/plugins/my-auth/my-auth'
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/style-resources'
  ],
  auth: {
    plugins: [ '~/plugins/my-auth/my-auth.js' ],
    redirect: {
      login: '/login',   // 未ログイン時に認証ルートへアクセスした際のリダイレクトURL
      logout: '/',  // ログアウト時のリダイレクトURL
      callback: false,   // Oauth認証等で必要となる コールバックルート
      home: '/',         // ログイン後のリダイレクトURL
    },
    strategies: {
      local: {
        token: {
          property: 'access_token'
        },
        user: {
          property: false
        },
        endpoints: {
          login: {url: 'auth', method: 'post'},
          user: {url: 'user/', method: 'get'},
          logout: false
        },
      }
    }
  },
  styleResources: {
    scss: [
      '~/assets/css/variables.scss'
    ]
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    baseURL: 'http://localhost:8002',
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
  },
  watchers: {
    webpack: {
      poll: 1000
    }
  }
}
