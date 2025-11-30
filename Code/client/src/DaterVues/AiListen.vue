<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { watch } from 'vue'
import PinkButton from '../components/PinkButton.vue';
import NavSuite from '../components/NavSuite.vue';

// --- Live Speech Panel logic (from RealtimeSpeechPanel.vue) ---
const listening = ref(false)
const transcript = ref('')
const interim = ref('')
const ttsText = ref('')
const recognitionSupported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window
let recognition = null
const voices = ref([])
const selectedVoice = ref('')
// Last filtered backend response for newly streamed interim text
const serverResult = ref('')
// Track current spoken utterance & speaking state
let currentUtterance = null
const speaking = ref(false)

function getCsrfToken() {
    // Django sets csrftoken cookie by default when CSRF middleware is active.
    const name = 'csrftoken='
    const decoded = document.cookie
    const parts = decoded.split(';')
    for (let p of parts) {
        p = p.trim()
        if (p.startsWith(name)) {
            return p.substring(name.length)
        }
    }
    return ''
}

function loadVoices() {
    const synth = window.speechSynthesis
    voices.value = synth.getVoices()
    if (!selectedVoice.value && voices.value.length) {
        selectedVoice.value = voices.value[0].name
    }
}

onMounted(() => {
    if (recognitionSupported) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
        recognition = new SpeechRecognition()
        recognition.continuous = true
        recognition.interimResults = true
        recognition.lang = 'en-US'
        recognition.onresult = (event) => {
            let finalText = ''
            let interimText = ''
            for (let i = event.resultIndex; i < event.results.length; ++i) {
                const res = event.results[i]
                if (res.isFinal) {
                    finalText += res[0].transcript
                } else {
                    interimText += res[0].transcript
                }
            }
            if (finalText) transcript.value += (transcript.value ? ' ' : '') + finalText.trim()
            interim.value = interimText
        }
        recognition.onerror = (e) => {
            console.error('STT error:', e)
            listening.value = false
        }
        recognition.onend = () => {
            listening.value = false
        }
    }
    loadVoices()
    if (typeof window !== 'undefined' && window.speechSynthesis) {
        window.speechSynthesis.onvoiceschanged = loadVoices
    }
    // Auto-cancel any speech on page reload/navigation
    window.addEventListener('beforeunload', cancelSpeech)
})

onBeforeUnmount(() => {
    if (recognition && listening.value) {
        recognition.stop()
    }
    cancelSpeech()
    window.removeEventListener('beforeunload', cancelSpeech)
})

// Call server with only new interim text chunks
watch(interim, async (newVal, oldVal) => {
    if (!newVal || !newVal.trim()) return
    // Determine appended portion relative to previous interim value
    let diff = ''
    if (oldVal && newVal.startsWith(oldVal)) {
        diff = newVal.slice(oldVal.length)
    } else {
        diff = newVal
    }
    diff = diff.trim()
    if (!diff) return
    const csrf = getCsrfToken()
    try {
        const res = await fetch('/api/speech/test', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf
            },
            body: JSON.stringify({ transcript: diff })
        })
        if (res.ok) {
            const data = await res.json()
            serverResult.value = data.result || ''
        }
    } catch (e) {
        console.error('Failed calling speech filter endpoint:', e)
    }
})

function toggleListening() {
    if (!recognitionSupported) return
    if (!listening.value) {
        transcript.value = transcript.value.trim()
        interim.value = ''
        try {
            recognition.start()
            listening.value = true
        } catch (e) {
            console.error('STT start failed:', e)
        }
    } else {
        recognition.stop()
        listening.value = false
    }
}

function speak() {
    if (!ttsText.value.trim()) return
    const utterance = new SpeechSynthesisUtterance(ttsText.value)
    const v = voices.value.find(v => v.name === selectedVoice.value)
    if (v) utterance.voice = v
    attachUtteranceEvents(utterance)
    window.speechSynthesis.cancel()
    window.speechSynthesis.speak(utterance)
}

function speakAI() {
    if (!serverResult.value.trim()) return
    if (!voices.value.length) {
        loadVoices()
    }
    const utterance = new SpeechSynthesisUtterance(serverResult.value)
    const v = voices.value.find(v => v.name === selectedVoice.value)
    if (v) utterance.voice = v
    attachUtteranceEvents(utterance)
    window.speechSynthesis.cancel()
    window.speechSynthesis.speak(utterance)
}

function attachUtteranceEvents(utterance) {
    currentUtterance = utterance
    utterance.onstart = () => speaking.value = true
    utterance.onend = () => { speaking.value = false; currentUtterance = null }
    utterance.onerror = () => { speaking.value = false; currentUtterance = null }
}

function cancelSpeech() {
    if (window.speechSynthesis) {
        window.speechSynthesis.cancel()
    }
    speaking.value = false
    currentUtterance = null
}

function stopSpeaking() {
    cancelSpeech()
}

function clearTranscript() {
    transcript.value = ''
    interim.value = ''
    serverResult.value = ''
}
</script>

<template>
    <div>
        <NavSuite title='Let the AI Listen in!' profile='DaterProfile'>
            <router-link class="link" :to="{ name: 'DaterHome', params: {id: user_id} }">
                Home
            </router-link>
            <router-link class="link" :to="{ name: 'DaterProfile', params: {id: user_id} }">
                Profile
            </router-link>
            <router-link class="link" :to="{ name: 'Calendar', params: {id: user_id} }">
                Calendar
            </router-link>
            <router-link class="link" :to="{ name: 'AiChat', params: {id: user_id} }">
                AI Chat
            </router-link>
            <router-link class="link" :to="{ name: 'DaterGigs', params: {id: user_id}}">
                Gigs
            </router-link>
            <router-link class="link" :to="{ name: 'CupidCash', params: {id: user_id} }">
                Balance
            </router-link> 
            <router-link class="link" :to="{ name: 'DaterFeedback', params: {id: user_id}}">
                Feedback
            </router-link>
            <router-link class="link" :to="{ name: 'NotificationCenter', params: {id: user_id}}">
                Notifications
            </router-link>
        </NavSuite>
    
        <div class="mobile-container">
            <!-- Text to Speech UI -->
            <div class="live-panel">
                <h2 class="panel-title">Live Speech Tools</h2>
                <div class="stt">
                    <div class="controls">
                        <PinkButton 
                            :class="listening ? 'danger' : 'primary'" 
                            @click="toggleListening" 
                            :disabled="!recognitionSupported"
                        >
                            {{ listening ? 'Stop Listening' : 'Start Listening' }}
                        </PinkButton>
                        <PinkButton @click="clearTranscript">Clear</PinkButton>
                    </div>
                    <p v-if="!recognitionSupported" class="hint">
                        Your browser doesn't support the Web Speech API. 
                        Chrome is recommended for live transcription.
                    </p>
                    <div class="transcript">
                        <div class="final" v-text="transcript" />
                        <div class="interim" v-text="interim" />
                    </div>
                    <div v-if="serverResult" class="filtered-response">
                        <h3 class="response-title">AI Filtered Insight</h3>
                        <pre class="response-text">{{ serverResult }}</pre>
                        <PinkButton class="primary" @click="speakAI">Speak Insight</PinkButton>
                        <PinkButton 
                            :class="speaking ? 'danger' : 'secondary'" 
                            @click="stopSpeaking" 
                            :disabled="!speaking"
                            class="stop-speaking"
                        >Stop Speaking</PinkButton>
                    </div>
                </div>
                <div class="tts">
                    <label>
                        Voice
                        <select v-model="selectedVoice">
                            <option
                                v-for="v in voices"
                                :key="v.name"
                                :value="v.name"
                            >
                                {{ v.name }}
                            </option>
                        </select>
                    </label>
                    <textarea v-model="ttsText" rows="3" placeholder="Type text to speak..." />
                    <PinkButton class="primary" @click="speak">Speak</PinkButton>
                    <PinkButton 
                        :class="speaking ? 'danger' : 'secondary'" 
                        @click="stopSpeaking" 
                        :disabled="!speaking"
                        class="stop-speaking"
                    >Stop Speaking</PinkButton>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 40px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-content: center;
}

.button {
    display: flex;
    justify-content: center;
    border: none;
    border-radius: 50%;
    height: 50%;
    padding: 30px;
    margin: 2px 4px;
    color: white;
    box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.2);
}

.button:hover {
    filter: brightness(0.6);
}

.listen {
    background-color: var(--secondary-blue);
}

.emergency {
    background-color: var(--secondary-red);
}

.text {
    display: flex;
    border-top: 4px solid var(--primary-red);
    margin: 10px;
    padding: 10px;
    justify-content: center;
    align-content: center;
    text-align: center;
}

.message {
    display: flex;
}

.space-evenly {
    display: flex;
    flex-direction: row;
    align-content: space-evenly;
}

.space-evenly > * {
    margin: 16px;
}

.popup h1 {
    margin: auto;
    margin-top: 12px;
    margin-bottom: 4px;
    width: fit-content;
}

.popup div {
    margin: auto;
}

.active {
    transform: scale(1);
    transition: transform 0.2s cubic-bezier(0,1.4,1,1);
}

.update-content {
    text-align: center;
    margin-bottom: 4px;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.update-content input{
    border: none;
    border-radius: 4px;
    padding: 8px;
}
.live-panel {
    background: var(--primary-white, #fff);
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    padding: 24px;
    margin: 32px auto;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.panel-title {
    color: var(--primary-red);
    margin-bottom: 8px;
    font-size: 1.3em;
    font-weight: 600;
    text-align: center;
}
.controls {
    display: flex;
    gap: 12px;
    justify-content: center;
    margin-bottom: 8px;
}
.transcript {
    min-height: 80px;
    border: 2px solid var(--primary-red);
    border-radius: 8px;
    padding: 12px;
    background: var(--primary-white, #fff);
    color: var(--primary-black, #222);
    margin-top: 8px;
}
.final { color: var(--primary-black, #222); font-size: 1.1em; }
.interim { color: var(--secondary-blue, #007bff); font-style: italic; }
.filtered-response {
    margin-top: 14px;
    background: var(--primary-white, #fff);
    /* Match transcript box border color */
    border: 2px solid var(--primary-red);
    border-radius: 8px;
    padding: 12px;
    white-space: pre-wrap;
    max-height: 160px; /* prevent overly tall box */
    overflow-y: auto; /* scroll if content exceeds height */
    /* Allow natural width within parent; avoid overflow to right */
    max-width: 100%;
    box-sizing: border-box;
    overflow-x: hidden;
}
.response-title {
    margin: 0 0 6px 0;
    font-size: 0.95em;
    color: var(--secondary-blue, #007bff);
    font-weight: 600;
    text-align: center;
}
.response-text {
    margin: 0;
    font-size: 0.85em;
    line-height: 1.25em;
    font-family: inherit;
    white-space: pre-wrap;
    word-break: break-word; /* ensure long tokens wrap */
    overflow-wrap: anywhere;
}
.tts {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 16px;
}
textarea {
    width: 100%;
    resize: vertical;
    border: 1px solid var(--primary-red);
    border-radius: 6px;
    padding: 8px;
    font-size: 1em;
}
select {
    margin-left: 8px;
    border-radius: 4px;
    padding: 4px;
}
.hint {
    font-size: 0.95em;
    color: var(--secondary-blue, #007bff);
    text-align: center;
}
.stop-speaking { margin-top: 4px; }
</style>
.live-panel {
    background: var(--primary-white, #fff);
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    padding: 24px;
    margin: 32px auto;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.panel-title {
    color: var(--primary-red);
    margin-bottom: 8px;
    font-size: 1.3em;
    font-weight: 600;
    text-align: center;
}
.controls {
    display: flex;
    gap: 12px;
    justify-content: center;
    margin-bottom: 8px;
}
.transcript {
    min-height: 80px;
    border: 2px solid var(--primary-red);
    border-radius: 8px;
    padding: 12px;
    background: var(--primary-white, #fff);
    color: var(--primary-black, #222);
    margin-top: 8px;
}
.final { color: var(--primary-black, #222); font-size: 1.1em; }
.interim { color: var(--secondary-blue, #007bff); font-style: italic; }
.tts {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 16px;
}
textarea {
    width: 100%;
    resize: vertical;
    border: 1px solid var(--primary-red);
    border-radius: 6px;
    padding: 8px;
    font-size: 1em;
}
select {
    margin-left: 8px;
    border-radius: 4px;
    padding: 4px;
}
.hint {
    font-size: 0.95em;
    color: var(--secondary-blue, #007bff);
    text-align: center;
}
