import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/NewsView.vue";
import Login from "../views/LoginView.vue";
import MyAccount from "../views/MyAccountView.vue";
import Courses from "../views/CoursesView.vue";
import Course from "../views/CourseView.vue";
import Chat from "../views/ChatView.vue";
import Messages from "../views/MessagesView.vue";
import AddActivity from "../views/AddActivityView.vue";
import Activities from "../views/ActivitiesView.vue";
import ActiveCourse from "../views/ActiveCourseView.vue";
import EducationalProgress from "../views/EducationalProgressView.vue"
import CourseProgress from "../views/CourseProgressView.vue"
import Landing from "../views/LandingView.vue"
const routes = [
	{
		path: "/",
		name: "Home",
		component: Home,
	},
	{
		path: "/welcome",
		name: "Welcome",
		component: Landing,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("token")) {
				return { name: "Welcome" };
			}
		},
	},

	{
		path: "/my-account",
		name: "MyAccount",
		component: MyAccount,
	},
	{
		path: "/edu-progress",
		name: "EducationalProgress",
		component: EducationalProgress,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("user.role") == 'student') {
				return { name: "Home" };
			}
		},
	},
	{
		path: "/courses",
		name: "Courses",
		component: Courses,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("user.role") == 'student') {
				return { name: "Activities" };
			}
		},
	},
	{
		path: "/activities",
		name: "Activities",
		component: Activities,
		beforeEnter: (to, from) => {
			let role = localStorage.getItem("user.role");
			if (role == 'teacher' || role == 'tutor') {
				return { name: "Courses" };
			}
		},
	},
	{
		path: "/chat",
		name: "Chat",
		component: Chat,
	},
	{
		path: "/messages",
		name: "Messages",
		component: Messages,
	},
	{
		path: "/add-activity",
		name: "AddActivity",
		component: AddActivity,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("user.role") == 'student') {
				return { name: "Home" };
			}
		},
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
	{
		path: "/courses/:id",
		name: "Course",
		component: Course,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("user.role") == 'student') {
				return { name: "Activities" };
			}
		},
	},
	{
		path: "/group/:id/progress",
		name: "CourseProgress",
		component: CourseProgress,
		beforeEnter: (to, from) => {
			if (localStorage.getItem("user.role") == 'student') {
				return { name: "Activities" };
			}
		},
	},
	{
		path: "/activities/:id",
		name: "ActiveCourse",
		component: ActiveCourse,
		beforeEnter: (to, from) => {
			let role = localStorage.getItem("user.role");
			if (role == 'teacher' || role == 'tutor') {
				return { name: "Courses" };
			}
		},
	},

];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

router.beforeEach((to, from) => {
	if (!localStorage.getItem("token") && (to.name !== "Login" && to.name !== "Welcome")) {
		return { name: "Welcome" };
	}
});

export default router;
