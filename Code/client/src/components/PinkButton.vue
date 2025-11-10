<script setup>
defineProps({
    id: String
})
</script>
<template>
    <button :id="id" @click="$emit('click-forward')"><slot /></button>
</template>
<style scoped>
    button {
        margin-left: 3px;
        margin-right: 3px;
        background-color: var(--primary);
        border-radius: var(--radius);
        color: var(--primary-foreground);
        border: none;
        box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
        text-decoration: solid;
        padding: 16px;
        margin: auto;
        display: flex;
        justify-self: center;
        align-self: center;
        user-select: none;
        transition: all 0.2s;
    }

    button:hover {
        filter: brightness(0.9);
    }

    button:active {
        filter: brightness(0.7);
        transform: translate(3px,3px);
        box-shadow: 3px 3px 1px rgba(0, 0, 0, 0.4);
    }
</style>
