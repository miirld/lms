<template>
    <div class="landing">
        <header>
            <b-navbar class="is-primary has-text-weight-semibold">
                <template #brand>
                    <b-navbar-item tag="router-link" id="logo" :to="{ name: 'Welcome' }">
                        <img src="../assets/logo.svg" alt="Лого" width="50px" style="max-height:57.53px ;">
                        <p class="is-size-5 pt-5 mt-4">Роснефть-классы</p>
                    </b-navbar-item>
                </template>
                <template #end>
                    <b-navbar-item tag="div">
                        <div class="buttons pt-5 mt-4">
                            <router-link class="button mb-0 is-primary " :to="{ name: 'Login' }">Войти</router-link>
                        </div>
                    </b-navbar-item>
                </template>
            </b-navbar>
        </header>
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
                                    <p>В школах, находящихся в регоинах присутствия компании, организуются так
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


                                <h3 class="title is-4">Задачи</h3>
                                <p> Основная задача программы – профориентация, мотивация школьников
                                    на поступление в вузы на профильные для Компании специальности
                                    и последующее трудоустройство в «Роснефти»
                                    после получения образования </p>
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
                                    <p> Компания расширяет возможности непрерывного образования и поддерживает создание
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
    </div>

</template>

<style scoped>
#logo:hover,
#logo:focus {
    background-color: #e7cf6e;
}
</style>



<script>


export default {
    name: 'Landing',
    async mounted() {
        document.title = 'Добро пожаловать' + ' | Роснефть класс'

    },
}

</script>