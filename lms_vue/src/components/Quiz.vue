<template>
    <div class="quiz">
        <h3>{{ quiz.question }}</h3>
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
            <button class="button is-info" @click="submitQuiz">Ответить</button>
        </div>
        <template v-if="quizResult == 'Верно'">
            <div class="notification is-success mt-4">Верно!</div>
        </template>
        <template v-if="quizResult == 'Неверно'">
            <div class="notification is-danger mt-4">Неверно! Попробуйте еще раз</div>
        </template>
    </div>
</template>


<script>
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
                } else {
                    this.quizResult = 'Неверно'
                }
            } else {
                alert('ВЫберите вариант ответа')
            }
        },
    }
}
</script>