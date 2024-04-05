<script setup>
</script>
<template>
    <button @click="$emit('click-forward')"><slot /></button>
</template>
<style>
    button {
        margin-left: 3px;
        margin-right: 3px;
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
        box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
        text-decoration: solid;
        padding: 16px;
        margin: 10px;
        user-select: none;
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
