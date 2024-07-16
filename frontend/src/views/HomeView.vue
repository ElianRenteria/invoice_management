<template>
  <div class="main">
    <Image :src="require('@/assets/placeholder.png')" alt="Image" width="750" />
    <h1 class="main-title">Best <span class="highlight">Invoice Manager</span> for Contractors</h1>
    <p class="main-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
    <Button @click="routeToSignUp" label="Get Started" severity="info" class="main-button"/>
  </div>
  
  <div class="stats">
    <div class="stats-item">
      <Knob v-model="value1" valueTemplate="50%" :size="180" readonly/>
      <h3 class="stat-description">Increase in productivity</h3>
    </div>
    <div class="stats-item">
      <Knob v-model="value2" valueTemplate="$10" :size="180" readonly/>
      <h3 class="stat-description">Savings</h3>
    </div>
    <div class="stats-item">
      <Knob v-model="value" :valueTemplate="`${value}`" :size="180" readonly/>
      <h3 class="stat-description">Already</h3>
    </div>
  </div>

  <h2 class="feature-title">Main Features</h2>
  <div class="features">
    <Accordion :activeIndex="0">
      <AccordionTab header="Quickly Make New Estimates">
          <p class="m-0">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
              consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
              laborum.
          </p>
      </AccordionTab>
      <AccordionTab header="Service Templates">
          <p class="m-0">
              Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo
              enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci velit, sed quia non numquam eius modi.
          </p>
      </AccordionTab>
      <AccordionTab header="Effective Client Manager">
          <p class="m-0">
              At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in
              culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
          </p>
      </AccordionTab>
      <AccordionTab header="Easy to use Business Management Tools">
          <p class="m-0">
              At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in
              culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus.
          </p>
      </AccordionTab>
    </Accordion>
  </div>
  <Footer />
</template>

<script lang="ts">
import { ref } from 'vue';
import Knob from 'primevue/knob';
import Image from 'primevue/image';
import Button from 'primevue/button';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import Footer from '@/components/Footer.vue';

export default {
  name: 'HomeView',
  components: {
    Image,
    Knob,
    Button,
    Accordion,
    AccordionTab,
    Footer,
  },
  setup() {
    const value1 = ref(50);
    const value2 = ref(10);
    const value = ref(30);

    function routeToSignUp() {
      // Replace with your actual routing logic
      console.log('Navigate to signup page');
    }

    return {
      value1,
      value2,
      value,
      routeToSignUp,
    };
  },
};
</script>

<style>
.main {
  margin: 3%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: 8% 27%;
}

.main-title {
  font-size: 4em;
  text-align: center;
}

.main-description {
  font-size: 1.2em;
}

.main-button {
  margin: 3%;
}

.stats {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  color: rgb(0, 140, 255);
}

.stat-description {
  font-size: 1em;
  text-align: center;
}

.feature-title {
  font-size: 3em;
  text-align: center;
  margin: 5%;
}

.features {
  margin: 10% 20%;
  border: 2px solid rgb(0, 140, 255);
  border-radius: 5px;
}

.highlight {
  color: rgb(0,212,255);
  color: linear-gradient(90deg, rgba(0,212,255,1) 0%, rgb(105, 210, 252) 22%, rgb(0, 64, 184) 100%);
}
</style>
