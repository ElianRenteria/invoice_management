<template>
    <div id="app">
      <ClientsNavBar @search="filterClients" @addClient="addClient" />
      <div class="container">
        <ClientsList :clients="filteredClients" @selectClient="selectClient" />
        <ClientDetailSidebar :client="selectedClient" v-if="showSidebar" @closeSidebar="showSidebar = false" />
      </div>
    </div>
  </template>

<script lang="ts">
    import { defineComponent } from "vue";
    import ClientsNavBar from '@/components/ClientsNavBar.vue';
    import ClientsList from '@/components/ClientsList.vue';
    import ClientDetailSidebar from '@/components/ClientDetailsSidebar.vue';

    interface Client {
        id: number;
        name: string;
        details: string;
    }

    export default defineComponent({
    name: "ClientsView",
    components: {
        ClientsNavBar,
        ClientsList,
        ClientDetailSidebar
    },
    data() {
        return {
        clients: [
            // Sample data for clients
            { id: 1, name: 'Client 1', details: 'Details about Client 1' },
            { id: 2, name: 'Client 2', details: 'Details about Client 2' },
            // Add more clients as needed
        ] as Client[],
        filteredClients: [] as Client[],
        selectedClient: null as Client | null,
        showSidebar: false
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
        addClient() {
        const newClient: Client = {
            id: this.clients.length + 1,
            name: `Client ${this.clients.length + 1}`,
            details: `Details about Client ${this.clients.length + 1}`
        };
        this.clients.push(newClient);
        this.filteredClients = this.clients;
        }
    },
});
    
</script>

<style>
.container {
  display: flex;
}
</style>