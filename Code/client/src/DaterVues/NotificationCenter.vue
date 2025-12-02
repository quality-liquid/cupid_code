<script setup>
import { ref, onMounted } from 'vue'
import NavSuite from '../components/NavSuite.vue'

// state
const status = ref('Ready')
const statusType = ref('info')
const notifications = ref([])
const title = ref('Test Notification')
const body = ref('This is a test notification from CupidCode')
const user_id = parseInt(window.location.hash.split('/')[3])

function setStatus(msg, type='info') {
	status.value = msg
	statusType.value = type
}

// Simple test: show a browser notification directly (no server needed)
function showLocalNotification() {
	if (!('Notification' in window)) {
		setStatus('Notifications not supported', 'error')
		return
	}
	
	if (Notification.permission === 'granted') {
		// Permission already granted, show notification
		new Notification(title.value, {
			body: body.value,
			icon: '/icon.png',
			badge: '/badge.png'
		})
		setStatus('Local notification shown!', 'success')
		// Add to our list too
		notifications.value.unshift({
			receivedAt: new Date().toLocaleTimeString(),
			title: title.value,
			body: body.value
		})
		persist()
	} else if (Notification.permission !== 'denied') {
		// Need to request permission
		Notification.requestPermission().then(permission => {
			if (permission === 'granted') {
				new Notification(title.value, {
					body: body.value,
					icon: '/icon.png'
				})
				setStatus('Permission granted! Notification shown!', 'success')
			} else {
				setStatus('Permission denied', 'error')
			}
		})
	} else {
		setStatus('Notification permission was previously denied', 'error')
	}
}

function clearNotifications() {
	notifications.value = []
	localStorage.setItem('cc_notifications', '[]')
}

// persist updates
function persist() {
	localStorage.setItem('cc_notifications', JSON.stringify(notifications.value.slice(0, 100)))
}

function loadNotifications() {
	const stored = JSON.parse(localStorage.getItem('cc_notifications') || '[]')
	notifications.value = stored
}

onMounted(() => loadNotifications())

</script>

<template>
	<div class="notification-center-root">
		<NavSuite title="Notifications" profile="DaterProfile">
			<router-link class="link" :to="{ name: 'DaterHome', params: { id: user_id } }">
				Home
			</router-link>
			<router-link class="link" :to="{ name: 'DaterProfile', params: { id: user_id } }">
				Profile
			</router-link>
			<router-link class="link" :to="{ name: 'Calendar', params: { id: user_id } }">
				Calendar
			</router-link>
			<router-link class="link" :to="{ name: 'AiChat', params: { id: user_id } }">
				AI Chat
			</router-link>
			<router-link class="link" :to="{ name: 'AiListen', params: { id: user_id } }">
				AI Listen
			</router-link>
			<router-link class="link" :to="{ name: 'DaterGigs', params: { id: user_id } }">
				Gigs
			</router-link>
			<router-link class="link" :to="{ name: 'CupidCash', params: { id: user_id } }">
				Balance
			</router-link>
			<router-link class="link" :to="{ name: 'DaterFeedback', params: { id: user_id } }">
				Feedback
			</router-link>
			<router-link class="link" :to="{ name: 'NotificationCenter', params: { id: user_id } }">
				Notifications
			</router-link>
		</NavSuite>

		<div class="status" :class="statusType">{{ status }}</div>

		<div class="send-box">
			<h3>Send Notification</h3>
			<p style="font-size: 0.85rem; color: #666;">
				Create a browser notification that appears immediately.
			</p>
			<input v-model="title" placeholder="Title" />
			<textarea v-model="body" placeholder="Body"></textarea>
			<div class="row">
				<button class="primary" @click="showLocalNotification">Show Notification</button>
				<button class="ghost" @click="clearNotifications">Clear History</button>
			</div>
		</div>

		<div class="list">
			<h3>Notification History ({{ notifications.length }})</h3>
			<ul v-if="notifications.length">
				<li v-for="(n,i) in notifications" :key="i">
					<div class="notif-title">{{ n.title }}</div>
					<div class="notif-body">{{ n.body }}</div>
					<div class="notif-time">{{ n.receivedAt }}</div>
				</li>
			</ul>
			<div v-else class="empty">No notifications yet.</div>
		</div>
	</div>
</template>

<style scoped>
.notification-center-root { padding: 1rem; }
.status { margin: .5rem 0; padding:.5rem .75rem; border-radius:6px; font-size:.9rem; }
.status.info { background:#eef; color:#334; }
.status.success { background:#e6f9ed; color:#164; }
.status.error { background:#ffecec; color:#600; }
.controls button { margin-right:.5rem; }
.send-box { margin:1rem 0; display:flex; flex-direction:column; gap:.5rem; }
.send-box input, .send-box textarea { 
	width:100%; 
	max-width:100%;
	box-sizing:border-box;
	padding:.5rem; 
	border:1px solid #ccc; 
	border-radius:4px; 
	font:inherit; 
	word-break:break-word;
}
/* Match visual sizing to notif-title and notif-body */
.send-box input { 
	font-weight:600; /* aligns with .notif-title */
}
.send-box textarea { 
	font-size:.85rem; 
	color:#444;      /* aligns with .notif-body */
	min-height:6rem;
	resize:vertical;
}
.row { display:flex; gap:.5rem; }
button { cursor:pointer; border:none; padding:.55rem .9rem; border-radius:6px; font-weight:600; }
button.primary { background: var(--secondary-blue, #3478f6); color:#fff; }
button.secondary { background: var(--secondary-red, #d9534f); color:#fff; }
button.ghost { background:#f5f5f5; }
.list ul { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:.5rem; }
.list li { 
	background:#fafafa;
	border:1px solid #e1e1e1;
	padding:.6rem .75rem;
	border-radius:6px;
	box-shadow:0 1px 2px rgba(0,0,0,.05);
}
.notif-title { font-weight:600; }
.notif-body { font-size:.85rem; color:#444; margin-top:.15rem; }
.notif-time { font-size:.7rem; color:#777; margin-top:.25rem; }
.empty { font-size:.85rem; color:#666; }
</style>