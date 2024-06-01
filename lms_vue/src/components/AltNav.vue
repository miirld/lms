<template>
    <header>
        <b-navbar class="is-primary has-text-weight-semibold">
            <template #brand>
                <b-navbar-item tag="router-link" id="logo" :to="{ name: 'Home' }">
                    <img src="../assets/logo.svg" alt="Лого" width="50px" style="max-height:80% ;">
                </b-navbar-item>
            </template>
            <template #start>
                <b-navbar-item tag="router-link" :active="this.$route.name == 'Home'" :to="{ name: 'Home' }"
                    :style="{ cursor: this.$route.name == 'Home' ? 'default' : 'pointer' }">
                    Новости
                </b-navbar-item>
                <b-navbar-item tag="router-link" :to="{ name: 'EducationalProgress' }"
                    :style="{ cursor: this.$route.name == 'EducationalProgress' ? 'default' : 'pointer' }"
                    v-if="this.$store.state.user.role == 'teacher' || this.$store.state.user.role == 'tutor'"
                    :active="this.$route.name == 'EducationalProgress'">
                    Успеваемость
                </b-navbar-item>

                <b-navbar-item v-if="this.$store.state.user.role == 'student'"
                    :active="this.$route.name == 'Activities'" tag="router-link" :to="{ name: 'Activities' }"
                    :style="{ cursor: this.$route.name == 'Activities' ? 'default' : 'pointer' }">
                    Курсы
                </b-navbar-item>
                <b-navbar-item v-if="this.$store.state.user.role == 'teacher' || this.$store.state.user.role == 'tutor'"
                    :active="this.$route.name == 'Courses'" tag="router-link" :to="{ name: 'Courses' }"
                    :style="{ cursor: this.$route.name == 'Courses' ? 'default' : 'pointer' }">
                    Курсы
                </b-navbar-item>
                <b-navbar-item tag="router-link" :active="this.$route.name == 'Chat'" :to="{ name: 'Chat' }"
                    :style="{ cursor: this.$route.name == 'Chat' ? 'default' : 'pointer' }">
                    Общение
                </b-navbar-item>


            </template>

            <template #end>
                <b-navbar-dropdown label="Личный кабинет">
                    <b-navbar-item tag="router-link" :to="{ name: 'MyAccount' }"
                        :style="{ cursor: this.$route.name == 'MyAccount' ? 'default' : 'pointer' }">
                        Личный кабинет
                    </b-navbar-item>
                    <b-navbar-item @click="logout">
                        Выйти
                    </b-navbar-item>
                </b-navbar-dropdown>
            </template>
        </b-navbar>
    </header>
</template>

<style scoped>
#logo:hover,
#logo:focus {
    background-color: #e7cf6e;
}
</style>


<script>
import axios from 'axios'
import { useRoute } from 'vue-router'
const loaction = useRoute();
export default {
    name: 'Nav',
    methods: {
        async logout() {
            console.log('Выход')


            await axios
                .post('/auth/logout/')
                .then(response => {
                    console.log('Logged out')
                })


            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('user.id')
            localStorage.removeItem('user.role')
            this.$store.commit('removeToken')

            this.$router.push('/welcome')


        }
    }
}
</script>