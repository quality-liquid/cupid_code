<script setup>
    return function openDrawer() {
        const element = document.getElementById('navbar')
        if (element.className === 'navbar') {
            element.className = 'navbar opened'
        }
        else {
            element.className = 'navbar'
        }
    }
</script>
<template>
    <div id="navbar" class="navbar">

    </div>
</template>
