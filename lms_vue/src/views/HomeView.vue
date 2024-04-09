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
                                            <input type="checkbox" />
                                            Новости
                                        </label>
                                    </a>
                                </li>
                                <li>
                                    <a>
                                        <label class="checkbox">
                                            <input type="checkbox" />
                                            Сообщения
                                        </label>
                                    </a>
                                </li>
                            </ul>

                            <p class="menu-label"><b>Дата</b></p>
                            <b-datepicker placeholder="Выберите дату" class="mb-3" range>
                            </b-datepicker>
                            <button class="button is-primary is-fullwidth">Применить</button>
                        </aside>

                    </div>

                    <div class="column is-7">


                        <article class="media" v-for="article in news" :key="article.id">
                            <div class="media-left">
                                <figure class="image is-48x48">
                                    <img class="is-rounded" :src="article.created_by.get_image" />
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong>{{ article.created_by.first_name }} {{ article.created_by.last_name }}
                                            {{ article.created_by.patronymic }}</strong>
                                        <br />
                                        <small>{{ article.created_at }}</small>
                                    </p>
                                    <p>
                                        {{ article.short_description }}
                                    </p>
                                </div>
                                <figure class="image">
                                    <img :src="article.get_image">
                                </figure>
                            </div>
                        </article>


                        <Trigger v-if="hasNext" @triggerIntersected="loadMore" />




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

export default {

    name: 'HomeView',
    data() {
        return {
            dates: [],
            news: [],
            currentPage: 1,
            hasNext: false,

        }
    },
    components: {
        Trigger,
    },
    async beforeMount() {
        document.title = 'Главная страница | Роснефть класс'
        await axios
            .get('/news/?page=1')
            .then(response => {
                this.news = response.data.results
                if (response.data.next) {
                    this.hasNext = true
                }

            })
            .catch(error => {
                console.log(error)
            })




    },
    methods: {
        async loadMore() {
            console.log('loadMore')
            this.currentPage += 1;

            await axios
                .get(`/news/?page=${this.currentPage}`)
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

        }

    }
}
</script>