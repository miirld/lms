<template>
    <div class="account">
        <div class="container">
            <section class="section">
                <h3 class="title is-3">О пользователе</h3>
                <div class="box">
                    <div class="content">
                        <div class="columns is-mobile">
                            <div class="column is-narrow pr-0">
                                <figure class="image is-48x48 mx-0">
                                    <img class="is-rounded" :src="user.get_image" />
                                </figure>
                            </div>
                            <div class="column">
                                <p>
                                    <strong>{{ user.first_name }} {{ user.last_name }} {{ user.patronymic }}</strong>
                                    <br />
                                    <small>{{ role }}</small>
                                </p>
                            </div>
                        </div>
                        <p><strong>Школа: </strong> {{ school }}</p>
                        <p><strong>Класс: </strong> {{ study_groups() }}
                        </p>
                    </div>
                    <button @click="logout" class="button is-danger">Выйти</button>
                </div>
            </section>
        </div>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccountView',
    data() {
        return {
            user: { study_groups: [{ school: {} },] },
            isLoading: true,
        }
    },
    async mounted() {
        document.title = 'Личный кабинет | Роснефть класс'
        this.isLoading = true
        await axios
            .get('/users/account')
            .then(response => {
                console.log(response.data)
                this.user = response.data
            })
            .catch(error => {
                console.log(error)
            })
        this.isLoading = false
    },

    computed: {
        school() {
            return this.user.study_groups.length !== 0 ? this.user.study_groups[0].school.short_name : '-'
        },
        role() {
            return this.user.role == 'student' ? 'Ученик' : (this.user.role == 'teacher' ? 'Учитель' : (this.user.role == 'tutor' ? 'Куратор' : ''))
        },
    },

    methods: {
        study_groups() {
            let groups = ''
            if (this.user.study_groups.length !== 0) {
                for (let group in this.user.study_groups) {
                    groups += this.user.study_groups[group].grade + this.user.study_groups[group].letter + ' '
                }
            }
            else {
                groups = '-'
            }
            return groups
        },

        async logout() {
            console.log('Выход')

            this.isLoading = true
            await axios
                .post('/users/logout/')
                .then(response => {
                    console.log('Logged out')
                    axios.defaults.headers.common['Authorization'] = ''
                    localStorage.removeItem('token')
                    localStorage.removeItem('user.id')
                    localStorage.removeItem('user.role')
                    this.$store.commit('removeToken')
                    this.$router.push('/welcome')
                })

            this.isLoading = false    

            console.log('Выполнено')


        }
    }
}
</script>