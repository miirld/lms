<template>
    <div class="study-groups">
        <div class="container">
            <section class="section">
                <div class="columns is-multiline">
                    <div class="column is-12">
                        <p class="is-size-4">
                            Успеваемость по курсу "{{ course.title }}"
                        </p>
                    </div>
                    <div class="column is-12 mb-3">
                        <div class="mb-3" v-for="group in groups">
                            <b-collapse :modelValue="false" class="card" animation="slide" aria-id="contentIdForA11y3">
                                <template #trigger="props">
                                    <div class="card-header" role="button" aria-controls="contentIdForA11y3"
                                        :aria-expanded="props.open">
                                        <p class="card-header-title">
                                            {{ group.grade }} {{ group.letter }} {{ group.school.short_name }}
                                        </p>
                                        <a class="card-header-icon">
                                            <b-icon :icon="props.open ? 'menu-down' : 'menu-up'">
                                            </b-icon>
                                        </a>
                                    </div>
                                </template>

                                <div class="card-content">
                                    <div class="content">
                                        <div class="mb-3 box" v-for="member in group.members">
                                            <p>{{ member.first_name }} {{ member.last_name }} {{
                                                member.patronymic }}</p>
                                            <template v-for="activity in member.activities">
                                                <b-icon
                                                    :title="activity.lesson.title + ' - ' + activity.lesson.chapter.title"
                                                    icon="square"
                                                    :type="activity.status == 'done' ? 'is-primary' : 'is-light'">
                                                </b-icon>
                                            </template>

                                        </div>
                                    </div>
                                </div>
                            </b-collapse>
                        </div>


                    </div>
                    <div class="coloumn is-12 pl-3">
                        <CoursesPagination :isNextExists="isNextExists" :isPreviousExists="isPreviousExists"
                            :currentPage="currentPage" :totalPages="totalPages"
                            @loadNextCoursesPage="loadNextCoursesPage" />
                    </div>
                </div>
            </section>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import CoursesPagination from '@/components/courses/CoursesPagination'
export default {
    name: 'EducationalProgress',
    data() {
        return {
            groups: {},
            course: {},
            isNextExists: false,
            isPreviousExists: false,
            currentPage: null,
            totalPages: 0,
            totalCourses: null,

        }
    },
    components: {
        CoursesPagination
    },
    async mounted() {
        this.loadFirstCourses()
        const id = this.$route.params.id
        await axios
            .get(`activities/course-progress/${id}/`)
            .then(response => {
                this.course = response.data
            })
            .catch(error => {
                console.log(error)
            })
        document.title = 'Успеваемость- '+ this.course.title + ' | Роснефть класс'
    },
    methods: {
        loadFirstCourses() {
            this.currentPage = 1
            this.loadCourses()
        },
        loadNextCoursesPage(n) {
            this.currentPage = n
            this.loadCourses()
        },
        async loadCourses() {
            const id = this.$route.params.id
            this.isNextExists = false
            this.isPreviousExists = false
            this.isLoading = true
            await axios
                .get(`activities/course-progress/${id}/groups`, {
                    params: {
                        page: this.currentPage,
                    }
                })
                .then(response => {
                    this.groups = response.data.results
                    this.totalPages = response.data.total_pages
                    this.totalCourses = response.data.count
                    if (response.data.previous) {
                        this.isPreviousExists = true
                    }
                    if (response.data.next) {
                        this.isNextExists = true
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>