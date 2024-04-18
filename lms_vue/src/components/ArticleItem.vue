<template>
    <article class="media">
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
</template>

<script>
export default {
    props: ["article",],
}
</script>