<template>
  <div class="page">
    <div class="page__form">
      <search-form @search="search($event)"/>
    </div>
    <div class="page__tabs">
      <div class="page__tab">
        <app-tab-button
            :state="tabs.item.state"
            @myClick="tabChange"
        >{{ tabs.item.value }}
        </app-tab-button>
      </div>
      <div class="page__tab">
        <app-tab-button
            :state="tabs.koe.state"
            @myClick="tabChange"
        >{{ tabs.koe.value }}
        </app-tab-button>
      </div>
    </div>

    <div class="page__content">
      <search-item-boxes v-show="tabs.item.state" :records="items" />
      <search-koe-boxes v-show="tabs.koe.state" :koe-lists="koes" />
    </div>
  </div>
</template>

<script>
import SearchForm from "@/components/organisms/forms/SearchForm";
import SearchItemBoxes from "@/components/organisms/ItemBoxes/SearchItemBoxes";
import AppTabButton from "@/components/atoms/buttons/AppTabButton";
import SearchKoeBoxes from "@/components/organisms/koeBoxes/SearchKoeBoxes";

export default {
  name: "search",
  components: {SearchKoeBoxes, AppTabButton, SearchItemBoxes, SearchForm},
  auth: false,
  async asyncData({query, $myAuth, $api}) {
    let params = {}
    if (Object.keys(query).length) {
      query.text ? params.text = query.text : ''
      query.category ? params.category = query.category : ''
      query.orderBy ? params.order_by = query.orderBy : ''
    }
    params.user_id = $myAuth.user().id
    console.log(params)
    const res = await $api['search'].getByParams(params).then(({data}) => {
      return data
    })
    return {
      items: res.entries.items,
      koes: res.entries.koes
    }
  },
  data() {
    return {
      items: [],
      koes: [],
      tabs: {
        item: {
          state: true,
          value: '商品'
        },
        koe: {
          state: false,
          value: 'コエ'
        }
      }

    }
  },
  methods: {
    tabChange() {
      this.tabs.item.state = !this.tabs.item.state
      this.tabs.koe.state = !this.tabs.koe.state
    },
    async search(values) {
      const query = {}
      if (values) {
        console.log(values)
        values.text ? query.text = values.text : ''
        values.category ? query.category = values.category : ''
        values.orderBy ? query.orderBy = values.orderBy : ''
      }
      const params = query
      const res = await this.$api['search'].getByParams(params).then(({data}) => {
        return data
      })
      this.items = res.entries.items
      this.koes = res.entries.koes

      if (Object.keys(query).length) {
        this.$router.push({path: '/search', query: query})
      } else {
        this.$router.push({path: '/search'})
      }
      return true
    }
  }
}
</script>

<style scoped lang="scss">
.page {
  max-width: 1024px;
  margin: 0 auto;
  &__form {
    max-width: 400px;
    margin: 0 auto $large-margin auto;
  }
  &__tabs {
    display: flex;
    justify-content: center;
    margin-bottom: $large-margin;
  }
  &__tab {
    width: 190px;
    height: 40px;
    &:first-child {
      margin-right: $large-margin;
    }
  }


  &__content {
    max-width: 1024px;
    margin: 0 auto;
  }
}
</style>