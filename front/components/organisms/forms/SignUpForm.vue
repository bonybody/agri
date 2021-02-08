<template>
  <div class="sign-up-form">
    <app-form-heading>新規登録</app-form-heading>
    <display-name-form v-model="displayName.value" :require="displayName.require"/>
    <email-form v-model="email.value" :require="email.require"/>
    <password-form v-model="password.value" :require="password.require"/>
    <app-separation/>
    <div class="user-name">
      <div class="user-name__label">
        <app-form-label>氏名</app-form-label>
        <app-require-mark v-show="userName.require"/>
      </div>
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

      <div class="birthday__form">
        <year-form v-model="birthday.value.year"/>
        <month-form v-model="birthday.value.month"/>
        <day-form v-model="birthday.value.day" :year="birthday.value.year" :month="birthday.value.month"/>
      </div>
    </div>

    <app-form-button @my-click="send()">新規登録</app-form-button>
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

export default {
  name: "SignUpForm",
  components: {
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
        value: null,
        require: true
      },
      email: {
        value: null,
        require: true
      },
      password: {
        value: null,
        require: true
      },
      userName: {
        require: true,
        value: {
          familyName: '',
          familyNameRuby: '',
          givenName: '',
          givenNameRuby: '',
        }
      },
      birthday: {
        require: true,
        value: {
          year: 1980,
          month: 1,
          day: 1
        }
      }
    }
  },
  methods: {
    send: function () {
      const params = {
        display_name: this.displayName,
        email: this.email,
        password: this.password,
        user_name: {
          family_name: this.userName.value.familyName,
          given_name: this.userName.value.givenName,
          family_name_ruby: this.userName.value.familyNameRuby,
          given_name_ruby: this.userName.value.givenNameRuby,
        },
        birthday: {
          year: this.birthday.year,
          month: this.birthday.month,
          day: this.birthday.day
        }
      }
      console.log(params);
      console.log(this.$api);
      this.$api['user'].signUp(params);
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