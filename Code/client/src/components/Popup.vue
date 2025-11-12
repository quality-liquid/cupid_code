<script setup>
import { defineProps } from 'vue'

const props = defineProps({
    dataActive: {
        type: Boolean,
        default: false,
    },
})
</script>

<template>
    <!-- Full-screen overlay behind the popup -->
    <div class="popup-overlay" :data-active="dataActive"></div>

    <div class="popup" :data-active="dataActive">
        <slot />
    </div>
</template>

<style scoped>
    .popup-overlay {
        position: fixed;
        inset: 0; /* top:0; right:0; bottom:0; left:0 */
        background-color: rgba(0, 0, 0, 0.75); /* solid-ish background */
        opacity: 0;
        transition: opacity 0.15s ease;
        pointer-events: none;
        z-index: 9998; /* sit below the popup itself */
    }

    .popup-overlay[data-active="true"] {
        opacity: 1;
        pointer-events: auto;
    }

    .popup {
        position: fixed;
        width: clamp(220px, 50%, 400px);
        height: fit-content;
        margin: auto;
        padding-left: 16px;
        padding-right: 16px;
        left: 0;
        right: 0;
        top: 30%;

        transform: scale(0);
        transition: transform 0.2s cubic-bezier(0, 1, 1, 1);

        display: flex;
        flex-direction: column;
        align-content: flex-end;
        background-color: var(--secondary-blue);
        border: 3px solid var(--primary-red);
        color: white;
        z-index: 9999; /* ensure popup is above everything */
    }

    .popup[data-active="true"] {
        transform: scale(1);
        transition: transform 0.2s cubic-bezier(0, 1.4, 1, 1);
    }

</style>
