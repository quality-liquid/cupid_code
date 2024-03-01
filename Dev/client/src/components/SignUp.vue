<script setup>
import { makeRequest } from '../utils/make_request.js';
import {ref} from 'vue';

const currPath = ref(window.location.hash);

// For both accounts
const email = ref('')
const password = ref('')
const accType = ref('')
const phone = ref()
const addr = ref('')
const fname = ref('')
const lname = ref('')
const username = ref('')
const desc = ref('')
let image = null 

// Dater specific - 
const str = ref('')
const weak = ref('')
const ntype = ref('')
const interests = ref('')
const goals = ref('')
const past = ref('')

async function register() {
    // Validate data
    image = document.querySelector('img[name=pfp]');
    const checkData = [email, password, accType, phone, addr]

    let check = 0;
    for (let i = 0; i < checkData.length; i++) {
        if (checkData[i] !== '') check++;
        else {
            const error = document.querySelector(`input[name=${checkData[i]}]`);
            error.class = error.class + 'error';
        }
    }

    if (accType.value === 'Dater' && check === checkData.length) {
        const results = await makeRequest('/sign_up/', 'post', {
            username: username.value,
            first_name: fname.value,
            last_name: lname.value,
            email: email.value,
            password: password.value,
            user_type: accType.value,
            phone_number: phone.value,
            location: addr.value,
            description: desc.value,
            //profile_picture: image,
            dating_strengths: str.value,
            dating_weakness: weak.value,
            nerd_type: ntype.value,
            relationship_goals: goals.value,
            past: past.value
        })
        
        window.addEventListener('hashchange', () => {
            currPath.value = '#/home';
        })
    }
    else if (accType.value === 'Cupid' && check === checkData.length) {
        await makeRequest('/sign_up/', 'post', {
            username: username.value,
            first_name: fname.value,
            last_name: lname.value,
            email: email.value,
            password: password.value,
            user_type: accType.value,
            phone_number: phone.value,
            location: addr.value,
            description: desc.value,
            //profile_picture: image
        })
        window.addEventListener('hashchange', () => {
            currPath.value = '#/home';
        })
    }
    else {
        console.log("Something went wrong")
    }

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
            <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
        </div>
        <h1>Create Your Account!</h1>
        <form class="form" @submit.prevent="register">
            <h3>Account Type</h3>
            <div class="radios">
                <label class="radio_detail" for="cupid">
                    Cupid 
                </label>
                <input type="radio" id="cupid" name="accountType" :value="accType" @change="(e) => accType = 'Cupid'"/>
                <label class="radio_detail" for="dater">
                    Dater
                </label>
                <input type="radio" id="dater" name="accountType" :value="accType" @change="(e) => accType = 'Dater'"/>
            </div>
            <label class="input_detail" for="fname">
                First Name
                <input type="text" id="fname" placeholder="First Name" :value="fname" @change="(e) => fname = e.target.value"/>
            </label>
            <label class="input_detail" for="lname">
                Last Name
                <input type="text" id="lname" placeholder="Last Name" :value="lname" @change="(e) => lname = e.target.value"/>
            </label>
            <label class="input_detail" for="username">
                Username
                <input type="text" id="username" placeholder="username01" :value="username" @change="(e) => username = e.target.value"/>
            </label>
            <label class="input_detail" for="email">
                Email
                <input type="email" id="email" placeholder="example@email.com" :value="email" @change="(e) => email = e.target.value"/>
            </label>
            <label class="input_detail" for="password">
                Password
                <input type="password" id="password" placeholder="Password" :value="password" @change="(e) => password = e.target.value"/>
            </label>
            <label class="input_detail" for="fname">
                Phone Number
                <input type="number" id="fname" :value="phone" placeholder="8889991111" @change="(e) => phone = e.target.value"/>
            </label>
            <label class="input_detail" for="address">
                Address
                <input type="text" id="address" :value="addr" placeholder="1300 N 400 W Example Lane" @change="(e) => addr = e.target.value"/>
            </label>
            <label class="input_detail" for="image">
                Profile Picture
                <input type="file" id="image" name="image" @change="previewFile"/>
                <img name="pfp" src="" height="100" alt="Image preview...">
            </label>
            <label class="text_detail" for="desc">
                Physical Description
                <textarea :value="desc" id="desc" @change="(e) => desc = e.target.value"></textarea>
            </label>
            <div v-if="accType === 'Dater'" class="form">
                <label class="input_detail" for="nerd_type">
                    Nerd Type
                    <input type="text" id="nerd_type" :value="ntype" @change="(e) => ntype = e.target.value"/>
                </label>
                <label class="text_detail" for="goals">
                    Relationship Goals
                    <textarea :value="goals" id="goals" @change="(e) => goals = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="interests">
                    Interests
                    <textarea :value="interests" id="interests" @change="(e) => interests = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="past">
                    Past Dating History
                    <textarea :value="past" id="past" @change="(e) => past = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="strengths">
                    Dating Strengths
                    <textarea :value="str" id="strengths" @change="(e) => str = e.target.value"></textarea>
                </label>
                <label class="text_detail" for="weaknesses">
                    Dating Weaknesses
                    <textarea :value="weak" id="weaknesses" @change="(e) => weak = e.target.value"></textarea>
                </label>
            </div>
            <button class="button">Create Account</button>
        </form>
    </div>
</template>


<style scoped>
    h1 {
        text-align: center;
    }

    h3 {
        text-align: center;
    }

    .form {
        display: flex;
        flex-flow: column wrap;
    }
    .image {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    .button {
        width: auto;
        background-color: var(--primary-red);
        border-radius: 10px;
        color: white;
        border: none;
        border-radius: 4px;
        box-shadow: 5px 5px 2px rgba(128, 128, 128, 0.5);
        text-decoration: solid;
    }

    .radios {
        display: flex;
        flex-flow: row wrap;
        justify-content: center;
        align-items: center;
    }
    .radio_detail {
        display: flex;
    }
    .input_detail {
        display: flex;
        flex-direction: column;
        padding: 8px;
        font-weight: bold;
    }
    input {
        border: 3px rgba(128, 128, 128, 0.5) solid;
        border-radius: 4px;
        width: auto;
        padding: 8px;
        margin: 10px;
    }
    input[type="file"] {
        border: none;
    }
    input[name="accountType"] {
        display: flex;
        border: none;
        color: var(--secondary-red);
    }
    input:focus {
        border-color: var(--primary-red)!important;
    }

    .text_detail {
        display: flex;
        justify-content: center;
        flex-flow: column wrap;
        padding: 8px;
        margin: 10px;
        font-weight: bold;
    }
    
    textarea {
        padding: 16px;
        width: auto;
        height: 100px;
        border: 3px rgba(128, 128, 128, 0.5) solid;
        border-radius: 16px;
    }
    .button {
        margin: 10px;
        padding: 16px;
        border: none;
        border-radius: 8px;
    }
    .error {
        border: 2px var(--secondary-red) solid;
    }
</style>
