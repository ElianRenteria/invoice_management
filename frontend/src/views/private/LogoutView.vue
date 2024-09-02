<template>

</template>
<script setup lang="ts">
    import { useRouter } from 'vue-router';
    const router = useRouter();
    onMounted(() => {
        localStorage.removeItem('access_token');
        router.push('/login');
    });
</script>