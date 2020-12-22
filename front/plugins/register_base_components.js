import Vue from 'vue'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'

const requireComponent = require.context(
  // コンポーネントフォルダの相対パス
  './components/bases',
  // サブフォルダ内を調べるかどうか
  false,
  // 基底コンポーネントのファイル名に一致させるのに使う正規表現
  /Base[A-Z]\w+\.(vue|js)$/
)

requireComponent.keys().forEach(fileName => {
  // コンポーネント設定を取得する
  const componentConfig = requireComponent(fileName)

  // コンポーネント名をパスカルケース (PascalCase) で取得する
  const componentName = upperFirst(
    camelCase(
      // フォルダの深さに関わらずファイル名を取得する
      fileName
        .split('/')
        .pop()
        .replace(/\.\w+$/, '')
    )
  )


  // コンポーネントをグローバル登録する
  Vue.component(
    componentName,
    // `export default` を使ってコンポーネントがエクスポートされた場合に存在する
    // `.default` でコンポーネントオプションを期待していて
    // 存在しない場合にはモジュールのルートにフォールバックします。
    componentConfig.default || componentConfig
  )
})
