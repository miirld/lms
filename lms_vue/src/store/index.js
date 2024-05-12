import { createStore } from "vuex";

export default createStore({
	state: {
		user: {
			token: "",
			id: "",
			isAuthenticated: false,
		},
	},
	getters: {},
	mutations: {
		initializeStore(state) {
			console.log("Инициализация состояния");
			if (localStorage.getItem("token")) {
				state.user.token = localStorage.getItem("token");
				state.user.id = localStorage.getItem("user.id")
				state.user.isAuthenticated = true;
			} else {
				state.user.token = "";
				state.user.id = ""
				state.user.isAuthenticated = false;
			}
		},
		setToken(state, token) {
			state.user.token = token;
			state.user.isAuthenticated = true;
		},
		removeToken(state) {
			state.user.token = "";
			state.user.id = ""
			state.user.isAuthenticated = false;
		},
		setUserInfo(state, user) {
			state.user.id = user.id
		}
	},
	actions: {},
	modules: {},
});
