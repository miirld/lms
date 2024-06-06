<template>
    <div class="landing">
        <div class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-4">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-12by9">
                                    <img src="../assets/landing1.jpg" alt="Placeholder image" />
                                </figure>
                            </div>
                            <div class="card-content">

                                <div class="content">
                                    <h3 class="title is-4">Роснефть-классы</h3>
                                    <p style="max-height: 120px; overflow-y: auto; scrollbar-width: thin">В школах, находящихся в регоинах присутствия компании, организуются так
                                        называемые
                                        «Роснефть-классы», это 10 и 11 классы с углубленным изучением предметов
                                        инженерного
                                        профиля </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-12by9">
                                    <img src="../assets/landing2.jpg" alt="Placeholder image" />
                                </figure>
                            </div>
                            <div class="card-content">
                                <div class="content">
                                    <h3 class="title is-4">Задачи программы</h3>
                                    <p style="max-height: 120px; overflow-y: auto; scrollbar-width: thin"> Основная задача программы – профориентация, мотивация школьников
                                        на поступление в вузы на профильные для Компании специальности
                                        и последующее трудоустройство в «Роснефти»
                                        после получения образования </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-12by9">
                                    <img src="../assets/landing4.jpg" alt="Placeholder image" />
                                </figure>
                            </div>
                            <div class="card-content">

                                <div class="content">
                                    <h3 class="title is-4">Цифровое образование</h3>
                                    <p style="max-height: 120px; overflow-y: auto; scrollbar-width: thin"> Компания расширяет возможности непрерывного образования и поддерживает создание
                                        цифровой
                                        образовательной среды. Большинство школ-партнеров компании обеспечены
                                        современным
                                        цифровым оборудованием
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </div>

</template>





<script>


export default {
    name: 'Landing',
    data () {
        return {
            isLoading : true,
        }
    },
    async mounted() {
        document.title = 'Добро пожаловать' + ' | Роснефть класс'
        this.isLoading = false

    },
}

</script>