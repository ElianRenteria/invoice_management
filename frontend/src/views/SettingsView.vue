<template>
    <div class="container">
        <SearchBarHeader />
    </div>
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import SearchBarHeader from "@/components/SearchBarHeader.vue";

    export default defineComponent({
    name: "SettingsView",
    components: {
        SearchBarHeader,
    },
    });
</script>
<style scoped>
    .container {
        background-color: #140a2c;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: start;
        width: 100%;
        height: 100%;
        padding: 0%;
        margin: 0%;
    }
</style>