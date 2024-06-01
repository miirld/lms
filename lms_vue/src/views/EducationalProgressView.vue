<template>
    <div class="courses">
        <section class="section">
            <div class="container">
                <div class="columns is-multiline">
                    <div class="column is-12 is-size-4">
                        <div class="container">Успеваемость</div>
                    </div>
                    <template v-if="totalCourses !== 0">
                        <div class="column is-12" v-for="group in groups">
                            <div class="card">
                                <div class="card-content is-size-5">
                                    <b-icon icon="account-group">
                                    </b-icon>
                                    {{ group.grade }} {{ group.letter }} {{ group.school.short_name }}
                                </div>

                                <footer class="card-footer">
                                    <router-link class="card-footer-item"
                                        :to="{ name: 'CourseProgress', params: { id: group.id } }">Смотреть
                                        прогресс</router-link>

                                </footer>

                            </div>

                        </div>
                    </template>
                    <template v-else>
                        <div class="column is-12">
                            <h3 class="subtitle is-3 has-text-grey">Вы не назначали активности ни одной группе</h3>
                        </div>
                    </template>
                    <div class="column is-12" v-if="groups.length !== 0">
                        <CoursesPagination :isNextExists="isNextExists" :isPreviousExists="isPreviousExists"
                            :currentPage="currentPage" :totalPages="totalPages"
                            @loadNextCoursesPage="loadNextCoursesPage" />
                    </div>
                </div>
            </div>
        </section>
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
import ProgressItem from '@/components/progress/ProgressItem'
import CoursesMenu from '@/components/courses/CoursesMenu'
import CoursesPagination from '@/components/courses/CoursesPagination'

export default {
    name: 'CourseView',
    data() {
        return {
            groups: [],
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

    mounted() {
        document.title = 'Успеваемость | Роснефть класс'
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
        loadCourses() {
            axios
                .get('/activities/my-groups/', {
                    params: {
                        page: this.currentPage,
                    }
                })
                .then(response => {
                    console.log(response.data)
                    this.groups = response.data.results
                    this.totalPages = response.data.total_pages
                    this.totalCourses = response.data.count
                    this.isNextExists = false
                    this.isPreviousExists = false
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
        },
    },
}
</script>