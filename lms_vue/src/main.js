import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@mdi/font/css/materialdesignicons.css'
import {Datepicker, Navbar, Icon} from 'buefy'
import axios from 'axios'
import TextClamp from 'vue3-text-clamp';



axios.defaults.baseURL = "http://127.0.0.1:8000/api/v1";

createApp(App).use(store).use(router, axios).use(Datepicker).use(Navbar).use(Icon).use(TextClamp).mount('#app')
