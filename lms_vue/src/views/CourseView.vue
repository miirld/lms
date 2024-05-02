<template>
    <div class="course">
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-2">
                        <h2>Разделы</h2>
                        <ul>
                            <li v-for="lesson in lessons" v-bind:key="lesson.id">
                                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
                            </li>

                        </ul>
                    </div>
                    <div class="column is-10">

                        <template v-if="activeLesson">
                            <h2>{{ activeLesson.title }}</h2>
                            <hr>
                            <p>{{ activeLesson.content }}</p>
                            <hr>
                            <template v-if="activeLesson.lesson_type === 'quiz'">
                                <Quiz :quiz="quiz" />
                            </template>
                            <template v-if="activeLesson.lesson_type === 'video'">
                                <Video :youtube_id="activeLesson.youtube_id" />
                            </template>
                        </template>
                        <template v-else>
                            {{ course.title }}
                            <br>
                            {{ course.description }}
                        </template>

                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import Quiz from '@/components/Quiz'
import Video from '@/components/Video'

export default {
    data() {
        return {
            course: { created_by: { id: 0, }, },
            lessons: [],
            activeLesson: null,
            quiz: {},
            activity: {},
        }
    },
    components: {
        Quiz,
        Video


    },
    async mounted() {
        console.log('mounted')
        const id = this.$route.params.id

        await axios
            .get(`/courses/${id}/`)
            .then(response => {
                console.log(response.data)
                this.course = response.data.course
                this.lessons = response.data.lessons
            })
        document.title = this.course.title + ' | Роснефть класс'

    },
    methods: {
        setActiveLesson(lesson) {
            this.activeLesson = lesson
            if (lesson.lesson_type === 'quiz') {
                this.getQuiz()
            }
        },
        getQuiz() {
            axios
                .get(`/courses/${this.course.id}/${this.activeLesson.id}/get-quiz/`)
                .then(response => {
                    console.log(response.data)
                    this.quiz = response.data
                })
        }
    }
}
</script>