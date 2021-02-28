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
    <div class="product-up-form__form">
      <item-shipment-form
          v-model="shipment.value"
          :require="shipment.require"
          :error="shipment.error"/>
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
import ItemShipmentForm from "~/components/molecules/forms/ItemShipmentForm";
import ProductNameForm from "~/components/molecules/forms/ProductNameForm";

export default {
  name: "ProductUpForm",
  components: {
    ProductNameForm,
    ItemShipmentForm,
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
          picked: '1',
          options: [
            {value: '1', label: '全期間'},
            {value: '2', label: '一日'},
            {value: '3', label: '一週間'},
            {value: '4', label: '一ヶ月'}
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
        value: 1
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
      this.post()
    },
    post() {
      const params = {
        name: this.itemName.value,
        description: this.itemDescription.value,
        period: this.period.value,
        remaining_days: this.remaining.value.value,
        remaining_format_id: this.remaining.value.picked,
        category_id: this.category.value,
        shipment: this.shipment.value,
        price: this.price.value,
        user_id: this.$myAuth.user().id
      }
      const fileParam = this.image.value
      const formData = new FormData()
      let jsonDate = JSON.stringify(params)
      formData.append('params', jsonDate)
      formData.append('image', fileParam)
      this.$api['item'].post(formData).then(({data}) => {
        console.log(data)
      }).catch((e) => {
        console.log(e)
      });

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