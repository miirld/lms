<template>
    <div class="courses">
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
        <section class="section">
            <div class="container">
                <div class="columns">

                    <div class="column is-2" id="filter">
                        <aside class="menu">
                            <p class="menu-label"><b>Категории</b></p>

                            <ul class="menu-list">
                                <li>
                                    <a :class="{ 'is-active': !activeCategory.id }" @click="setActiveCategory(null)">
                                        Все
                                    </a>
                                </li>

                                <li v-for="category in categories" :key="category.id">
                                    <a @click="setActiveCategory(category)"
                                        :class="{ 'is-active': activeCategory.id === category.id }">
                                        {{ category.title }}
                                    </a>
                                </li>
                            </ul>
                        </aside>
                    </div>

                    <div class="column is-10 mx-2">
                        <div class="columns is-multiline">
                            <div class="column is-12 is-size-4">
                                Курсы
                            </div>
                            <div class="column is-12">
                                <template v-if="totalCourses !== 0">
                                    <template v-for=" course in courses" v-bind:key="course.id">
                                        <CourseItem class="mb-5" :course="course" />
                                    </template>
                                </template>
                                <template v-else>
                                    <h3 class="subtitle is-3 has-text-grey" style="height:75vh;">Курсов нет</h3>
                                </template>
                            </div>
                            <div v-if="totalCourses !== 0" class="column is-12">
                                <nav v-if="totalCourses" class="pagination">
                                    <a class="pagination-previous" :class="{ 'is-disabled': !isPreviousExists }"
                                        @click="goToPage(currentPage - 1)">Предыдущая</a>
                                    <a class="pagination-next" :class="{ 'is-disabled': !isNextExists }"
                                        @click="goToPage(currentPage + 1)">Следующая</a>


                                    <ul class="pagination-list">
                                        <li v-if="currentPage - 2 > 1">
                                            <a class="pagination-link" @click="goToPage(1)">{{ 1 }}</a>
                                        </li>
                                        <li v-if="currentPage - 2 > 1">
                                            <span class="pagination-ellipsis">&hellip;</span>
                                        </li>
                                        <li v-if="currentPage - 2 == 1">
                                            <a class="pagination-link" @click="goToPage(1)">{{ 1 }}</a>
                                        </li>
                                        <li v-if="currentPage - 1 >= 1">
                                            <a class="pagination-link" @click="goToPage(currentPage - 1)">{{
                                                currentPage
                                                - 1 }}</a>
                                        </li>
                                        <li>
                                            <a class="pagination-link is-current">{{ currentPage }}</a>
                                        </li>
                                        <li v-if="currentPage + 1 <= totalPages">
                                            <a class="pagination-link" @click="goToPage(currentPage + 1)">{{
                                                currentPage
                                                + 1 }}</a>
                                        </li>
                                        <li v-if="currentPage + 2 <= totalPages">
                                            <a class="pagination-link" @click="goToPage(currentPage + 2)">{{
                                                currentPage
                                                + 2 }}</a>
                                        </li>
                                        <li v-if="currentPage + 3 == totalPages">
                                            <a class="pagination-link" @click="goToPage(totalPages)">{{ totalPages
                                                }}</a>
                                        </li>
                                        <li v-if="currentPage + 3 < totalPages">
                                            <span class="pagination-ellipsis">&hellip;</span>
                                        </li>
                                        <li v-if="currentPage + 3 < totalPages">
                                            <a class="pagination-link" @click="goToPage(totalPages)">{{ totalPages
                                                }}</a>
                                        </li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
@media screen and (min-width: 1024px) {
    #filter {
        height: 100%;
        position: sticky;
        top: 3.2rem;
    }

}
</style>

<script>
import axios from 'axios'
import CourseItem from '@/components/CourseItem'

export default {
    name: 'CourseView',
    data() {
        return {
            courses: [],
            categories: [],
            activeCategory: {
                'id': null,
                'title': null
            },
            isNextExists: false,
            isPreviousExists: false,
            currentPage: null,
            totalPages: null,
            totalCourses: null,
            isLoading: true,

        }
    },

    components: {
        CourseItem,
    },

    methods: {
        goToPage(n) {
            this.currentPage = n
            this.getMoreCourses()
        
        },

        setActiveCategory(category) {
            if (category) {
                this.activeCategory = category
            } else {
                this.activeCategory = {
                    'id': null,
                    'title': null
                }
            }
            this.getFirstCourses()
        },

        async getCourses(url) {
            this.isLoading = true
            await axios
                .get(url)
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
            window.scrollTo(0, 0);
            this.isLoading = false

        },

        getFirstCourses() {
            this.isNextExists = false
            this.isPreviousExists = false
            this.currentPage = 1
            this.totalPages = null
            let url = '/courses/'
            if (this.activeCategory.id) {
                url += '?category_id=' + this.activeCategory.id
            }
            this.getCourses(url)
        },

        getMoreCourses() {
            this.isNextExists = false
            this.isPreviousExists = false
            let url = '/courses/'
            url += '?page=' + this.currentPage
            if (this.activeCategory.id) {
                url += '&category_id=' + this.activeCategory.id
            }
            this.getCourses(url)
        }
    },

    async mounted() {
        console.log('mounted')
        document.title = 'Курсы | Роснефть класс'
        this.isLoading = true
        await axios
            .get('/courses/categories/')
            .then(response => {
                console.log(response.data)
                this.categories = response.data
            })
        this.getFirstCourses()
        this.isLoading = false
    }
}
</script>