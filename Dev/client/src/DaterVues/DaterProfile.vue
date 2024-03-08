<script setup>
    import {ref} from 'vue';
    import router from '../router';
    import { makeRequest } from '../utils/make_request';

    const email = ref('')
    const password = ref('')
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

    const user_id  = parseInt(window.location.hash.split('/')[3])

    function openDrawer() {
        const element = document.getElementById('navbar')
        if (element.className === 'navbar') {
            element.className = 'navbar opened'
        }
        else {
            element.className = 'navbar'
        }
    }

    async function logout() {
        const result = await makeRequest(`/logout/`)
        router.push('/')
    }

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
        const results = await makeRequest(`api/dater/profile/${user_id}`);
        email.value = results.email
        username.value = results.username
        phone.value = results.phone_number
        addr.value = results.location
        fname.value = results.first_name
        lname.value = results.last_name
        desc.value = results.description
        str.value = results.dating_strengths
        weak.value = results.dating_weaknesses
        ntype.value = results.nerd_type
        interests.value = results.interests
        goals.value = results.relationship_goals
        past.value = results.past
    }

    async function update() {
        // Validate data
        const checkData = [email, password, accType, phone, addr, desc]

        let check = 0;
        for (let i = 0; i < checkData.length; i++) {
            if (checkData[i] !== '') check++;
            else {
                const error = document.querySelector(`input[name=${checkData[i]}]`);
                error.class = error.class + 'error';
            }
        }
        const results = await makeRequest('/api/dater/profile/', 'post', {
            username: username.value,
            first_name: fname.value,
            last_name: lname.value,
            email: email.value,
            password: password.value,
            phone_number: phone.value,
            location: addr.value,
            description: desc.value,
            profile_picture: image,
            dating_strengths: str.value,
            dating_weaknesses: weak.value,
            nerd_type: ntype.value,
            interests: interests.value,
            relationship_goals: goals.value,
            past: past.value,
        })
        router.push({name: DaterProfile, params: {id: user_id}});
    }    

</script>

<template>
    <nav class="nav homenav">
        <button @click="openDrawer" class="icon-button">
            <img :src="'/get_menu/'" alt="Menu Open icon" class="icon">
        </button>
        <!-- This will be the profile picture when setup -->
        <img :src="'/get_menu/'" alt="Profile Picture" class="icon">
        <div id="navbar" class="navbar">
            <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }"> Home </router-link>
            <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }"> Profile </router-link>
            <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }"> AI Chat </router-link>
            <router-link class="link" :to="{ name: 'AiListen', params: {id: user_id} }"> AI Listen </router-link>
            <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }"> Balance</router-link>
            <button class="logout" @click="logout"> Logout </button>
        </div>
    </nav>      
    <div class="container">
        <label class="update-content" for="image">
            Profile Picture
            <input type="file" id="image" name="image" @change="previewFile"/>
            <img name="pfp" src="" height="200" alt="Image preview...">
        </label>
        <div class="personal">
            <label class="update-content" for="fname">
                First Name
                <input type="text" id="fname" :value="fname" @change="(e) => fname = e.target.value"/>
            </label>
            <label class="update-content" for="lname">
                Last Name
                <input type="text" id="lname" :value="lname" @change="(e) => lname = e.target.value"/>
            </label>
            <label class="update-content" for="phone">
                Phone Number
                <input type="number" id="phone" :value="phone" @change="(e) => phone = e.target.value"/>
            </label>
            <label class="update-content" for="address">
                Address
                <input type="text" id="address" :value="addr" @change="(e) => addr = e.target.value"/>
            </label>
        </div>
        <div class="userinfo">
            <label class="update-content" for="username">
                Username
                <input type="text" id="username" :value="username" @change="(e) => username = e.target.value"/>
            </label>
            <label class="update-content" for="email">
                Email
                <input type="email" id="email" :value="email" @change="(e) => email = e.target.value"/>
            </label>
            <label class="update-content" for="password">
                Password
                <input type="password" id="password" :value="password" @change="(e) => password = e.target.value"/>
            </label>
        </div>
        <div class="details">
            <label class="update-text" for="desc">
                Physical Description
                <textarea :value="desc" id="desc" @change="(e) => desc = e.target.value"></textarea>
            </label>
            <label class="update-content" for="nerd_type">
                Nerd Type
                <input type="text" id="nerd_type" :value="ntype" @change="(e) => ntype = e.target.value"/>
            </label>
            <label class="update-text" for="goals">
                Relationship Goals
                <textarea :value="goals" id="goals" @change="(e) => goals = e.target.value"></textarea>
            </label>
            <label class="update-text" for="interests">
                Interests
                <textarea :value="interests" id="interests" @change="(e) => interests = e.target.value"></textarea>
            </label>
            <label class="update-text" for="past">
                Past Dating History
                <textarea :value="past" id="past" @change="(e) => past = e.target.value"></textarea>
            </label>
            <label class="update-text" for="strengths">
                Dating Strengths
                <textarea :value="str" id="strengths" @change="(e) => str = e.target.value"></textarea>
            </label>
            <label class="update-text" for="weaknesses">
                Dating Weaknesses
                <textarea :value="weak" id="weaknesses" @change="(e) => weak = e.target.value"></textarea>
            </label>
        </div>
    </div>
    <button class="button" @click="update"> Update/Save changes </button>
</template>

<style scoped>

.container {
    margin-top: 40px;
}

.personal {
    display: flex;
}

.details {
    display: flex;
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
    width: auto;
    height: 100px;
    border: 3px rgba(128, 128, 128, 0.5) solid;
    border-radius: 16px;
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
</style>