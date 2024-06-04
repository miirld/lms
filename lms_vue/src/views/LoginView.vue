<template>
    <div class="login">
        <header>
            <b-navbar class="is-primary has-text-weight-semibold" :mobile-burger="false">
                <template #brand>
                    <b-navbar-item tag="router-link"  id="logo" :to="{ name: 'Welcome' }">
                        <img src="../assets/logo.svg"  alt="Лого" width="50px" style="max-height:57.53px ;">
                        <p class="is-size-5 pt-5 mt-4">Роснефть-классы</p>
                    </b-navbar-item>
                </template>
            </b-navbar>
        </header>
        <div class="hero is-small pt-6">
            <div class="hero-body has-text-centered">
                <h1 class="title">Вход на платформу</h1>
            </div>
        </div>
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <form class="box" v-on:submit.prevent="submitForm">
                            <div class="field">
                                <label>Логин</label>
                                <div class="control">
                                    <input type="username" class="input" v-model="username">
                                </div>
                            </div>

                            <div class="field">
                                <label>Пароль</label>
                                <div class="control">
                                    <input type="password" class="input" v-model="password">
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button is-dark">Войти</button>
                                </div>
                            </div>

                            <template v-if="errors.length">
                                <div class="notification is-light" v-for="error in errors" v-bind:key="error">
                                    {{ error }}
                                </div>
                            </template>

                        </form>



                    </div>
                </div>
            </div>
        </section>

    </div>
</template>





<script>
import axios from 'axios'
export default {
    data() {
        return {
            username: '',
            password: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Авторизация | Роснефть класс'

    },

    methods: {
        async submitForm() {
            console.log('Подтверждение формы')
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')


            this.errors = []

            if (this.username === '' && this.password === '') {
                this.errors.push('Вы не ввели логин и пароль!')
            }

            else if (this.username === '') {
                this.errors.push('Вы не ввели логин!')
            }

            else if (this.password === '') {
                this.errors.push('Вы не ввели пароль!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/users/login/', formData)
                    .then(response => {
                        const token = response.data.token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}:${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push(JSON.stringify(error))
                            console.log(JSON.stringify(error))
                        }
                    })

                await axios
                    .get('/users/me')
                    .then(response => {
                        this.$store.commit('setUserInfo', response.data)
                        localStorage.setItem('user.id', response.data.id)
                        localStorage.setItem('user.role', response.data.role)
                        this.$router.push('/')
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
}
</script>