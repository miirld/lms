<template>
    <aside class="menu">
        <p class="menu-label"><b>Категории</b></p>
        <ul class="menu-list">
            <li>
                <a @click="setActiveCategory(null)" :class="{ 'is-active': !activeCategoryId }" title="Все">
                    Все
                </a>
            </li>
            <li v-for="category in categories" :key="category.id">
                <a @click="setActiveCategory(category)" :class="{ 'is-active': activeCategoryId === category.id }"
                    :title="category.title">
                    <p style="overflow-wrap: break-word;">
                        <text-clamp :text="category.title" :max-height="20" auto-resize />
                    </p>
                </a>
            </li>
        </ul>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </aside>
</template>


<script>
import axios from 'axios'

export default {
    name: 'CoursesMenu',
    data() {
        return {
            categories: [],
            activeCategoryId: null,
            isLoading: true,
        }
    },
    mounted() {
        this.loadCategories()
    },

    methods: {
        setActiveCategory(category) {
            if (category) {
                this.activeCategoryId = category.id
            } else {
                this.activeCategoryId = null
            };
            this.$emit('resetCategory', this.activeCategoryId)

        },
        async loadCategories() {
            this.isLoading = true
            await axios
                .get('/courses/categories/')
                .then(response => {
                    this.categories = response.data
                })
            this.isLoading = false
        }
    }
}
</script>