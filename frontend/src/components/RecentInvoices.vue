<template>
  <div class="invoice-container">
    <div class="header">
      <h2>Recent Invoices</h2>
      <FloatLabel>
        <InputText id="search" v-model="searchQuery" />
        <label for="search">Search</label>
      </FloatLabel>
    </div>
    <div class="invoice-holder">
      <div class="invoices">
        <div class="invoice" v-for="invoice in filteredInvoices" :key="invoice.month">
          <h3 class="month">{{ invoice.month }}</h3>
          <Listbox v-model="selectedInvoice" :options="invoice.data" @optionLabel="invoice.data" class="w-full md:w-56" listStyle="max-height:200px"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import Listbox from 'primevue/listbox';


interface Invoice {
  month: string;
  data: string[];
}

export default defineComponent({
  name: 'RecentInvoices',
  components: {
    InputText,
    FloatLabel,
    Listbox,
  },
  data() {
    return {
      selectedInvoice: null,
    }
  },
  setup() {
    const searchQuery = ref<string>('');
    const invoices = ref<Invoice[]>([
      { month: 'January',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom', 'Bedroom'] },
      { month: 'February',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'March',  data: ['Bathroom', 'Kitchen', 'Living Room', 'Basement', 'Bedroom'] },
      { month: 'April',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'May',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'June',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'July',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'August',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'September',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'October',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'November',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
      { month: 'December',  data: ['Bathroom', 'Kitchen', 'Bedroom', 'Basement', 'Bedroom'] },
    ]);
    
    const filteredInvoices = computed<Invoice[]>(() => {
      return invoices.value.map(invoice => {
        return {
          ...invoice,
          data: invoice.data.filter(item =>
            item.toLowerCase().includes(searchQuery.value.toLowerCase())
          ),
        };
      });
    });

    const filteredData = computed<string[]>(() => {
      return invoices.value
        .map(invoice => invoice.data)
        .flat()
        .filter(item =>
          item.toLowerCase().includes(searchQuery.value.toLowerCase())
        );
    });

    return {
      searchQuery,
      filteredInvoices,
      filteredData
    };
  },
});
</script>

<style scoped>
#search {
  color: black;
}

.month {
  text-align: center;
}

.content {
  height: 100px;
  overflow-y: auto;
}

.invoice-container {
  width: 30%;
  padding: 1%;
  box-sizing: border-box;
  background-color: rgba(176, 107, 255, 0.3);
  margin: 1%;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-bottom: 10px;
}

.search-bar {
  flex: 1;
  padding: 5px;
  margin: 0 10px;
}

.invoices {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  
}

.invoice-holder {
  height: 300px;
  overflow-y: auto;
}

.invoice {
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
</style>