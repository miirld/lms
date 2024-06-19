<template>
    <div class="study-groups">
        <div class="container">
            <section class="section">
                <div class="columns is-multiline">
                    <div class="column is-12">
                        <p class="is-size-4">
                            Успеваемость класса «{{ group.grade }}{{ group.letter }} {{ group.school.short_name }}»
                        </p>
                    </div>
                    <template v-if="totalCourses !== 0">
                        <div class="column is-12 mb-3">
                            <div class="mb-3" v-for="course in courses">
                                <b-collapse :modelValue="false" class="card" animation="slide"
                                    aria-id="contentIdForA11y3">
                                    <template #trigger="props">
                                        <div class="card-header" role="button" aria-controls="contentIdForA11y3"
                                            :aria-expanded="props.open">
                                            <p class="card-header-title">
                                                {{ course.title }}
                                            </p>
                                            <a class="card-header-icon">
                                                <b-icon :icon="props.open ? 'menu-down' : 'menu-up'">
                                                </b-icon>
                                            </a>
                                        </div>
                                    </template>

                                    <div class="card-content">
                                        <div class="content">
                                            <div class="mb-3 box" v-for="member in course.members">
                                                <p>{{ member.last_name }} {{ member.first_name }} {{
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
                    </template>
                    <template v-else>
                        <div class="column is-12">
                            <h3 class="subtitle is-3 has-text-grey">У Вас нет назначенных активностей у этой группы</h3>
                        </div>
                    </template>


                    <div class="coloumn is-12 pl-3" v-if="courses.length !== 0">
                        <CoursesPagination :isNextExists="isNextExists" :isPreviousExists="isPreviousExists"
                            :currentPage="currentPage" :totalPages="totalPages"
                            @loadNextCoursesPage="loadNextCoursesPage" />
                    </div>
                </div>
            </section>
            <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
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
            courses: {},
            group: { school: {} },
            isNextExists: false,
            isPreviousExists: false,
            currentPage: null,
            totalPages: 0,
            totalCourses: null,
            isLoading: true,

        }
    },
    components: {
        CoursesPagination
    },
    async mounted() {
        
        const id = this.$route.params.id
        
        this.isLoading = true
        await axios
            .get(`activities/group-progress/${id}/get-data/`)
            .then(response => {
                console.log(response.data)
                this.group = response.data
            })
            .catch(error => {
                console.log(error)
            })
        document.title = this.group.grade + this.group.letter + ' ' + this.group.school.short_name + ' | Роснефть класс'
        this.isLoading = false
        this.loadFirstCourses()
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
            this.isLoading = true
            await axios
                .get(`activities/group-progress/${id}/`, {
                    params: {
                        page: this.currentPage,
                    }
                })
                .then(response => {
                    console.log(response.data)
                    this.totalCourses = response.data.count
                    this.isNextExists = false
                    this.isPreviousExists = false
                    this.courses = response.data.results
                    this.totalPages = response.data.total_pages
                    
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
            this.isLoading = false
        }
    }
}
</script>