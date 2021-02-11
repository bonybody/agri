<template>
  <div class="sign-up-form">
    <app-form-heading>新規登録</app-form-heading>
    <display-name-form v-model="displayName.value" :require="displayName.require" :error="displayName.error"/>
    <email-form v-model="email.value" :require="email.require" :error="email.error"/>
    <password-form v-model="password.value" :require="password.require" :error="password.error"/>
    <app-separation/>
    <div class="user-name">
      <div class="user-name__label">
        <app-form-label>氏名</app-form-label>
        <app-require-mark v-show="userName.require"/>
      </div>
      <app-error-message>{{ userName.error }}</app-error-message>
      <div class="user-name__line">
        <family-name-form v-model="userName.value.familyName"/>
        <given-name-form v-model="userName.value.givenName"/>
      </div>
      <div class="user-name__line">
        <family-name-ruby-form v-model="userName.value.familyNameRuby"/>
        <given-name-ruby-form v-model="userName.value.givenNameRuby"/>
      </div>
    </div>
    <div class="birthday">
      <div class="birthday__label">
        <app-form-label>生年月日</app-form-label>
        <app-require-mark v-show="birthday.require"/>
      </div>
      <app-error-message>{{ birthday.error }}</app-error-message>
      <div class="birthday__form">
        <year-form v-model="birthday.value.year"/>
        <month-form v-model="birthday.value.month"/>
        <day-form v-model="birthday.value.day" :year="birthday.value.year" :month="birthday.value.month"/>
      </div>
    </div>

    <app-form-button @my-click="signUp()">新規登録</app-form-button>
  </div>
</template>

<script>
import AppFormHeading from "~/components/atoms/headings/AppFormHeading";
import EmailForm from "~/components/molecules/forms/EmailForm";
import PasswordForm from "~/components/molecules/forms/PasswordForm";
import AppFormButton from "~/components/atoms/forms/button/AppFormButton";
import AppSeparation from "~/components/atoms/separations/AppSeparation";
import DisplayNameForm from "~/components/molecules/forms/DisplayNameForm";
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

export default {
  name: "SignUpForm",
  components: {
    AppErrorMessage,
    AppRequireMark,
    AppFormLabel,
    DayForm,
    MonthForm,
    YearForm,
    GivenNameRubyForm,
    GivenNameForm,
    FamilyNameRubyForm,
    FamilyNameForm, AppSeparation, AppFormButton, PasswordForm, EmailForm, DisplayNameForm, AppFormHeading
  },
  data() {
    return {
      displayName: {
        value: '',
        error: '',
        require: true
      },
      image: {
        value: '',
        error: '',
        require: false
      },
      email: {
        value: '',
        error: '',
        require: true
      },
      password: {
        value: '',
        error: '',
        require: true
      },
      userName: {
        require: true,
        error: '',
        value: {
          familyName: '',
          familyNameRuby: '',
          givenName: '',
          givenNameRuby: '',
        }
      },
      birthday: {
        require: true,
        error: '',
        value:
            {
              year: 1981,
              month: 1,
              day: 1
            }
      }
    }
  },
  methods: {
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
.sign-up-form {
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