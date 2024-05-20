<template>
    <header>
        <b-navbar class="is-primary has-text-weight-semibold">
            <template #brand>
                <router-link :to="{ name: 'Home' }" class="navbar-item"><img src="../assets/logo.svg" alt="Лого"
                        width="50px" style="max-height:80% ;"></router-link>
            </template>
            <template #start>
                <b-navbar-item tag="router-link" :to="{ name: 'Home' }">
                    Новости
                </b-navbar-item>
                <b-navbar-item v-if="this.$store.state.user.role=='teacher'" tag="router-link" :to="{ name: 'Courses' }">
                    Курсы
                </b-navbar-item>
                <b-navbar-item v-if="this.$store.state.user.role=='student'" tag="router-link" :to="{ name: 'Activities' }">
                    Курсы
                </b-navbar-item>
                <b-navbar-item tag="router-link" :to="{ name: 'Chat' }">
                    Общение
                </b-navbar-item>
            </template>

            <template #end>
                <b-navbar-dropdown label="Личный кабинет">
                    <b-navbar-item tag="router-link" :to="{ name: 'MyAccount' }">
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

<script>
import axios from 'axios'

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

            this.$router.push('/log-in')


        }
    }
}
</script>