import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/HomeView.vue";
import Login from "../views/LoginView.vue";
import MyAccount from "../views/MyAccountView.vue";
import Courses from "../views/CoursesView.vue";

const routes = [
	{
		path: "/",
		name: "Home",
		component: Home,
	},
	{
		path: "/my-account",
		name: "MyAccount",
		component: MyAccount,
	},
	{
		path: "/courses",
		name: "Courses",
		component: Courses,
	},
	{
		path: "/log-in",
		name: "Login",
		component: Login,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("token")) {
				return { name: "Home" };
			}
		},
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

router.beforeEach((to, from) => {
	if (!localStorage.getItem("token") && to.name !== "Login") {
		return { name: "Login" };
	}
});

export default router;
