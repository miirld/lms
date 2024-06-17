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
                            <h3 class="title is-3">{{ activeLesson.title }}</h3>
                            <hr>
                            <p style="white-space: pre-wrap;">{{ activeLesson.content }}</p>
                            <figure v-if="activeLesson.get_image" class="image my-0 ml-0" style="max-width: 750px;">
                                <img :src="activeLesson.get_image">
                            </figure>
                            <template v-if="activeLesson.lesson_type === 'quiz'">
                                <Quiz :quiz="quiz" />
                            </template>
                            <template v-if="activeLesson.lesson_type === 'video'">
                                <Video :youtube_id="activeLesson.youtube_id" />
                            </template>
                        </template>
                        <template v-else>
                            <h3 class="title is-3">{{ course.title }}</h3>
                            <hr>
                            <p style="white-space: pre-wrap;">{{ course.description }}</p>
                            <figure v-if="course.get_image" class="image my-0 ml-0" style="max-width: 750px;">
                                <img :src="course.get_image">
                            </figure>
                        </template>
                    </div>
                </div>
            </div>
        </div>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
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

            small: false,
            show: false,
            isLoading: true,

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

        this.isLoading = true
        await axios
            .get(`/courses/${id}/`)
            .then(response => {
                console.log(response.data)
                this.course = response.data.course
                this.chapters = response.data.chapters
            })
        this.isLoading = false
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

        async getQuiz() {
            this.isLoading = true
            await axios
                .get(`/courses/lesson/${this.activeLesson.id}/get-quiz/`)
                .then(response => {
                    this.quiz = response.data
                })
            this.isLoading = false
        },
        async getLesson(id) {
            if (id === null) {
                this.activeLesson = null
            }
            else {
                this.isLoading = true
                await axios
                    .get(`/courses/lesson/${id}/`)
                    .then(response => {
                        this.activeLesson = response.data
                        if (this.activeLesson.lesson_type === 'quiz') {
                            this.getQuiz()
                        }
                    })
                this.isLoading = false
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