<script setup>
    import {ref, onMounted} from 'vue';
    import router from '../router/index';
    import { makeRequest } from '../utils/make_request';

    import NavSuite from '../components/NavSuite.vue';
    import PinkButton from '../components/PinkButton.vue';

    const email = ref('')
    const phone = ref()
    const addr = ref('')
    const fname = ref('')
    const lname = ref('')
    const username = ref('')
    const desc = ref('')
    let image = null 
    const str = ref('')
    const weak = ref('')
    const ntype = ref('')
    const interests = ref('')
    const goals = ref('')
    const past = ref('')
    const degree = ref('')

    // Allow user to change password
    const oldPassword = ref('')
    const newPassword = ref('')
    const newPassword2 = ref('')
    
    const user_id  = parseInt(window.location.hash.split('/')[3])

    function previewFile() {
        let preview = document.querySelector('img[name=pfp]');
        let file = document.querySelector('input[type=file]').files[0];
        let reader = new FileReader();
        
        image = file

        reader.onloadend = function () {
            preview.src = reader.result;
        }

        if (file) {
            reader.readAsDataURL(file);
        } else {
            preview.src = "";
        }
    }

    async function getData() {
        // dater results
        const results = await makeRequest(`api/user/${user_id}`)
        degree.value = results.ai_degree
        addr.value = results.location
        desc.value = results.description
        str.value = results.dating_strengths
        weak.value = results.dating_weaknesses
        ntype.value = results.nerd_type
        interests.value = results.interests
        goals.value = results.relationship_goals
        past.value = results.past

        // user results
        email.value = results.user['email']
        fname.value = results.user['first_name']
        lname.value = results.user['last_name']
        phone.value = results.user['phone_number']
        username.value = results.user['username']
    }

    async function update() {
        // Validate data
        const checkData = [email, phone, addr, desc]

        let check = 0;
        for (let i = 0; i < checkData.length; i++) {
            if (checkData[i] !== '') check++;
            else {
                const error = document.querySelector(`input[name=${checkData[i]}]`);
                error.class = error.class + 'error';
            }
        }
        const results = await makeRequest(`/api/dater/profile/`, 'post', {
            username: username.value,
            first_name: fname.value,
            last_name: lname.value,
            email: email.value,
            phone_number: phone.value,
            location: addr.value,
            description: desc.value,
            //profile_picture: image,
            dating_strengths: str.value,
            dating_weaknesses: weak.value,
            nerd_type: ntype.value,
            interests: interests.value,
            relationship_goals: goals.value,
            past: past.value,
        })
        router.push({name: 'DaterProfile', params: {id: user_id}});
    }
    
    async function updatePassword() {
        if (newPassword.value === newPassword2.value) console.log("Still not a feature")
        console.log("Not a feature currently")
    }

    onMounted(getData)

</script>

<template>
    <NavSuite title='Profile' profile='DaterProfile'>
        <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
        <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }"> Calendar </router-link>
        <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
        <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
        <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
        <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}"> Feedback </router-link>
    </NavSuite>

    <form class="container" @submit.prevent="update">
        <h2 class="top">Personal Information</h2>      
        <div class="personal">
            <label class="update-content" for="fname">
                First Name
                <input type="text" id="fname" v-model="fname"/>
            </label>
            <label class="update-content" for="lname">
                Last Name
                <input type="text" id="lname" v-model="lname"/>
            </label>
            <label class="update-content" for="phone">
                Phone Number
                <input type="number" id="phone" v-model="phone"/>
            </label>
            <label class="update-content" for="address">
                Address
                <input type="text" id="address" v-model="addr"/>
            </label>
            <label class="update-content" for="degree">
                AI Degree
                <select id="degree" v-model="degree" class="update-select">
                    <option value="I don't want any help">I don't want any help</option>
                    <option value="I would like a little help">I would like a little help</option>
                    <option value="I need a good amount of help">I need a good amount of help</option>
                    <option value="I need all the help">I need all the help</option>
                </select>
            </label>
        </div>
        <h2>User Information</h2>
        <div class="userinfo">
            <label class="update-content" for="username">
                Username
                <input type="text" id="username" v-model="username"/>
            </label>
            <label class="update-content" for="email">
                Email
                <input type="email" id="email" v-model="email"/>
            </label>
        </div>
        <h2> Details about you! </h2>
        <div class="details">
            <label class="update-text" for="desc">
                Physical Description
                <textarea id="desc" v-model="desc"></textarea>
            </label>
            <label class="update-content" for="nerd_type">
                Nerd Type
                <input type="text" id="nerd_type" v-model="ntype"/>
            </label>
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
                <textarea id="strengths" v-model="str"></textarea>
            </label>
            <label class="update-text" for="weaknesses">
                Dating Weaknesses
                <textarea id="weaknesses" v-model="weak"></textarea>
            </label>
        </div>
        <label class="update-content" for="image">
            Profile Picture
            <input type="file" id="image" name="image" @change="previewFile"/>
            <img name="pfp" src="" height="200" alt="Image preview...">
        </label>
        <PinkButton> Update/Save changes </PinkButton>
    </form>
    <form class="container" @submit.prevent="updatePassword">
        <h2> Update Password </h2>
        <!-- Make it so they have to update the password w/ old, new, repeated new. -->
        <label class="update-content" for="old-password">
            Old Password
            <input type="password" id="old-password" v-model="oldPassword"/>
        </label>
        <label class="update-content" for="new-password">
            New Password
            <input type="password" id="new-password" v-model="newPassword">
        </label>
        <label class="update-content" for="new-password-2">
            Repeat New password
            <input type="password" id="new-password-2" v-model="newPassword2"/>
        </label>
        <PinkButton> Update Password </PinkButton>
    </form>
</template>

<style scoped>

h2 {
    margin: 5px;
    color: var(--secondary-blue);
}

.top {
    margin-top: 50px;
}

.container {
    color: var(--primary-blue);
    text-decoration: bold;
    margin-bottom: 10px;
}

.personal {
    display: flex;
    flex-direction: column;
}

.details {
    display: flex;
    flex-direction: column;
}

.update-content {
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

.update-text {
    display: flex;
    justify-content: center;
    flex-flow: column wrap;
    padding: 8px;
    margin: 10px;
    font-weight: bold;
}

textarea {
    padding: 16px;
    margin: 10px;
    width: auto;
    height: 100px;
    border: 3px rgba(128, 128, 128, 0.5) solid;
    border-radius: 16px;
}

.update-select {
    padding: 8px;
    border: 3px rgba(128, 128, 128, 0.5) solid;
    border-radius: 8px;
    margin: 10px;
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
    padding: 16px;
    margin: 10px;
    display: flex;
    justify-self: center;
    align-self: center;
}
</style>
