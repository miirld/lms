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


                        <article class="media">
                            <div class="media-left">
                                <figure class="image is-48x48">
                                    <img class="is-rounded" src="https://placehold.co/48x48" />
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong>Рудаков Михаил Дмитриевич</strong>
                                        <br />
                                        <small>18 марта 2024 18:45</small>
                                    </p>
                                    <p>
                                        Банальные, но неопровержимые выводы, а также независимые государства, вне
                                        зависимости от их уровня,
                                        должны быть подвергнуты целой серии независимых исследований. Есть над чем
                                        задуматься: интерактивные
                                        прототипы набирают популярность среди определенных слоев населения, а значит,
                                        должны быть в равной
                                        степени предоставлены сами себе. Господа, начало повседневной работы по
                                        формированию позиции
                                        позволяет оценить значение направлений прогрессивного развития.
                                    </p>
                                </div>
                                <figure class="image">
                                    <img src="https://placehold.co/4000x2000">
                                </figure>
                            </div>
                        </article>

                        <article class="media">
                            <div class="media-left">
                                <figure class="image is-48x48">
                                    <img class="is-rounded" src="https://placehold.co/48x48" />
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong>Рудаков Михаил Дмитриевич</strong>
                                        <br />
                                        <small>18 марта 2024 18:45</small>
                                    </p>
                                    <p>
                                        Банальные, но неопровержимые выводы, а также независимые государства, вне
                                        зависимости от их уровня,
                                        должны быть подвергнуты целой серии независимых исследований. Есть над чем
                                        задуматься: интерактивные
                                        прототипы набирают популярность среди определенных слоев населения, а значит,
                                        должны быть в равной
                                        степени предоставлены сами себе. Господа, начало повседневной работы по
                                        формированию позиции
                                        позволяет оценить значение направлений прогрессивного развития.
                                    </p>
                                </div>
                                <figure class="image">
                                    <img src="https://placehold.co/4000x2000">
                                </figure>
                            </div>
                        </article>

                        <article class="media">
                            <div class="media-left">
                                <figure class="image is-48x48">
                                    <img class="is-rounded" src="https://placehold.co/48x48" />
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <strong>Рудаков Михаил Дмитриевич</strong>
                                        <br />
                                        <small>18 марта 2024 18:45</small>
                                    </p>
                                    <p>
                                        Банальные, но неопровержимые выводы, а также независимые государства, вне
                                        зависимости от их уровня,
                                        должны быть подвергнуты целой серии независимых исследований. Есть над чем
                                        задуматься: интерактивные
                                        прототипы набирают популярность среди определенных слоев населения, а значит,
                                        должны быть в равной
                                        степени предоставлены сами себе. Господа, начало повседневной работы по
                                        формированию позиции
                                        позволяет оценить значение направлений прогрессивного развития.
                                    </p>
                                </div>
                                <figure class="image">
                                    <img src="https://placehold.co/4000x2000">
                                </figure>
                            </div>
                        </article>


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


export default {
    name: 'HomeView',
    data() {
        return {
            dates: []
        }
    },
    mounted() {
        document.title = 'Главная страница | Роснефть класс'
    }
}
</script>