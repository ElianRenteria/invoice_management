<template>
  <div class="main">
    <Image :src="require('../assets/placeholder.png')" alt="Image" width="750" />
    <h1 class="title">Best <span class="highlight">Invoice Manager</span> for Contractors</h1>
    <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
    <Button @click="routeToSignUp" label="Get Started" severity="info" class="main-button"/>
  </div>
  
  <div class="stats">
    <div class="stats-item">
      <Knob v-model="value1" valueTemplate="50%" :size="180" readonly/>
      <h3 class="description">Increase in productivity</h3>
    </div>
    <div class="stats-item">
      <Knob v-model="value2" valueTemplate="$10" :size="180" readonly/>
      <h3 class="description">Savings</h3>
    </div>
    <div class="stats-item">
      <Knob v-model="value" valueTemplate="{value}" :size="180" readonly/>
      <h3 class="description">Already</h3>
    </div>
  </div>

  <div class="features">
    <h2>Main Features</h2>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Knob from 'primevue/knob';
import Image from 'primevue/image';
import Button from 'primevue/button';

export default defineComponent({
  name: "HomeView",
  components: {
    Image,
    Knob,
    Button
  },
  methods: {
    routeToSignUp() {
      this.$router.push({name: 'signup'});
    }
  },
  data: function(){
    return {
      value1: 50,
      value2: 10,
      value: 30
    }
  }
});
</script>
<style>
.main {
  margin: 3%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.stats {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  color: rgb(0, 140, 255);
}

.description {
  font-size: 1em;
  text-align: center;
}

.title {
  font-size: 4em;
}

.description {
  font-size: 1.2em;
}

.highlight {
  color: rgb(0,212,255);
  color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
}

.main-button {
  margin: 3%;
}
</style>