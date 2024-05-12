<template>
    <div class="home">
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-3" id="filter">
                        <HomeMenu @resetFilters="resetFilters" />
                    </div>
                    <div class="column is-7 mx-2">
                        <div class="columns is-multiline">
                            <div class="column is-12 is-size-4">
                                Новостная лента
                            </div>
                            <div class="column is-12">
                                <template v-if="totalNews !== 0">
                                    <template v-for="article in news" :key="article.id">
                                        <ArticleItem :article="article" />
                                    </template>
                                    <Trigger v-if="hasNext" @triggerIntersected="loadMoreCourses" />
                                </template>
                                <template v-else>
                                    <h3 class="subtitle is-3 has-text-grey">Новостей нет</h3>
                                </template>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
/* Помещение изображений за всплывающим окном выбора даты */
img {
    z-index: -1;
    position: relative;
}

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
import Trigger from '@/components/news/Trigger'
import ArticleItem from '@/components/news/ArticleItem'
import HomeMenu from '@/components/news/HomeMenu.vue'

export default {
    name: 'HomeView',

    data() {
        return {
            news: [],
            types: [],
            dates: [],
            currentPage: 1,
            hasNext: false,
            isLoading: true,
            totalNews: null,
        }
    },

    components: {
        Trigger,
        ArticleItem,
        HomeMenu
    },

    mounted() {
        document.title = 'Главная страница | Роснефть класс'
        this.loadFirstCourses()
    },

    methods: {
        resetFilters(dates, types) {
            this.dates = dates
            this.types = types
            this.loadFirstCourses()
        },
        loadFirstCourses() {
            this.news = []
            this.currentPage = 1
            this.hasNext = false
            this.loadCourses()
        },
        loadMoreCourses() {
            this.currentPage += 1
            this.loadCourses()
        },
        async loadCourses() {
            this.isLoading = true
            await axios
                .get('/news/', {
                    params: {
                        page: this.currentPage,
                        types: this.types,
                        dates: this.dates
                    }
                })
                .then(response => {
                    this.news = [...this.news, ...response.data.results]
                    this.totalNews = response.data.count
                    this.hasNext = false
                    if (response.data.next) {
                        this.hasNext = true
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