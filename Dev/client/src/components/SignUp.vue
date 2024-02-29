<script setup>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

const props = defineProps(['routes'])

// For both accounts
const email = ref('')
const password = ref('')
const accType = ref('')
const phone = ref()
const addr = ref('')
const image = null 

// Dater specific
const str = ref('')
const weak = ref('')
const ntype = ref('')
const interests = ref('')
const goals = ref('')
const past = ref('')

console.log(accType)

async function register() {
    // Validate data
    image = document.querySelector('img[name=pfp]')
    if (accType.toLowerCase === 'dater') {
        await makeRequest('/sign_in/', 'post', {
            email: email,
            password: password,
            role: accType,
            phone_number: phone,
            location: addr,
            profile_picture: image,
            dating_strengths: str,
            dating_weakness: weak,
            nerd_type: ntype,
            relationship_goals: goals,
            past: past
        })
    }
    else {
        await makeRequest('/sign_in/', 'post', {
            email: email,
            password: password,
            role: accType,
            phone_number: phone,
            location: addr,
            profile_picture: image
        })
    }
    // Redirect to dashboard
    
}

function previewFile() {
  let preview = document.querySelector('img[name=pfp]');
  let file = document.querySelector('input[type=file]').files[0];
  let reader = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}

</script>

<template>
    <div class="container">
        <div class="image">
            <img :src="'/get_img/'" alt="Cupid Code Logo" width="400" height="400">
        </div>
        <form class="form">
            <h1>Create Your Account!</h1>
            <div class="radios">
                <h3>Account Type</h3>
                <label class="radio_detail" for="cupid">
                    Cupid 
                    <input type="radio" id="cupid" name="accountType" :value="accType" @change="(e) => accType = 'cupid'"/>
                </label>
                <label class="radio_detail" for="dater">
                    Dater
                    <input type="radio" id="dater" name="accountType" :value="accType" @change="(e) => accType = 'dater'"/>
                </label>
            </div>
            <label class="input_detail" for="email">
                Email
                <input type="email" :value="email" @change="(e) => email = e.target.value"/>
            </label>
            <label class="input_detail" for="password">
                Password
                <input type="password" :value="password" @change="(e) => password = e.target.value"/>
            </label>
            <label class="input_detail" for="fname">
                Phone Number
                <input type="number" :value="phone" @change="(e) => phone = e.target.value"/>
            </label>
            <label class="input_detail" for="image">
                Profile Picture
                <input type="file" name="image" @change="previewFile"/>
                <img name="pfp" src="" height="200" alt="Image preview...">
            </label>
            <label class="input_detail" for="address">
                Address
                <input type="text" :value="addr" @change="(e) => addr = e.target.value"/>
            </label>
            <div v-if="accType === 'dater'" class="form">
                <label class="input_detail" for="nerd_type">
                    Nerd Type
                    <input type="text" :value="ntype" @change="(e) => ntype = e.target.value"/>
                </label>
                <label class="text_detail" for="goals">
                    Relationship Goals
                    <textarea :value="goals" @change="(e) => goals = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="interests">
                    Interests
                    <textarea :value="interests" @change="(e) => interests = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="past">
                    Past Dating History
                    <textarea :value="past" @change="(e) => past = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="strengths">
                    Dating Strengths
                    <textarea :value="str" @change="(e) => str = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="weaknesses">
                    Dating Weaknesses
                    <textarea :value="weak" @change="(e) => weak = e.target.value"></textarea>
                </label>
            </div>
            <button class="button" @click="register">Create Account</button>
        </form>
    </div>
</template>


<style scoped>
    h1 {
        margin: 30px;
    }

    .image {
        display: flex;
        margin-top: 50px;
        border-radius: 16px;
    }
    .button {
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
    }
    .container {
        margin: auto;
        padding: 10px;
    }
    .form {
        display: flex;
        flex-flow: column wrap;
        justify-content: center;
        align-items: center;
        background-color: var(--secondary-blue);
        border-radius: 16px;
        color: white;
        margin-top: 20px;
    }
    .radios {
        display: flex;
        flex-flow: column wrap;
        margin-bottom: 8px;
    }
    .radio_detail {
        display: flex;
        padding: 4px;
        align-items: center;
        justify-content: center;
    }
    .input_detail {
        margin: 4px;
        text-align: center;
    }

    input {
        display: flex;
        flex-direction: column;
        border: none;
        padding: 16px;
        border-radius: 8px;
        margin: 8px;
    }

    input[name="accountType"] {
        display: flex;
        border: none;
        color: var(--secondary-red);
    }

    input[name="image"] {
        display: flex;
    }
    .text_detail {
        display: flex;
        justify-content: center;
        flex-flow: column wrap;
        padding: 8px;
        margin: 10px;
    }
    
    textarea {
        padding: 16px;
        margin: 8px;
        width: 100px;
        height: 100px;
    }
    .button {
        margin: 10px;
        padding: 16px;
        border: none;
        border-radius: 8px;
    }
    .error {
        border: 4px var(--secondary-red) solid;
    }
</style>
