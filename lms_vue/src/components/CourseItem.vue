<template>
    <div class="card">
        <div class="card-content">

            <h4 class="title is-4 "> 
                <b-icon icon="school">
                </b-icon> 
                 {{ course.title }}</h4>
            <div class="columns">
                <div class="column is-4">
                    <p><small><b>Преподаватель:</b> {{ course.created_by.first_name }} {{ course.created_by.last_name }}
                        {{ course.created_by.patronymic }}</small></p>

                    <p><small><b>Категории:</b> <span v-for="category in course.categories" :key="category.id">{{ category.title }}&nbsp </span> </small></p>
                </div>
                <div class="column is-offset-1 is-7">
                    <template v-if="course.preview_description">
                        <small> {{ course.preview_description }}</small>
                    </template>
                </div>
            </div>

        </div>

        <footer class="card-footer">
            <a href="#" class="card-footer-item">Продолжить</a>
        </footer>

    </div>
</template>


<style scoped>
.card {
    transition-duration: 0.1s;

}

.card:hover {
    box-shadow: 0 0.5em 1em 0.125em rgba(10, 10, 10, 0.1), 0 0px 0 1px rgba(10, 10, 10, 0.02);

}
</style>


<script>
export default {
    props: ['course']
}

</script>