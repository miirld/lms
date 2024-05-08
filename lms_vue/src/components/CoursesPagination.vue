<template>
    <nav class="pagination">
        <a class="pagination-previous" :class="{ 'is-disabled': !isPreviousExists }"
            @click="$emit( 'loadNextCoursesPage', currentPage - 1 )">Предыдущая</a>
        <a class="pagination-next" :class="{ 'is-disabled': !isNextExists }"
            @click="$emit( 'loadNextCoursesPage', currentPage + 1)">Следующая</a>


        <ul class="pagination-list">
            <li v-if="currentPage - 2 > 1">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', 1 )">{{ 1 }}</a>
            </li>
            <li v-if="currentPage - 2 > 1">
                <span class="pagination-ellipsis">&hellip;</span>
            </li>
            <li v-if="currentPage - 2 == 1">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', 1 )">{{ 1 }}</a>
            </li>
            <li v-if="currentPage - 1 >= 1">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', currentPage - 1 )">{{
                    currentPage - 1 }}</a>
            </li>
            <li>
                <a class="pagination-link is-current">{{ currentPage }}</a>
            </li>
            <li v-if="currentPage + 1 <= totalPages">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', currentPage + 1 )">{{
                    currentPage
                    + 1 }}</a>
            </li>
            <li v-if="currentPage + 2 <= totalPages">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', currentPage + 2 )">{{
                    currentPage
                    + 2 }}</a>
            </li>
            <li v-if="currentPage + 3 == totalPages">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', totalPages )">{{ totalPages
                    }}</a>
            </li>
            <li v-if="currentPage + 3 < totalPages">
                <span class="pagination-ellipsis">&hellip;</span>
            </li>
            <li v-if="currentPage + 3 < totalPages">
                <a class="pagination-link" @click="$emit( 'loadNextCoursesPage', totalPages )">{{ totalPages
                    }}</a>
            </li>
        </ul>
    </nav>
</template>



<script>

export default {
    name: 'CoursesPagination',
    props: ['isNextExists', 'isPreviousExists', 'currentPage', 'totalPages']

}

</script>
