<template>
    <div>
        <div class="section">
            <div class="container">
                <div class="columns">
                    <div class="column" v-if="small"><button class="button is-primary mb-3" @click="setShow"><b-icon
                                icon="dots-horizontal">
                            </b-icon></button></div>
                    <div class="column scrollable is-3 pl-2" v-if="!small || show">
                        <aside class="menu mb-5">
                            <template v-for="chapter in chapters" :key="chapter.id">
                                <ul class="menu-list">
                                    <li>
                                        <a v-if="chapter.lessons.length !== 0" class="has-background-light"
                                            style="pointer-events: none;">
                                            <p style="overflow-wrap: break-word;">
                                                <b>
                                                    <text-clamp :text="chapter.title" :max-height="20" auto-resize />
                                                </b>
                                            </p>
                                        </a>
                                        <ul>
                                            <template v-for="lesson in chapter.lessons" :key="lesson.id">
                                                <li>
                                                    <a @click="setActiveLesson(lesson.id)"
                                                        :class="{ 'is-active': activeLessonId === lesson.id }"
                                                        :title="lesson.title">
                                                        <p style="overflow-wrap: break-word;">
                                                            <text-clamp :text="lesson.title" :max-height="20"
                                                                auto-resize />
                                                        </p>
                                                    </a>
                                                </li>
                                            </template>
                                        </ul>
                                    </li>
                                </ul>
                            </template>

                        </aside>
                    </div>
                    <div class="column is-9 content">
                        <template v-if="activeLesson">
                            <h3 class="title is-3">{{ activeLesson.title }}</h3>
                            <hr>
                            <p style="white-space: pre-wrap;">{{ activeLesson.content }}</p>
                            <template v-if="activeLesson.lesson_type === 'quiz'">
                                <Quiz :quiz="quiz" />
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
import Quiz from '@/components/Quiz'
import Video from '@/components/Video'

export default {
    data() {
        return {
            course: {},
            quiz: {},

            chapters: [],
            activeLessonId: null,
            activeLesson: null,

            small: false,
            show: false

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
        setActiveLesson(id) {
            this.activeLessonId = id
            this.getLesson()
        },
        getQuiz() {
            axios
                .get(`/courses/lesson/${this.activeLesson.id}/get-quiz/`)
                .then(response => {
                    this.quiz = response.data
                })
        },
        getLesson() {
            axios
                .get(`/courses/lesson/${this.activeLessonId}/`)
                .then(response => {
                    this.activeLesson = response.data
                    if (this.activeLesson.lesson_type === 'quiz') {
                        this.getQuiz()
                    }
                })
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