<template>
  <div class="invoice-container">
    <h2>Recent Invoices</h2>
    <div class="header">
      <input type="text" placeholder="search" v-model="searchQuery" class="search-bar" />
    </div>
    <div class="invoices">
      <div class="invoice" v-for="(items, month) in filteredInvoices" :key="month">
        <h3><span class="highlight">{{ month }}</span></h3>
        <ul>
          <li v-for="item in items" :key="item">{{ item }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RecentInvoices",
  data() {
    return {
      searchQuery: '',
      groupBy: 'date',
      invoices: {
        August: ['Backyard', 'Bedroom', 'Kids room'],
        July: ['Backyard', 'Bedroom', 'Kids room'],
        June: ['Bathroom', 'Kitchen'],
        May: ['Basement', 'Kitchen', 'Bathroom'],
        April: ['Basement'],
        March: ['Backyard', 'Bedroom', 'Kids room'],
        February: ['Backyard', 'Bedroom', 'Kids room'],
        January: ['Backyard', 'Bedroom', 'Kids room'],
      },
    };
  },
  computed: {
    /*filteredInvoices() {
      let result = {};
      for (let month in this.invoices) {
        result[month] = this.invoices[month].filter(item =>
          item.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      return result;
    },*/
  },
});
</script>
<style scoped>
  .invoice-container {
    width: 40%;
    padding: 10px;
    box-sizing: border-box;
    border: 3px black solid;
    border-radius: 20px;
  }

  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
  }

  .search-bar {
    flex: 1;
    padding: 5px;
    margin-right: 10px;
    border-radius: 10px;
  }

  .invoices {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }

  .invoice {
    border: 1px solid #000;
    padding: 10px;
    margin: 10px;
    width: 22%;
    box-sizing: border-box;
  }

  .invoice h3 {
    margin-top: 0;
  }

  .invoice ul {
    list-style: none;
    padding: 0;
  }

  .invoice ul li {
    margin: 5px 0;
  }

  .highlight {
    color: rgb(0,212,255);
    color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
  }
</style>
