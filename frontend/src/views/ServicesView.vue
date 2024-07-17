<template>
    <div class="container">
        <SearchBarHeader />
        <services />
    </div>
</template>

<script setup lang="ts">
    import SearchBarHeader from "@/components/SearchBarHeader.vue";
    import services from "@/components/services.vue";
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