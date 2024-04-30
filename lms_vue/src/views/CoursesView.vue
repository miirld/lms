<template>
    <div class="courses">
        <section class="section">
            <div class="container">
                <div class="columns">

                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">Категории</p>
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

                    <div class="column is-10">
                        <div class="mx-2">

                            <template v-if="totalCourses !== 0">
                                <template v-for=" course in courses" v-bind:key="course.id">
                                    <CourseItem class="mb-5" :course="course" />
                                </template>
                                <nav v-if="totalCourses" class="pagination is-small">
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
                                            <a class="pagination-link" @click="goToPage(1)">{{1}}</a>
                                        </li>
                                        <li v-if="currentPage - 1 >= 1">
                                            <a class="pagination-link"  @click="goToPage(currentPage - 1)">{{ currentPage - 1 }}</a>
                                        </li>
                                        <li>
                                            <a class="pagination-link is-current">{{ currentPage }}</a>
                                        </li>
                                        <li v-if="currentPage + 1 <= totalPages">
                                            <a class="pagination-link" @click="goToPage(currentPage + 1)">{{ currentPage + 1 }}</a>
                                        </li>
                                        <li v-if="currentPage + 2 <= totalPages">
                                            <a class="pagination-link" @click="goToPage(currentPage + 2)">{{ currentPage + 2 }}</a>
                                        </li>
                                        <li v-if="currentPage + 3 == totalPages">
                                            <a class="pagination-link"  @click="goToPage(totalPages)">{{totalPages}}</a>
                                        </li>
                                        <li v-if="currentPage + 3 < totalPages">
                                            <span class="pagination-ellipsis">&hellip;</span>
                                        </li>
                                        <li v-if="currentPage + 3 < totalPages">
                                            <a class="pagination-link" @click="goToPage(totalPages)">{{ totalPages }}</a>
                                        </li>

                                    </ul>
                                </nav>
                            </template>

                            <template v-else>
                                <h3 class="subtitle is-3 has-text-grey" style="height:75vh;">Курсов нет</h3>
                            </template>

                        </div>
                    </div>

                </div>
            </div>
        </section>
    </div>
</template>

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
            isLoading: false,

        }
    },

    components: {
        CourseItem,
    },

    methods: {
        goToPage(n) {
            this.currentPage = n
            this.getMoreCourses()
            window.scrollTo(0, 0);
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

        getCourses(url) {
            axios
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

    mounted() {
        console.log('mounted')
        document.title = 'Курсы | Роснефть класс'
        axios
            .get('/courses/categories/')
            .then(response => {
                console.log(response.data)
                this.categories = response.data
            })
        this.getFirstCourses()
    }
}
</script>