<script setup>
import { ref, onMounted } from 'vue';
import router from '../router/index';
import { makeRequest } from '../utils/make_request';

import NavSuite from '../components/NavSuite.vue';
import { loadStripe } from '@stripe/stripe-js';

const user_id = parseInt(window.location.hash.split('/')[3])

const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY)

const stripe = ref(null)

const balance = ref(0)
const amount = ref(0)
const clientSecret = ref('')
const elementsRef = ref(null)

const returnUrl = `${window.location.origin.split('?')[0]}/#/dater/balance/${user_id}`
console.log(returnUrl)

async function addFunds() {
    const res = await makeRequest(`/api/dater/payment/${user_id}/`, 'post', {
        amount: amount.value
    })
    clientSecret.value = res.client_secret
        // Build Stripe appearance using app CSS variables so the Payment Element matches
        // the app color palette and adapts to dark mode where possible.
        function cssVar(name, fallback) {
            try {
                const v = getComputedStyle(document.documentElement).getPropertyValue(name)
                if (v) return v.trim()
            } catch (e) {
                // ignore
            }
            return fallback
        }

        function getStripeAppearance() {
            const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
            // Common app variables used across components
            const colorPrimary = cssVar('--secondary-red', '#e55353')
            const colorBackground = cssVar('--primary-white', prefersDark ? '#0b0b0b' : '#ffffff')
            const colorText = cssVar('--primary-foreground', prefersDark ? '#f6f6f6' : '#111115')
            const colorDanger = cssVar('--destructive', '#ff4d4f')
            const colorBorder = cssVar('--accent', prefersDark ? '#2b2b2b' : '#e6e6e6')
            const colorPlaceholder = cssVar('--secondary-blue', '#6b7280')

            return {
                theme: 'stripe',
                variables: {
                    colorPrimary,
                    colorBackground,
                    colorText,
                    colorDanger,
                    colorBorder,
                    colorPlaceholder,
                    fontFamily: cssVar('--font-family', 'Inter, system-ui, sans-serif'),
                    borderRadius: cssVar('--radius', '8px'),
                },
                rules: {
                    '.Label': { color: colorText },
                    '.Input, .Block': { color: colorText, background: colorBackground },
                    '.Input::placeholder': { color: colorPlaceholder },
                },
            }
        }

        const options = {
            clientSecret: clientSecret.value,
            appearance: getStripeAppearance(),
        };
    // initialize Elements and mount the Payment Element
    elementsRef.value = stripe.value.elements(options)
    const paymentElementOptions = { layout: 'accordion' };
    const paymentElement = elementsRef.value.create('payment', paymentElementOptions);
    paymentElement.mount('#payment-element');
    const paymentForm = document.getElementById('payment-form')
    if (!paymentForm.querySelector('button[type="submit"]')) {
        const button = document.createElement('button')
        button.type = 'submit'
        button.textContent = 'Submit Payment'
        button.className = 'button'
        paymentForm.appendChild(button)
    }
}

async function getMoney() {
    const results = await makeRequest(`/api/dater/balance/${user_id}`)
    balance.value = results.balance
}

async function submitPayment() {
    const { error } = await stripe.value.confirmPayment({
        // `Elements` instance that was used to create the Payment Element
        elements: elementsRef.value,
        confirmParams: { return_url: returnUrl },
    });
    if (error) {
        // This point will only be reached if there is an immediate error when
        // confirming the payment. Show error to your customer (for example, payment
        // details incomplete)
        console.log(error.message);
    } else {
        router.push({ name: 'CupidCash', params: { id: user_id } });
    }
}

onMounted(async () => {
    try {
        await getMoney()
    } catch (error) {
        console.error('Error fetching money:', error)
    }
    try {
        stripe.value = await stripePromise
        if (!stripe.value) {
            console.error('Stripe.js failed to load.')
            return
        }
    }
    catch (error) {
        console.error('Error loading Stripe.js:', error)
    }
})
</script>

<template>
    <NavSuite title='Add Cash' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterHome', params: { id: user_id } }"> Home </router-link>
        <router-link class="link" :to="{ name: 'DaterProfile', params: { id: user_id } }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: { id: user_id } }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: { id: user_id } }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: { id: user_id } }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'DaterGigs', params: { id: user_id } }"> Gigs </router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: { id: user_id } }"> Feedback </router-link>
    </NavSuite>
    <div class="mobile-container">
        <h1>{{ 'Current balance: $' + balance }}</h1>
        <form class="container clamped" @submit.prevent="addFunds">
            <div class="oneline">
                <input type="number" min="0" id="amount" v-model="amount" />
                <button class="button">Deposit</button>
            </div>
        </form>
        <form @submit.prevent="submitPayment" id="payment-form" class="container clamped">
            <div id="payment-element">
                <!--Stripe.js injects the Payment Element-->
            </div>
        </form>
    </div>
</template>

<style scoped>
.container h1 {
    margin-top: 0px;
    text-align: center;
}

.container {
    display: flex;
    justify-content: center;
    align-content: center;
    margin-left: 0px;
    margin-right: 0px;
    flex-direction: column;
}

.input-container input {
    border: none;
    box-sizing: border-box;
    outline: 0;
    padding: 12px;
    width: 100%;
}

.oneline {
    display: flex;
    flex-direction: row;
}

select,
.oneline>input {
    margin: auto;
    display: flex;
    border: 1px solid rgb(139, 139, 139);
    border-radius: 4px;
    padding: 12px;
    color: rgb(139, 139, 139);
    width: 100%;
}

select {
    color: black;
}

.center {
    display: flex;
    flex-direction: column;
    align-content: center;
}

.center>* {
    margin: auto;
}

.clamped {
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
}

.details input {
    display: flex;
    margin: 4px;
    border: 1px solid rgb(139, 139, 139);
    gap: 8px;
    border-radius: 4px;
    padding: 16px;
    color: rgb(139, 139, 139);
}

.date {
    display: flex;
    flex-direction: row;
}

.button {
    display: flex;
    justify-content: center;
    align-content: center;
    border: none;
    border-radius: 8px;
    padding: 16px;
    margin: 10px;
    color: white;
    background-color: var(--secondary-red);
}

input:focus {
    border-color: var(--secondary-red);
}
</style>
