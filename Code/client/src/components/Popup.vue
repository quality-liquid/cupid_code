<script setup>
    import {ref, onMounted} from 'vue'

    const popupActive = ref(false)
</script>
<template>
    <div class="popup" data-active="false">
        <slot />
    </div>
</template>
<style scoped>
    .popup {
        position: fixed;
        width: clamp(220px, 50%, 400px);
        height: fit-content;
        margin: auto;
        padding-left: 16px;
        padding-right: 16px;
        left:0;
        right:0;
        top: 30%;

        transform: scale(0);
        transition: transform 0.2s cubic-bezier(0,1,1,1);

        display: flex;
        flex-direction: column;
        align-content: flex-end;
        background-color: var(--secondary-blue);
        border: 3px solid var(--primary-red);
        color: white;
    }

    .popup[data-active="true"] {
        transform: scale(1);
        transition: transform 0.2s cubic-bezier(0,1.4,1,1);
    }

</style>
