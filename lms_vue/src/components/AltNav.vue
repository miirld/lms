<template>
    <b-navbar class="is-primary has-text-weight-semibold">
        <template #brand>
            <router-link to="/" class="navbar-item"><img src="../assets/logo.svg" alt="Лого" width="50px"
                    style="max-height:80% ;"></router-link>
        </template>
        <template #start>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                Главная
            </b-navbar-item>
            <b-navbar-item tag="router-link" :to="{ path: 'courses' }">
                Курсы
            </b-navbar-item>
        </template>

        <template #end>
            <b-navbar-dropdown label="Личный кабинет">
                <b-navbar-item tag="router-link" :to="{ path: 'my-account' }">
                    Личный кабинет
                </b-navbar-item>
                <b-navbar-item @click="logout">
                    Выйти
                </b-navbar-item >
            </b-navbar-dropdown>
        </template>
    </b-navbar>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Nav',
    methods: {
        async logout() {
            console.log('Выход')


            await axios
                .post('/token/logout/')
                .then(response => {
                    console.log('Logged out')
                })


            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')

            this.$store.commit('removeToken')

            this.$router.push('/login')


        }
    }
}
</script>