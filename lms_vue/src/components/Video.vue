<template>
    <div class="video-container">
        <figure class="image is-16by9 mx-0 ">
            <iframe class="has-ratio" referrerpolicy="strict-origin-when-cross-origin" width="640" height="360"
                :src="'https://www.youtube.com/embed/' + youtube_id" frameborder="0" allowfullscreen></iframe>
        </figure>
    </div>
</template>


<style scoped>
@media screen and (min-width: 768px) {
    .video-container {
        max-width: 75%;
    }

}
</style>



<script>
export default {
    props: ['youtube_id']
}
</script>