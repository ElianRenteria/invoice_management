<template>
    <h1>Clients</h1>
    <div class="main">
      <ClientsNavBar @search="filterClients" @toggleAddClientForm="toggleAddClientForm" />
      <div class="container">
        <ClientsList :clients="filteredClients" @selectClient="selectClient" />
        <ClientDetailSidebar :client="selectedClient" v-if="showSidebar" @closeSidebar="showSidebar = false" />
        <AddClient v-if="showAddClientForm" @addClient="addClient" @closeForm="toggleAddClientForm" />
      </div>
    </div>
  </template>

<script lang="ts">
    import { defineComponent } from "vue";
    import ClientsNavBar from '@/components/ClientsNavBar.vue';
    import ClientsList from '@/components/ClientsList.vue';
    import ClientDetailSidebar from '@/components/ClientDetailsSidebar.vue';
    import AddClient from '@/components/AddClient.vue';

    interface Client {
        id: number;
        name: string;
        about: string;
        email: string;
        phone: string;
        address: string;
        city: string;
        state: string;
        zip: string;
    }

    export default defineComponent({
    name: "ClientsView",
    components: {
        ClientsNavBar,
        ClientsList,
        ClientDetailSidebar,
        AddClient
    },
    data() {
        return {
        clients: [
            { id: 1, name: 'John Doe', about: 'His a prick', email: "prick@gmail.com", phone: "(666)666-6666", address: "123 Nowhere Street", city: "Atlanta", state: "GA", zip: "66666" },
            { id: 2, name: 'Jane Doe', about: 'Shes cheap af', email: "bitch@gmail.com", phone: "(666)666-6666", address: "123 Nowhere Street", city: "Atlanta", state: "GA", zip: "66666"  },
        ] as Client[],
        filteredClients: [] as Client[],
        selectedClient: null as Client | null,
        showSidebar: false,
        showAddClientForm: false
        };
    },
    created() {
        this.filteredClients = this.clients;
    },
    methods: {
        filterClients(searchTerm: string) {
            this.filteredClients = this.clients.filter(client =>
                client.name.toLowerCase().includes(searchTerm.toLowerCase())
            );
        },
        selectClient(client: Client) {
            this.selectedClient = client;
            this.showSidebar = true;
        },
        addClient(client: Client) {
        client.id = this.clients.length + 1;
        this.clients.push(client);
        this.filteredClients = this.clients;
        this.showAddClientForm = false;
        },
        toggleAddClientForm() {
            this.showAddClientForm = !this.showAddClientForm
        }
    },
});
    
</script>

<style scoped>
h1 {
  font-size: 4em;
  text-align: center;
}
.container {
    display: flex;
    align-items: right;
    width: 100%;
}
.main {
    width: 50%;
    padding: 2%;
}
</style>