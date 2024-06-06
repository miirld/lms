<template>
    <header>
        <b-navbar class="is-primary has-text-weight-semibold">
            <template #brand>
                <b-navbar-item tag="router-link" id="logo" :to="{ name: 'Welcome' }">
                    <img src="../assets/logo.svg" alt="Лого" width="50px" style="max-height:57.53px ;">
                    <p class="is-size-5 pt-5 mt-4">Роснефть-классы</p>
                </b-navbar-item>
            </template>
            <template #end>
                <b-navbar-item tag="router-link" :to="{ name: 'Login' }" >
                    <b-icon class="m-3" icon="login-variant" size="is-medium" />
                </b-navbar-item>
            </template>
        </b-navbar>
    </header>
</template>

<style scoped>
#logo:hover,
#logo:focus {
    background-color: #e7cf6e;
}
</style>


<script>

export default {
    name: 'Nav',

}

</script>