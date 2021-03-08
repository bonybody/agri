<template>
  <div class="product-up-form">
    <div class="product-up-form__form">
      <item-image-form
          v-model="images.value"
          :reuiqre="images.require"
          :error="images.error"

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
          :date="periodDate"
      />

    </div>
    <div class="product-up-form__form">
      <item-remaining-form
          :picked="remaining.value.picked"
          :options="remaining.value.options"
          @changeRadio="changeRadio($event)"
          @changeValue="changeRemainingDays($event)"
          :value="remaining.value.value"
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
      <item-volume-form
          v-model="volume.value"
          :require="volume.require"
          :error="volume.error"
      />
    </div>
    <div class="product-up-form__form">

      <item-price-form
          v-model="price.value"
          :require="price.require"
          :error="price.error"/>
    </div>
    <div class="product-up-form__form">
      <area-form
          v-model="area.value"
          :require="area.require"
          :error="area.error"
      />
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
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppSeparation from "~/components/atoms/separations/AppSeparation";
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
import AreaForm from "~/components/molecules/forms/AreaForm";
import ItemVolumeForm from "~/components/molecules/forms/ItemVolumeForm";
import dateFormat from "@/functions/format/dateFormat";


export default {
  name: "ProductUpForm",
  components: {
    ItemVolumeForm,
    AreaForm,

    ProductNameForm,
    ItemShipmentForm,
    ItemImageForm,
    ItemPriceForm,
    DeliveryFeeForm,
    ItemCategoryForm,
    ItemRemainingForm,
    ItemPeriodForm,
    ItemDescriptionForm,
    AppSeparation, AppFormButton, AppFormHeading
  },
  data() {
    return {
      images: {
        value: null,
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
          picked: 1,
          options: [
            {value: 1, label: '全期間'},
            {value: 2, label: '一日'},
            {value: 3, label: '一週間'},
            {value: 4, label: '一ヶ月'}
          ]
        }
      },
      category: {
        error: '',
        require: true,
        value: ''
      },
      shipment: {
        error: '',
        require: true,
        value: 1
      },
      volume: {
        value: '',
        require: true,
        error: ''
      },

      price: {
        value: 300,
        require: true,
        error: ''
      },
      area: {
        value: '愛知県名古屋市',
        require: true,
        error: ''
      }
    }
  },
  computed: {
    periodDate() {
      console.log(this.period.value)
      if (this.period.value === 0) {
        return ''
      }
      const date = new Date()
      date.setDate(date.getDate() + this.period.value)
      return dateFormat(date)
    }
  },
  methods: {
    changeRadio(radioValue) {
      console.log(radioValue)
      this.remaining.value.picked = radioValue
    },
    changeRemainingDays(value) {
      console.log(value)
      this.remaining.value.value = value
    },
    clickCheckbox(value) {
      if (value !== 0) {
        this.period.value = 0
      } else {
        this.period.value = 1
      }
    },
    formButtonClick() {
      console.log(this.images)

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
        volume: this.volume.value,
        price: this.price.value,
        user_id: this.$myAuth.user().id,
        area: this.area.value
      }
      console.log(params)
      const formData = new FormData()
      let jsonDate = JSON.stringify(params)
      formData.append('params', jsonDate)
      if (this.images.value) {
        this.images.value.forEach(async function (image, index) {
          await formData.append('image' + index, image)
        })
      }

      this.$api['item'].post(formData).then(({data}) => {
        if (data.state) {
          this.$router.push({path: '/item/' + data.entries.item.id})
        }
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
  &__form {
    margin-bottom: $semi-large-margin;
  }
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