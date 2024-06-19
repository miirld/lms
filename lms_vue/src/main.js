import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "@mdi/font/css/materialdesignicons.css";
import {
	Datepicker,
	Navbar,
	Icon,
	Loading,
	Menu,
	Dropdown,
	Collapse,
	Select,
	Toast,
} from "buefy";
import axios from "axios";
import TextClamp from "vue3-text-clamp";

// axios.defaults.baseURL = "http://127.0.0.1:8000/api/v1";
axios.defaults.baseURL = "http://192.168.97.55:8000/api/v1";
// axios.defaults.baseURL = "http://api.watch-this.site/api/v1";

axios.interceptors.response.use(
	function (response) {
		return response;
	},
	function (error) {
		if (error.response.status == 401) {
			axios.defaults.headers.common["Authorization"] = "";
			localStorage.removeItem("token");
			store.commit("removeToken");
			router.push("/log-in");
			return Promise.reject("Unauthorized");
		}
		return Promise.reject(error);
	}
);

createApp(App)
	.use(store)
	.use(router, axios)
	.use(Datepicker)
	.use(Navbar)
	.use(Icon)
	.use(TextClamp)
	.use(Loading)
	.use(Menu)
	.use(Dropdown)
	.use(Collapse)
	.use(Select)
	.use(Toast)
	.mount("#app");
