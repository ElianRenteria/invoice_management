<template>
  <div class="add-client-form">
    <h3>Add New Client</h3>
    <form @submit.prevent="onSubmit">

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="name" placeholder="name" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="about" placeholder="about" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="email" placeholder="email" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="phone" placeholder="phone" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="address" placeholder="address" size="small" type="text" required/>
      </InputGroup>
      
      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="city" placeholder="city" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="state" placeholder="state" size="small" type="text" required/>
      </InputGroup>

      <InputGroup>
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="zip" placeholder="zip" size="small" type="text" required/>
      </InputGroup>

      <div>
        <Button label="Add" type="submit" severity="help" rounded />
        <Button label="Cancel" @click="onClose" type="button" severity="help" rounded />
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
export default defineComponent({
  name: 'AddClientComponent',
  components: {
    InputText,
    Button,
    InputGroup,
    InputGroupAddon
  },
  data() {
    return {
      name: '',
      about: '',
      email: '',
      phone: '',
      address: '',
      city: '',
      state: '',
      zip: '',
    };
  },
  methods: {
    onSubmit() {
      const newClient = {
        id: 0, 
        name: this.name,
        about: this.about,
        email: this.email,
        phone: this.phone,
        address: this.address,
        city: this.city,
        state: this.state,
        zip: this.zip
      };
      this.$emit('addClient', newClient);
      this.resetForm();
    },
    onClose() {
      this.$emit('closeForm');
      this.resetForm();
    },
    resetForm() {
      this.name = '';
      this.about = '';
      this.email = '';
      this.phone = '';
      this.address = '';
      this.city = '';
      this.state = '';
      this.zip = ''
    }
  }
});
</script>

<style scoped>
.add-client-form {
  width: 50%;
  padding: 10px;
  background-color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.add-client-form form {
  display: flex;
  flex-direction: column;
}
.add-client-form form div {
  margin-bottom: 10px;
}
</style>
