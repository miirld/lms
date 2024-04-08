<template>

    <nav class="navbar is-primary" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item"><img src="../assets/logo.svg" alt="Лого" width="50px"
                    style="max-height:80% ;"></router-link>
        </div>

        <div id="navbar-item" class="navbar-menu">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item  has-text-weight-semibold">Главная</router-link>
                <router-link to="/courses" class="navbar-item  has-text-weight-semibold">Курсы</router-link>

            </div>

            <div class="navbar-end">
                <div class="navbar-item">

                    <div class="buttons">
                        <router-link to="/my-account" class="button is-primary has-text-weight-semibold">Личный
                            кабинет</router-link>
                    </div>


                </div>
            </div>
        </div>
    </nav>
</template>