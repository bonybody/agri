export default function requireValidate(attrs) {
  let flg = true;
  Object.keys(attrs).forEach(function (key) {
    console.log(attrs[key]);
    if (
      (attrs[key].value === '' ||
        attrs[key].value === null ||
        attrs[key].value === false) &&
      attrs[key].require
    ) {
      attrs[key].error = 'この項目は入力必須です。'
      flg = false
    }
  });
  return flg
}