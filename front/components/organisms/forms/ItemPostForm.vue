<template>
  <div class="product-up-form">
    <div class="product-up-form__form">
      <item-image-form
          v-model="image.value"
          :reuiqre="false"
          :error="image.error"
      />
    </div>
    <div class="product-up-form__form">
      <product-name-form
          v-model="itemName.value"
          :require="itemName.require"
          :error="itemName.error"
      />
    </div>
    <div class="product-up-form__form">
      <item-description-form
          v-model="itemDescription.value"
          :require="itemDescription.require"
          :error="itemDescription.error"
      />
    </div>
    <div class="product-up-form__form">
      <item-period-form
          v-model="period.value"
          :toggle="period.value"
          @clickCheckbox="clickCheckbox"
          :require="period.require"
          :error="period.error"
      />
    </div>
    <div class="product-up-form__form">
      <item-remaining-form
          v-model="remaining.value.value"
          :picked="remaining.value.picked"
          :options="remaining.value.options"
          @changeRadio="changeRadio($event)"
          :require="remaining.require"
          :error="remaining.error"
      />
    </div>
    <div class="product-up-form__form">
      <item-category-form
          v-model="category.value"
          :require="category.require"
          :error="category.error"
      />
    </div>
    <div class="product-up-form__form">
      <delivery-fee-form
          v-model="deliveryFee"
          :require="deliveryFee.require"
          :error="deliveryFee.error"
      />
    </div>
    <div class="product-up-form__form">
      <item-price-form
          v-model="price.value"
          :require="price.require"
          :error="price.error"/>
    </div>
    <app-separation/>
    <app-form-button @my-click="formButtonClick">次へ進む</app-form-button>
  </div>
</template>

<script>
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";
import EmailForm from "~/components/molecules/forms/EmailForm";
import PasswordForm from "~/components/molecules/forms/PasswordForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppSeparation from "~/components/atoms/separations/AppSeparation";
import ProductPhotoForm from "~/components/molecules/forms/ProductPhotoForm";
import FamilyNameForm from "~/components/molecules/forms/FamilyNameForm";
import FamilyNameRubyForm from "~/components/molecules/forms/FamilyNameRubyForm";
import GivenNameForm from "~/components/molecules/forms/GivenNameForm";
import GivenNameRubyForm from "~/components/molecules/forms/GivenNameRubyForm";
import YearForm from "~/components/molecules/forms/YearForm";
import MonthForm from "~/components/molecules/forms/MonthForm";
import DayForm from "~/components/molecules/forms/DayForm";
import AppFormLabel from "~/components/atoms/forms/label/AppFormLabel";
import AppRequireMark from "~/components/atoms/forms/marks/AppRequireMark";
import AppErrorMessage from "~/components/atoms/forms/error/AppErrorMessage";
import ProductDescriptionForm from "~/components/molecules/forms/ItemDescriptionForm";
import ItemDescriptionForm from "~/components/molecules/forms/ItemDescriptionForm";
import ItemPeriodForm from "~/components/molecules/forms/ItemPeriodForm";
import ItemRemainingForm from "~/components/molecules/forms/ItemRemainingForm";
import ItemCategoryForm from "~/components/molecules/forms/ItemCategoryForm";
import DeliveryFeeForm from "~/components/molecules/forms/DeliveryFeeForm";
import ItemPriceForm from "~/components/molecules/forms/ItemPriceForm";
import ItemImageForm from "~/components/molecules/forms/ItemImageForm";
import requireValidate from "~/functions/validate/requireValidate";

export default {
  name: "ProductUpForm",
  components: {
    ItemImageForm,
    ItemPriceForm,
    DeliveryFeeForm,
    ItemCategoryForm,
    ItemRemainingForm,
    ItemPeriodForm,
    ItemDescriptionForm,
    ProductDescriptionForm,
    AppErrorMessage,
    AppRequireMark,
    AppFormLabel,
    DayForm,
    MonthForm,
    YearForm,
    GivenNameRubyForm,
    GivenNameForm,
    FamilyNameRubyForm,
    FamilyNameForm, AppSeparation, AppFormButton, PasswordForm, EmailForm, ProductPhotoForm, AppFormHeading
  },
  data() {
    return {
      image: {
        value: '',
        error: '',
        require: false
      },

      itemName: {
        value: '',
        error: '',
        require: true
      },
      itemDescription: {
        value: '',
        error: '',
        require: false
      },
      period: {
        require: true,
        error: '',
        value: 1
      },
      remaining: {
        require: true,
        error: '',
        value: {
          value: 1,
          picked: 'whole',
          options: [
            {value: 'whole', label: '全期間'},
            {value: 'day', label: '一日'},
            {value: 'week', label: '一週間'},
            {value: 'month', label: '一ヶ月'}
          ]
        }
      },
      category: {
        error: '',
        require: true,
        value: ''
      },
      deliveryFee: {
        error: '',
        require: true,
        value: ''
      },
      shipment: {
        error: '',
        require: true,
        value: ''
      },
      price: {
        value: 300,
        require: true,
        error: ''
      },
    }
  },
  methods: {
    changeRadio(radioValue) {
      console.log(radioValue)
      this.remaining.value.picked = radioValue
    },
    clickCheckbox(value) {
      if (value !== 0) {
        this.period.value = 0
      } else {
        this.period.value = 1
      }
    },
    formButtonClick() {
      let validateFlg;
      validateFlg = requireValidate(this.$data);
      if (!validateFlg) {
        return
      }
    },
    signUp: function () {
      let errorFlg = false
      !this.requireValidate(this.displayName) ? errorFlg = true : '';
      !this.requireValidate(this.email) ? errorFlg = true : '';
      !this.requireValidate(this.password) ? errorFlg = true : '';
      !this.requireValidate(this.userName) ? errorFlg = true : '';
      !this.requireValidate(this.birthday) ? errorFlg = true : '';
      if (errorFlg) {
        return
      }
      const params = {
        display_name: this.displayName.value,
        email: this.email.value,
        image: this.image.value,
        password: this.password.value,
        name: this.userName.value.familyName + this.userName.value.givenName,
        name_ruby: this.userName.value.familyNameRuby + this.userName.value.givenNameRuby,
        birthday: this.birthday.value.year + '-' +
            ('00' + this.birthday.value.month).slice(-2) + '-' +
            ('00' + this.birthday.value.day).slice(-2)
      }
      this.$api['user'].signUp(params).then(() => {
        console.log(this.email.value, this.password.value)
        this.$myAuth.login(this.email.value, this.password.value)
      }).catch((e) => {
        console.log(e)
      });

    },
    requireValidate: function (form) {
      if (form.require) {
        if (typeof form.value === 'object') {
          Object.keys(form.value).forEach(function (key) {
            if (form.value[key] === '') {
              form.error = '入力必須です。';
              return false
            }
          }, form.value);
        } else {
          if (!form.value) {
            form.error = "入力必須です。";
            return false
          }
        }
      }
      return true;
    },
  }
}
</script>

<style scoped lang="scss">
.product-up-form {
  @include form-box-style();
}

.user-name {
  &__label {
    @include left-right-alignment-mixin;
  }

  &__line {
    width: 100%;
    display: flex;

    div:first-child {
      margin-right: 30px;
    }
  }
}

.birthday {
  &__label {
    @include left-right-alignment-mixin;
  }

  &__form {
    @include left-right-alignment-mixin;
  }
}
</style>