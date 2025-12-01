<script setup>
import { makeRequest } from '../utils/make_request.js';
import { ref, computed } from 'vue';
import router from '../router/index.js';

import PinkButton from '../components/PinkButton.vue'

// For both accounts
const email = {
    name: "email",
    value: ref('')
}
const password = {
    name: "password",
    value: ref('')
}
const accType = {
    name: "accountType",
    value: ref('cupid')
}
const phone = {
    name: "phone",
    value: ref()
}
const addr = {
    name: "addr",
    value: ref('')
}
const fname = {
    name: "fname",
    value: ref('')
}
const lname = {
    name: "lname",
    value: ref('')
}
const username = {
    name: "username",
    value: ref('')
}
const desc = {
    name: "desc",
    value: ref('')
}
const imagePreview = ref("")

// Dater specific 
const relationshipStatus = ref('single')
const strengths = ref('')
const weak = ref('')
const ntype = ref('')
const interests = ref('')
const goals = ref('')
const past = ref('')

// Toast state (simple, accessible)
const toast = ref({ show: false, message: '' })
function showToast(msg, ms = 3000) {
    toast.value = { show: true, message: msg }
    setTimeout(() => (toast.value.show = false), ms)
}
function hideToast() {
    toast.value.show = false
}

// Simple password rules (client-side guidance only)
const commonPasswords = [
    'password', '123456', '123456789', 'qwerty', '12345678', '111111', '1234567'
]

const pwMinLen = computed(() => password.value.value && password.value.value.length >= 8)
const pwHasUpper = computed(() => /[A-Z]/.test(password.value.value || ''))
const pwHasLower = computed(() => /[a-z]/.test(password.value.value || ''))
const pwHasNumber = computed(() => /\d/.test(password.value.value || ''))
const pwHasSpecial = computed(() => /[^A-Za-z0-9]/.test(password.value.value || ''))
const pwNotCommon = computed(() => !commonPasswords.includes((password.value.value || '')))

const passwordValid = computed(() => pwMinLen.value && pwHasUpper.value && pwHasLower.value && pwHasNumber.value && pwHasSpecial.value && pwNotCommon.value)

async function register() {
    // Prevent submit if password doesn't meet requirements
    if (!passwordValid.value) {
        // focus the password input so the user sees the checklist
        const pwInput = document.getElementById('password')
        if (pwInput) pwInput.focus()
        return
    }

    const requiredFields = [username, email, password, accType, phone, addr, desc]

    for (let field of requiredFields) {
        if (field.value.value === '') {
            const emptyInput = document.getElementById(field.name)
            if (emptyInput) emptyInput.focus()
            showToast(`Please fill out the ${field.name} field.`)
            return
        }
    }

    try {
        if (accType.value.value === 'dater') {
            const results = await makeRequest('/api/user/create/', 'post', {
                username: username.value.value,
                first_name: fname.value.value,
                last_name: lname.value.value,
                email: email.value.value,
                password: password.value.value,
                role: accType.value.value,
                phone_number: phone.value.value,
                location: addr.value.value,
                description: desc.value.value,
                //profile_picture: image, // Crashing here
                dating_strengths: strengths.value,
                dating_weaknesses: weak.value,
                nerd_type: ntype.value,
                interests: interests.value,
                relationship_status: relationshipStatus.value,
                relationship_goals: goals.value,
                past: past.value,
            })
            if (results.user === undefined || results.user === null) {
                let errors = ""
                for (let key in results) {
                    errors += `\n${key}: ${results[key][0]}`
                }
                showToast(`Failed to create account:${errors}`)
            }
            else {
                showToast('Account created — redirecting...')
                setTimeout(() => router.push({ name: 'DaterHome', params: { id: results.user['id'] } }), 900)
            }
        }
        else {
            const results = await makeRequest('/api/user/create/', 'post', {
                username: username.value.value,
                first_name: fname.value.value,
                last_name: lname.value.value,
                email: email.value.value,
                password: password.value.value,
                role: accType.value.value,
                phone_number: phone.value.value,
                location: addr.value.value,
                description: desc.value.value,
                //profile_picture: image
            })
            if (results.user === undefined || results.user === null) {
                let errors = ""
                for (let key in results) {
                    errors += `\n${key}: ${results[key][0]}`
                }
                showToast(`Failed to create account:${errors}`)
            }
            else {
                showToast('Account created — redirecting...')
                setTimeout(() => router.push({ name: 'DaterHome', params: { id: results.user['id'] } }), 900)
            }
        }
    } catch (err) {
        // show an error toast (server-side validation failures should be shown inline ideally)
        showToast('Failed to create account')
        console.error(err)
    }
}

function previewFile() {
    let file = document.querySelector('input[type=file]').files[0];
    let reader = new FileReader();

    imagePreview.value = file

    reader.onloadend = function () {
        imagePreview.value = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
        imagePreview.value = imagePreview.value.name
        console.log(imagePreview.value)
    } else {
        imagePreview.value = "";
    }
}

</script>

<template>
    <div class="mobile-container">
        <div class="image">
            <img :src="'/get_img/'" alt="Cupid Code Logo" width="300" height="300">
        </div>
        <h1>Create Your Account!</h1>
        <form class="form" @submit.prevent="register">
            <h3>Account Type</h3>
            <div class="radios">
                <label class="radio_detail" for="cupid">
                    Cupid
                    <input
                        type="radio"
                        id="cupid"
                        name="accountType"
                        value="cupid"
                        v-model="accType.value.value"
                    />
                </label>
                <label class="radio_detail" for="dater">
                    Dater
                    <input
                        type="radio"
                        id="dater"
                        name="accountType"
                        value="dater"
                        v-model="accType.value.value"
                    />
                </label>
            </div>
            <label class="input_detail" for="fname">
                First Name*
                <input
                    type="text"
                    id="fname"
                    placeholder="First Name"
                    v-model="fname.value.value"
                />
            </label>
            <label class="input_detail" for="lname">
                Last Name*
                <input
                    type="text"
                    id="lname"
                    placeholder="Last Name"
                    v-model="lname.value.value"
                />
            </label>
            <label class="input_detail" for="username">
                Username*
                <input
                    type="text"
                    id="username"
                    placeholder="username01"
                    v-model="username.value.value"
                />
            </label>
            <label class="input_detail" for="email">
                Email*
                <input
                    type="email"
                    id="email"
                    placeholder="example@email.com"
                    v-model="email.value.value"
                />
            </label>
            <label class="input_detail" for="password">
                Password*
                <input
                    v-model="password.value.value"
                    type="password"
                    id="password"
                    placeholder="Password"
                    aria-describedby="pw-requirements" 
                />
                <div id="pw-requirements" class="pw-checklist" aria-live="polite">
                    <div><small :class="{ ok: pwMinLen, bad: !pwMinLen }">
                        ▣ At least 8 characters
                    </small></div>
                    <div><small :class="{ ok: pwHasUpper, bad: !pwHasUpper }">
                        ▣ Uppercase letter
                    </small></div>
                    <div><small :class="{ ok: pwHasLower, bad: !pwHasLower }">
                        ▣ Lowercase letter
                    </small></div>
                    <div><small :class="{ ok: pwHasNumber, bad: !pwHasNumber }">
                        ▣ Number
                    </small></div>
                    <div><small :class="{ ok: pwHasSpecial, bad: !pwHasSpecial }">
                        ▣ Special character
                    </small></div>
                    <div><small :class="{ ok: pwNotCommon, bad: !pwNotCommon }">
                        ▣ Not a common password
                    </small></div>
                </div>
            </label>
            <label class="input_detail" for="phone">
                Phone Number*
                <input
                    type="number" 
                    id="phone" 
                    placeholder="8889991111" 
                    v-model="phone.value.value" 
                />
            </label>
            <label class="input_detail" for="address">
                Address*
                <input 
                    type="text" 
                    id="address" 
                    placeholder="1300 N 400 W Example Lane" 
                    v-model="addr.value.value" 
                />
            </label>
            <label class="input_detail" for="image">
                Profile Picture
                <input type="file" id="image" name="image" @change="previewFile" />
                <img 
                    name="pfp" 
                    v-if="imagePreview" :src="imagePreview" 
                    height="100" 
                    alt="Image preview..."
                >
            </label>
            <label class="text_detail" for="desc">
                Physical Description*
                <textarea v-model="desc.value.value"></textarea>
            </label>
            <div v-if="accType.value.value === 'dater'" class="form">
                <label class="update-text" for="nerd_type">
                    Nerd Type
                    <input type="text" id="nerd_type" v-model="ntype" />
                </label>
                <fieldset class="update-text">
                    <legend>Relationship Status</legend>
                    <label class="radio_detail" for="single">
                        Single
                        <input type="radio" id="single" name="relationshipStatus" value="single"
                            v-model="relationshipStatus" />
                    </label>
                    <label class="radio_detail" for="dating">
                        Dating
                        <input type="radio" id="dating" name="relationshipStatus" value="dating"
                            v-model="relationshipStatus" />
                    </label>
                    <label class="radio_detail" for="married">
                        Married
                        <input type="radio" id="married" name="relationshipStatus" value="married"
                            v-model="relationshipStatus" />
                    </label>
                </fieldset>
                <label class="update-text" for="goals">
                    Relationship Goals
                    <textarea id="goals" v-model="goals"></textarea>
                </label>
                <label class="update-text" for="interests">
                    Interests
                    <textarea id="interests" v-model="interests"></textarea>
                </label>
                <label class="update-text" for="past">
                    Past Dating History
                    <textarea id="past" v-model="past"></textarea>
                </label>
                <label class="update-text" for="strengths">
                    Dating Strengths
                    <textarea id="strengths" v-model="strengths"></textarea>
                </label>
                <label class="update-text" for="weaknesses">
                    Dating Weaknesses
                    <textarea id="weaknesses" v-model="weak"></textarea>
                </label>
            </div>
            <PinkButton type="submit">Create Account</PinkButton>
        </form>
        <!-- Toast (non-blocking) -->
        <div v-if="toast.show" class="toast" role="status" aria-live="polite">
            <span>{{ toast.message }}</span>
            <button @click="hideToast" aria-label="Dismiss notification">×</button>
        </div>
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

.radios {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    align-items: center;
}

.radio_detail {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 8px 0;
}

.radio_detail input[type="radio"] {
    margin: 0;
    padding: 0;
    width: auto;
    border: none;
}

.input_detail {
    display: flex;
    flex-direction: column;
    padding: 8px;
    margin: 10px;
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
    border-color: var(--primary-red) !important;
}

.text_detail {
    display: flex;
    justify-content: center;
    flex-flow: column wrap;
    padding: 8px;
    margin: 10px;
    font-weight: bold;
}

.update-text {
    display: flex;
    flex-direction: column;
    padding: 16px;
}

fieldset {
    border: none;
    padding: 8px 0;
    margin: 10px 0;
}

legend {
    font-weight: bold;
    padding: 0 0 8px 0;
}

textarea {
    padding: 16px;
    width: auto;
    height: 100px;
    border: 3px rgba(128, 128, 128, 0.5) solid;
    border-radius: 16px;
}

.error {
    border: 2px var(--secondary-red) solid;
}

/* Password checklist */
.pw-checklist {
    display: flex;
    flex-direction: column;
    margin-top: 6px;
}

.pw-checklist small {
    display: inline-block;
    padding: 4px 2px;
}

.pw-checklist .ok {
    color: green;
}

.pw-checklist .bad {
    color: #b33;
}

/* Toast */
.toast {
    position: fixed;
    right: 20px;
    top: 20px;
    background: #222;
    color: #fff;
    padding: 12px 16px;
    border-radius: 6px;
    display: flex;
    gap: 12px;
    align-items: center;
    z-index: 1000;
}

.toast button {
    background: transparent;
    color: #fff;
    border: none;
    font-size: 18px;
    cursor: pointer;
}
</style>
