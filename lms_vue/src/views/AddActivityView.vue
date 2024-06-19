<template>
    <div class="add-activity">
        <div class="hero is-small pt-6">
            <div class="hero-body has-text-centered">
                <h1 class="title">Назначить курс</h1>
            </div>
        </div>
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <form class="box" v-on:submit.prevent="submitForm">
                            <div class="field">
                                <label>Класс</label>
                                <div class="control">
                                    <div class="select is-fullwidth">
                                        <select v-model="group">
                                            <option v-for="study_group in form_data" :key="study_group.id"
                                                :value="study_group">
                                                {{ study_group.grade + study_group.letter + ' ' +
                                                    study_group.school.short_name }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>

                            <div class="field">
                                <label>Курс</label>
                                <div class="control">
                                    <div class="control">
                                        <div class="select is-fullwidth">
                                            <select v-model="course">
                                                <template v-for="study_group in form_data" :key="study_group.id">
                                                    <template v-for="course in study_group.courses" :key="course.id">
                                                        <option v-if="study_group.id == group.id" :value="course">
                                                            {{ course.clamped_title }}
                                                        </option>
                                                    </template>
                                                </template>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button is-primary">Назначить</button>
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
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'AddActivity',
    data() {
        return {
            form_data: [],
            group: '',
            course: '',
            isLoading: false,
            errors: [],
        }
    },

    mounted() {
        document.title = 'Назначить курс | Роснефть класс'
        this.getData()
    },
    methods: {
        async getData() {
            this.isLoading = true
            await axios
                .get('/activities/get-data-to-assign/')
                .then(response => {
                    console.log(response.data)
                    this.form_data = response.data
                })
                .catch(error => {
                    console.log(error)
                }
                )
            this.isLoading = false

        },
        async submitForm() {
            this.errors = []

            if (this.group === '' && this.course === '') {
                this.errors.push('Вы не выбрали группу и курс!')
            }

            else if (this.group === '') {
                this.errors.push('Вы не выбрали группу!')
            }

            else if (this.course === '') {
                this.errors.push('Вы не выбрали курс!')
            }
            if (!this.errors.length) {
                const formData = {
                    study_group: this.group.id,
                    course: this.course.id
                }
                this.isLoading = true
                await axios
                    .post('/activities/assign/', formData)
                    .then(response => {
                        console.log(response)
                        this.errors.push('Вы успешно назначили классу «' + this.group.grade + this.group.letter + ' ' +
                            this.group.school.short_name + '» курс «' + this.course.clamped_title + '»')
                        this.group = ''
                        this.course = ''

                    })
                    .catch(error => {
                        console.log('error:', error)
                        if (error.response) {
                            this.errors.push(JSON.stringify(error.response.data))
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push(JSON.stringify(error))
                            console.log(JSON.stringify(error))
                        }
                    })
                this.isLoading = false
                this.getData()
            }
        }
    }
}


</script>