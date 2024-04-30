<template>
    <div class="home">
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-3" id="filter">

                        <aside class="menu">
                            <p class="menu-label"><b>Тип</b></p>
                            <ul class="menu-list">
                                <li>
                                    <a>
                                        <label class="checkbox ">
                                            <input type="checkbox" value="article" v-model="types" />
                                            Статьи
                                        </label>
                                    </a>
                                </li>
                                <li>
                                    <a>
                                        <label class="checkbox">
                                            <input type="checkbox" value="message" v-model="types" />
                                            Сообщения
                                        </label>
                                    </a>
                                </li>
                            </ul>
                            <p class="menu-label"><b>Дата</b></p>
                            <b-datepicker placeholder="Выберите дату" v-model="dates" class="mb-3" range>
                            </b-datepicker>
                            <button class="button is-primary is-fullwidth" @click="load">Применить</button>
                        </aside>

                    </div>

                    <div class="column is-7">
                        <div class="mx-2">
                            <template v-if="news.length !== 0">
                                <template v-for="article in news" :key="article.id">
                                    <ArticleItem class="" :article="article" />
                                </template>
                                <Trigger v-if="hasNext" @triggerIntersected="loadMore" />
                            </template>
                            <template v-else>
                                <h3 class="subtitle is-3 has-text-grey" style="height:75vh;">Новостей нет</h3>
                            </template>
                        </div>
                    </div>

                </div>
            </div>
        </section>

    </div>
</template>


<style scoped>
input[type="checkbox"] {
    accent-color: #e7cf6e;
}

/* Помещение изображений за всплывающим окном выбора даты */
img {
    z-index: -1;
    position: relative;
}

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
import Trigger from '@/components/Trigger'
import ArticleItem from '@/components/ArticleItem'

export default {
    name: 'HomeView',

    data() {
        return {
            news: [],
            dates: [],
            types: [],
            currentPage: 1,
            hasNext: false

        }
    },

    computed: {
        typeDates() {
            if (this.dates.length !== 0) {
                let from = new Date(this.dates[0]).valueOf();
                let to = new Date(this.dates[1]).valueOf();
                return [from, to]
            }
            return []
        }
    },

    components: {
        Trigger,
        ArticleItem
    },

    mounted() {
        document.title = 'Главная страница | Роснефть класс'
        this.load()
    },

    methods: {
        loadMore() {
            console.log('loadMore')
            this.currentPage += 1;

            axios
                .get('/news/', {
                    params: {
                        page: this.currentPage,
                        types: this.types,
                        dates: this.typeDates
                    }
                })
                .then(response => {
                    this.news = [...this.news, ...response.data.results]
                    this.hasNext = false
                    if (response.data.next) {
                        this.hasNext = true
                    }
                })
                .catch(error => {
                    console.log(error)
                })

        },
        load() {
            console.log('doFilter')
            this.hasNext = false
            this.news = []
            this.currentPage = 1

            axios
                .get('/news/', {
                    params: {
                        page: 1,
                        types: this.types,
                        dates: this.typeDates
                    }
                })
                .then(response => {
                    this.news = response.data.results
                    if (response.data.next) {
                        this.hasNext = true
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }

    }
}
</script>