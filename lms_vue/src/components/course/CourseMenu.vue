<template>
    <aside class="menu mb-5">
        <p class="menu-label"><a @click="setActiveLesson(null)">{{ course.title }}</a></p>
        <template v-for="chapter in chapters" :key="chapter.id">
            <ul class="menu-list">
                <li>
                    <a v-if="chapter.lessons.length !== 0" class="has-background-light" style="pointer-events: none;">
                        <p style="overflow-wrap: break-word;">
                            <b>
                                <text-clamp :text="chapter.title" :max-height="20" auto-resize />
                            </b>
                        </p>
                    </a>
                    <ul>
                        <template v-for="lesson in chapter.lessons" :key="lesson.id">
                            <li>
                                <a @click="setActiveLesson(lesson.id)"
                                    :class="{ 'is-active': activeLessonId === lesson.id }" :title="lesson.title">
                                    <p style="overflow-wrap: break-word;">
                                        <text-clamp :text="lesson.title" :max-height="20" auto-resize />
                                    </p>
                                </a>
                            </li>
                        </template>
                    </ul>
                </li>
            </ul>
        </template>

    </aside>
</template>

<style scoped>
.menu-label a {
    color: hsl(0, 0%, 48%);
}
.menu-label a:hover {
    color: black;
}
</style>


<script>

export default {
    name: 'CourseMenu',
    props: ['chapters', 'course',],
    data() {
        return {
            activeLessonId: null,
        }
    },
    methods: {
        setActiveLesson(id) {
            this.activeLessonId = id
            this.$emit('getLesson', this.activeLessonId)
        },
    }

}


</script>