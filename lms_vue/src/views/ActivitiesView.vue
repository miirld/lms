<template>
    <div class="courses">
        <section class="section">
            <div class="container">
                <div class="columns">

                    <div class="column is-2" id="filter">
                        <CoursesMenu @resetCategory="resetCategory" />
                    </div>

                    <div class="column is-10 mx-2">
                        <div class="columns is-multiline">
                            <div class="column is-12 is-size-4">
                                <div class="container">Активности</div>
                            </div>
                            <div class="column is-12">
                                <template v-if="totalCourses !== 0">
                                    <template v-for=" course in courses" v-bind:key="course.id">
                                        <CourseItem class="mb-5" :course="course" />
                                    </template>
                                </template>
                                <template v-else>
                                    <h3 class="subtitle is-3 has-text-grey">Активностей нет</h3>
                                </template>
                            </div>

                            <div v-if="courses.length !== 0" class="column is-12">
                                <CoursesPagination :isNextExists="isNextExists" :isPreviousExists="isPreviousExists"
                                    :currentPage="currentPage" :totalPages="totalPages"
                                    @loadNextCoursesPage="loadNextCoursesPage" />
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </div>
</template>

<style scoped>
@media screen and (min-width: 768px) {
    #filter {
        height: 100%;
        position: sticky;
        top: 3.2rem;
    }

}
</style>

<script>
import axios from 'axios'
import CourseItem from '@/components/activities/ActivityItem'
import CoursesMenu from '@/components/courses/CoursesMenu'
import CoursesPagination from '@/components/courses/CoursesPagination'

export default {
    name: 'CourseView',
    data() {
        return {
            courses: [],
            isNextExists: false,
            isPreviousExists: false,
            currentPage: null,
            totalPages: 0,
            totalCourses: null,
            isLoading: true,
            activeCategoryId: null,

        }
    },

    components: {
        CourseItem,
        CoursesMenu,
        CoursesPagination
    },

    async mounted() {
        document.title = 'Курсы | Роснефть класс'
        this.loadFirstCourses()
    },

    methods: {
        resetCategory(activeCategoryId) {
            this.activeCategoryId = activeCategoryId
            this.loadFirstCourses()
        },
        loadActivities() {
            axios
                .get('/activities/')
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        loadFirstCourses() {
            this.currentPage = 1
            this.loadCourses()
        },
        loadNextCoursesPage(n) {
            this.currentPage = n
            this.loadCourses()
        },
        async loadCourses() {
            this.isNextExists = false
            this.isPreviousExists = false
            this.isLoading = true
            await axios
                .get('/activities/', {
                    params: {
                        page: this.currentPage,
                        category_id: this.activeCategoryId
                    }
                })
                .then(response => {
                    this.courses = response.data.results
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
            window.scrollTo(0, 0);
            this.isLoading = false
        },
    },
}
</script>