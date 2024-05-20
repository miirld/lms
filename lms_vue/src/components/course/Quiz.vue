<template>
    <div class="quiz">
        <div class="box">
            <h6 class="title is-6">{{ quiz.question }} </h6>
            <template v-if="quizResult == 'Верно'">
                <div class="mb-4">
                    <b-icon icon="checkbox-marked-circle" size="is-small" type="is-primary">
                    </b-icon>
                    Верно!
                </div>
            </template>
            <template v-if="quizResult == 'Неверно'">
                <div class="mb-4">
                    <b-icon icon="close-circle" size="is-small">
                    </b-icon>
                    Неверно. Попробуйте ещё раз
                </div>
            </template>
            <div class="control">
                <label class="radio">
                    <input type="radio" :value="quiz.opt1" v-model="selectedAnswer"> {{
                        quiz.opt1 }}
                </label>
            </div>
            <div class="control">
                <label class="radio">
                    <input type="radio" :value="quiz.opt2" v-model="selectedAnswer"> {{
                        quiz.opt2 }}
                </label>
            </div>
            <div class="control">
                <label class="radio">
                    <input type="radio" :value="quiz.opt3" v-model="selectedAnswer"> {{
                        quiz.opt3 }}
                </label>
            </div>
            <div class="control mt-4">
                <button class="button is-primary" @click="submitQuiz">Ответить</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
input[type="radio"] {
    accent-color: #e7cf6e;
}
</style>


<script>
import axios from 'axios'


export default {
    props: ['quiz'],
    data() {
        return {
            selectedAnswer: '',
            quizResult: null,
        }
    },
    methods: {
        submitQuiz() {
            this.quizResult = null

            if (this.selectedAnswer) {
                if (this.selectedAnswer === this.quiz.answer) {
                    this.quizResult = 'Верно'
                           this.$emit('done')
                } else {
                    this.quizResult = 'Неверно'
                }
            } else {
                alert('Выберите вариант ответа')
            }
        },
    }
}
</script>