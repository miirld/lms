<template>
    <div>
        <div class="section">
            <div class="container">
                <div class="columns">
                    <div class="column" v-if="small"><button class="button is-primary mb-3" @click="setShow"><b-icon
                                :icon="show ? 'close' : 'dots-horizontal'">
                            </b-icon></button></div>
                    <div class="column scrollable is-3 pl-2" v-if="!small || show">
                        <CourseMenu :chapters="chapters" :course="course" @getLesson="getLesson" />
                    </div>
                    <div class="column is-9 content">
                        <template v-if="activeLesson">
                            <h3 class="title is-3">{{ activeLesson.title }}
                                <span class="tag is-warning" v-if="activeLessonStatus == 'started'"
                                    @click="markAsDone">Активен</span>
                                <span class="tag is-success" v-else>Завершён</span>

                            </h3>

                            <hr>
                            <p style="white-space: pre-wrap;">{{ activeLesson.content }}</p>
                            <template v-if="activeLesson.lesson_type === 'quiz'">
                                <Quiz @done="done" :quiz="quiz" />
                            </template>
                            <template v-if="activeLesson.lesson_type === 'video'">
                                <Video :youtube_id="activeLesson.youtube_id" />
                            </template>
                        </template>
                        <template v-else>
                            <h3 class="title is-3">{{ course.title }}</h3>
                            <p style="white-space: pre-wrap;">{{ course.description }}</p>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
@media screen and (min-width: 768px) {
    .scrollable {
        max-height: 100%;
        position: sticky;
        top: 3.2rem;
    }

    .content {
        padding: 0px 48px;
    }

}

.scrollable {
    max-height: calc(90vh - 87.911px);
    overflow-y: auto;
    scrollbar-width: thin
}
</style>

<script>
import axios from 'axios'
import Quiz from '@/components/course/Quiz'
import Video from '@/components/course/Video'
import CourseMenu from '@/components/course/CourseMenu'

export default {
    data() {
        return {
            course: {},
            quiz: {},

            chapters: [],
            activeLesson: null,
            activeLessonStatus: null,

            small: false,
            show: false

        }
    },
    components: {
        Quiz,
        Video,
        CourseMenu


    },
    async mounted() {
        console.log('mounted')
        const id = this.$route.params.id

        await axios
            .get(`/activities/${id}/`)
            .then(response => {
                this.course = response.data.course
                this.chapters = response.data.chapters
            })
        document.title = this.course.title + ' | Роснефть класс'

    },
    created() {
        window.addEventListener('resize', this.onResize);
        this.onResize();
    },
    destroyed() {
        window.removeEventListener('resize', this.onResize)
    },
    methods: {
        done() {
            axios
                .post(`/activities/mark-as-done/${this.activeLesson.id}/`)
                .then(response => {
                    console.log(response.data)
                    this.activeLessonStatus = response.data.status
                })
        },


        getQuiz() {
            axios
                .get(`/courses/lesson/${this.activeLesson.id}/get-quiz/`)
                .then(response => {
                    this.quiz = response.data
                })
        },
        async getLesson(id) {
            await axios
                .get(`/courses/lesson/${id}/`)
                .then(response => {
                    this.activeLesson = response.data
                    if (this.activeLesson.lesson_type === 'quiz') {
                        this.getQuiz()
                    }
                })

            if (this.activeLesson.lesson_type === 'article' || this.activeLesson.lesson_type === 'video') {
                await axios
                    .post(`/activities/mark-as-done/${this.activeLesson.id}/`)
                    .then(response => {
                        console.log(response.data)
                        this.activeLessonStatus = response.data.status
                    })
            }


            else {

                await axios
                    .get(`/activities/lesson/${id}/`)
                    .then(response => {
                        this.activeLessonStatus = response.data.status
                    })
                console.log(this.activeLessonStatus)
            }
        },
        onResize() {
            this.small = window.innerWidth <= 768;
        },
        setShow() {
            if (this.show) {
                this.show = false
            }
            else {
                this.show = true
            }
        }
    }
}
</script>