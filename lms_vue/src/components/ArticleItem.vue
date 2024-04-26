<template>
    <article class="media">

        <div class="media-content">
            <div class="content">
                <div class="columns is-mobile">
                    <div class="column is-narrow pr-0">

                        <figure class="image is-48x48 mx-0">
                            <img class="is-rounded" :src="article.created_by.get_image" />
                        </figure>
                    </div>
                    <div class="column">
                        <p>
                            <strong>{{ article.created_by.first_name }} {{ article.created_by.last_name }}
                                {{ article.created_by.patronymic }}</strong>
                            <br />
                            <small>{{ article.created_at }}</small>
                        </p>
                    </div>

                </div>

                <text-clamp :text="article.content" :max-lines="6" auto-resize style="white-space: pre-wrap;">
                    <template #after="{ toggle, expanded, clamped }">
                        <br>
                        <a v-if="expanded || clamped" @click="toggle">
                            <b-icon :icon="clamped == true ? 'menu-down' : 'menu-up'"></b-icon>
                            {{ clamped == true ? " Показать больше" : "Скрыть" }}
                        </a>
                    </template>
                </text-clamp>

            </div>
            <figure class="image">
                <img :src="article.get_image">
            </figure>
        </div>
    </article>
</template>

<style scoped>
a:hover {
    color: #e7cf6e;
}
</style>

<script>
export default {
    props: ["article",],
}
</script>