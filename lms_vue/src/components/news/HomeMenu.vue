<template>
    <aside class="menu">
        <p class="menu-label"><b>Тип</b></p>
        <ul class="menu-list">
            <li>
                <a>
                    <label class="checkbox ">
                        <input type="checkbox" value="article" v-model="types" />
                        Статьи
                    </label>
                </a>
            </li>
            <li>
                <a>
                    <label class="checkbox">
                        <input type="checkbox" value="message" v-model="types" />
                        Сообщения
                    </label>
                </a>
            </li>
        </ul>
        <p class="menu-label">
            <b>Дата</b> <button v-if="datesSelected" class="delete is-small" @click="clearDates"></button>
        </p>
        <b-datepicker placeholder="Выберите дату" v-model="dates" class="mb-3" range :mobile-native="false"/>
        <button class="button is-primary is-fullwidth" @click="resetFilters">Применить</button>
    </aside>
</template>

<style scoped>
input[type="checkbox"] {
    accent-color: #e7cf6e;
}
</style>


<script>
export default {
    name: 'HomeMenu',
    data() {
        return {
            dates: [],
            types: [],
            datesSelected: false
        }
    },
    computed: {
        typeDates() {
            if (this.dates.length !== 0) {
                let from = new Date(this.dates[0]).valueOf();
                let to = new Date(this.dates[1]).valueOf();
                return [from, to]
            }
            return []
        }
    },
    methods: {
        clearDates(){
            this.dates=[]
            this.datesSelected = false
            this.resetFilters()
        },
        resetFilters(){
            if (this.dates.length!==0){
                this.datesSelected = true
            }
            this.$emit('resetFilters', this.typeDates, this.types)
        }
    }
}
</script>