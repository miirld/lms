<template>
    <div class="add-activity">
        <div class="hero is-primary is-small">
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
                                <label>Группа</label>
                                <div class="control">
                                    <div class="select is-fullwidth">
                                        <select v-model="form.study_group">
                                            <option v-for="study_group in form_data" :key="study_group.id"
                                                :value="study_group.id">
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
                                            <select v-model="form.course">
                                                <template v-for="study_group in form_data" :key="study_group.id"
                                                    :value="study_group.id">
                                                    <template v-for="course in study_group.courses" :key="course.id"
                                                        :value="course.id">
                                                        <option v-if="study_group.id == form.study_group" :value="course.id">
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

                        </form>



                    </div>
                </div>
            </div>
        </section>

    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'AddActivity',
    data() {
        return {
            form_data: [],
            form: {
                study_group: null,
                course: null
            }
        }
    },

    mounted() {
        axios
            .get('/activities/get-for-assign/')
            .then(response => {
                console.log(response.data)
                this.form_data = response.data
            })
            .catch(error => {
                console.log(error)
            }
            )
    },
    methods: {
        submitForm() {
            if (this.form.study_group && this.form.course) {
                axios
                    .post('/activities/assign/', this.form)
                    .then(response => {
                        console.log(response)
                    })
                    .catch(error => {
                        console.log('error:', error)

                    })
                this.form.study_group = null
                this.form.course = null
            }
        }
    }
}


</script>