export default function requireValidate(attrs) {
  let flg = true;
  Object.keys(attrs).forEach(function (key) {
    if (
      (attrs[key].value === '' ||
        attrs[key].value === null ||
        attrs[key].value === false) &&
      attrs[key].require
    ) {
      attrs[key].error = 'この項目は入力必須です。'
      console.log(attrs[key])
      flg = false
    } else {
      // attrs[key].error = ''
    }
  });
  return flg
}