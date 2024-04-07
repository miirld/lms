<template>
  <div class="home">
    <section class="section">
      <div class="container">
        <div class="columns is-mobile">
          <div class="column is-3" style="height:100%; position: sticky; top: 3.2rem;">

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
              <p class="menu-label is-inline">От</p> <input type="date">
              <br>
              <p class="menu-label is-inline">До</p> <input type="date">
            </aside>

          </div>

          <div class="column is-6">


            <article class="media">
              <figure class="media-left">
                <p class="image is-48x48">
                  <img class="is-rounded" src="https://placehold.co/48x48" />
                </p>
              </figure>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>Рудаков Михаил Дмитриевич</strong>
                    <br />
                    <small>18 марта 2024 18:45</small>
                  </p>
                  <p>
                    Банальные, но неопровержимые выводы, а также независимые государства, вне зависимости от их уровня,
                    должны быть подвергнуты целой серии независимых исследований. Есть над чем задуматься: интерактивные
                    прототипы набирают популярность среди определенных слоев населения, а значит, должны быть в равной
                    степени предоставлены сами себе. Господа, начало повседневной работы по формированию позиции
                    позволяет оценить значение направлений прогрессивного развития.
                  </p>
                </div>
                <figure>
                  <img src="https://placehold.co/4000x2000">
                </figure>
              </div>
            </article>

            <article class="media">
              <figure class="media-left">
                <p class="image is-48x48">
                  <img class="is-rounded" src="https://placehold.co/48x48" />
                </p>
              </figure>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>Рудаков Михаил Дмитриевич</strong>
                    <br />
                    <small>18 марта 2024 18:45</small>
                  </p>
                  <p>
                    Банальные, но неопровержимые выводы, а также независимые государства, вне зависимости от их уровня,
                    должны быть подвергнуты целой серии независимых исследований. Есть над чем задуматься: интерактивные
                    прототипы набирают популярность среди определенных слоев населения, а значит, должны быть в равной
                    степени предоставлены сами себе. Господа, начало повседневной работы по формированию позиции
                    позволяет оценить значение направлений прогрессивного развития.
                  </p>
                </div>
                <figure>
                  <img src="https://placehold.co/4000x2000">
                </figure>
              </div>
            </article>

            <article class="media">
              <figure class="media-left">
                <p class="image is-48x48">
                  <img class="is-rounded" src="https://placehold.co/48x48" />
                </p>
              </figure>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>Рудаков Михаил Дмитриевич</strong>
                    <br />
                    <small>18 марта 2024 18:45</small>
                  </p>
                  <p>
                    Банальные, но неопровержимые выводы, а также независимые государства, вне зависимости от их уровня,
                    должны быть подвергнуты целой серии независимых исследований. Есть над чем задуматься: интерактивные
                    прототипы набирают популярность среди определенных слоев населения, а значит, должны быть в равной
                    степени предоставлены сами себе. Господа, начало повседневной работы по формированию позиции
                    позволяет оценить значение направлений прогрессивного развития.
                  </p>
                </div>
                <figure>
                  <img src="https://placehold.co/4000x2000">
                </figure>
              </div>
            </article>
          </div>
          <div class="column is-3">
            Виджеты
          </div>
        </div>
      </div>
    </section>

  </div>
</template>


<style scoped>
input[type="checkbox"] {
  accent-color: black;
}
</style>


<script>


export default {
  name: 'HomeView',
  mounted() {
    document.title = 'Главная страница | Роснефть класс'
  }
}
</script>
