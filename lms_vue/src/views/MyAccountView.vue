<template>
    <div class="account">
        <div class="hero is-primary">
            <div class="hero-body has-text-centered">
                <h1 class="title">Личный кабинет</h1>
            </div>
        </div>

        <section class="section">
            <button @click="logout" class="button is-danger">Выйти</button>
        </section>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccountView',
    mounted() {
        document.title = 'Личный кабинет | Роснефть класс'
    },

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

            this.$store.commit('removeToken')

            this.$router.push('/log-in')
            console.log('Выполнено')


        }
    }
}
</script>