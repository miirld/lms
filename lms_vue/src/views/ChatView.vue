<template>
    <div class="chat">
        <div class="section">
            <div class="container">
                <div class="columns">
                    <div class="column" v-if="small"><button class="button is-primary mb-3" @click="setShow"><b-icon
                        :icon="show? 'close' : 'dots-horizontal'">
                            </b-icon></button></div>
                    <div class="column is-3 pl-2" v-if="!small || show">
                        <div class="columns is-multiline">
                            <div class="column is-12 pr-5">
                                <div class="field has-addons mb-0">
                                    <div class="control is-expanded">
                                        <input v-model='search' class="search input is-primary" type="text"
                                            placeholder="Искать среди всех">
                                    </div>
                                    <div class="control">
                                        <a class="button is-primary" @click="searchInterlocutors">
                                            <b-icon icon="magnify">
                                            </b-icon>
                                        </a>
                                    </div>
                                    <div class="control">
                                        <a class="button is-primary" @click="searchReset">
                                            <b-icon icon="close">
                                            </b-icon>
                                        </a>
                                    </div>
                                </div>
                            </div>
                            <div class="column is-12 scrollable" >
                                <aside class="menu">
                                    <ul class="menu-list">
                                        <template v-for="user in interlocutors" :key="user.id">
                                            <li @click="setActiveInterluctor(user.id)">
                                                <a
                                                    :title="user.last_name + ' ' + user.first_name + ' ' + user.patronymic" :class="{'is-active': user.id == activeInterluctor}">
                                                    <div class="columns is-mobile">
                                                        <div class="column is-narrow pr-0">
                                                            <figure class="image is-48x48 mx-0">
                                                                <img class="is-rounded" :src="user.get_image" />
                                                            </figure>
                                                        </div>
                                                        <div class="column">
                                                            <p>
                                                                <strong><text-clamp
                                                                        :text="user.last_name + ' ' + user.first_name + ' ' + user.patronymic"
                                                                        :max-height="20" auto-resize /></strong>
                                                            </p>
                                                            <p v-if="user.study_groups">
                                                                <small><text-clamp
                                                                        :text="school(user)"
                                                                        :max-height="20" auto-resize /></small>
                                                            </p>
                                                            <p>
                                                                <small><text-clamp :text="toRolePlusGroup(user)"
                                                                        :max-height="20" auto-resize /></small>
                                                            </p>
                                                        </div>
                                                    </div>
                                                </a>
                                            </li>
                                        </template>
                                    </ul>
                                </aside>
                            </div>
                        </div>
                    </div>
                    <div class="column is-9">
                        <div class="main-chat">
                            <div class="px-3 pb-3">
                                <p class="is-size-4">
                                    Общение
                                </p>
                            </div>
                            <div class="p-3 mb-1 chat-wrap box">
                                <div class="p-5 overflow-chat" id="test">
                                    <template v-for="message in this.activeConversation.messages">
                                        <template v-if="message.created_by.id == this.$store.state.user.id">
                                            <div class="custom-message">
                                                <div class="message-outer">
                                                    <div class="message-inner is-flex-direction-row-reverse ">
                                                        <div class="message-avatar">
                                                            <figure class="image is-48x48 my-1 ml-2">
                                                                <img class="is-rounded"
                                                                    :src="message.created_by.get_image" />
                                                            </figure>
                                                        </div>
                                                        <div class="message-content">
                                                            <div class="message-bubble has-background-primary"
                                                                style="justify-content: flex-end; margin-left: auto;">
                                                                {{ message.body }}
                                                            </div>
                                                            <div style="text-align: right;">
                                                                <small>{{ message.created_at_formatted }} назад</small>
                                                            </div>
                                                        </div>
                                                        <div class="message-spacer"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </template>
                                        <template v-else>
                                            <div class="custom-message">
                                                <div class="message-outer">
                                                    <div class="message-inner is-flex-direction-row ">
                                                        <div class="message-avatar">
                                                            <figure class="image is-48x48 my-1 mr-2">
                                                                <img class="is-rounded"
                                                                    :src="message.created_by.get_image" />
                                                            </figure>
                                                        </div>
                                                        <div class="message-content">
                                                            <div class="message-bubble has-background-light">
                                                                {{ message.body }}</div>
                                                            <p style="text-align: left;">
                                                                <small>{{ message.created_at_formatted }} назад</small>
                                                            </p>
                                                        </div>
                                                        <div class="message-spacer"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </template>
                                    </template>
                                </div>
                            </div>
                            <div class="p-3">
                                <form @submit.prevent="submitForm">
                                    <textarea v-model="body" class="textarea is-primary mb-3 " rows="2"
                                        placeholder="Введите сообщение" style="resize: none;"></textarea>
                                    <button class="button is-primary">Отправить</button>
                                </form>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
        <b-loading v-model="isLoading" :is-full-page="true"></b-loading>
    </div>
</template>


<style scoped>
@media screen and (min-width: 768px) {
    .scrollable {
        max-height: 100%;
    }
}


.scrollable {
    max-height: calc(90vh - 87.911px - 64px);
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: thin
}



.main-chat {
    display: flex;
    flex-direction: column;
    height: calc(90vh - 87.911px);
}

.chat-wrap {
    display: flex;
    flex: 1;
    min-height: 0px;

}


.overflow-chat {
    flex: 1;
    overflow-y: scroll;

    scrollbar-width: thin
}

.message-outer {
    display: flex;
    margin: 15px auto;
}

.message-inner {
    flex: 1;
    display: flex;

}

.message-spacer {
    flex: 1;
}

.message-bubble {
    border-radius: 20px;
    padding: 10px;
    height: fit-content;
    width: fit-content;
    max-width: 100%;
    overflow-wrap: break-word;

}


.message-content {
    max-width: 80%;
    display: flex;
    flex-direction: column;
}

.box {
    box-shadow: 0 0em 0em 0.125em rgba(10, 10, 10, 0.1);

}

input.search:focus {
    box-shadow: inset 0 0.0625em 0.125em rgba(10, 10, 10, 0.05);
}
</style>


<script>
import axios from 'axios'



export default {
    name: 'chat',
    data() {
        return {
            interlocutors: [],
            activeInterluctor: '',
            activeConversation: {},
            body: '',
            search: '',
            small: false,
            show: false,
            isLoading :true,
        }
    },
    mounted() {
        document.title = 'Общение | Роснефть класс'
        this.getInterlocutors()
    },
    created() {
        window.addEventListener('resize', this.onResize);
        this.onResize();
    },
    destroyed() {
        window.removeEventListener('resize', this.onResize)
    },
    methods: {
        toRolePlusGroup(user) {
            let role = ''
            if (user.role) {
                role = user.role == 'student' ? 'Ученик' : (user.role == 'teacher' ? 'Учитель' : 'Куратор')
            }
            let groups = ''
            if (user.study_groups.length !== 0){
            for (let group in user.study_groups) {
                groups += user.study_groups[group].grade + user.study_groups[group].letter + ' '
            }
        }
            return role + ' ' + groups
        },
        school(user) {
            let school = ''
            if (user.study_groups.length !== 0){
                school = user.study_groups[0].school.short_name
        }
            return school
        },

        searchReset() {
            this.search = ''
            this.getInterlocutors()
        },
        async searchInterlocutors() {
            if (this.search) {
                this.isLoading = true
                await axios
                    .get('/chat/search', {
                        params: {
                            search: this.search,

                        }
                    })
                    .then(response => {
                        this.interlocutors = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.isLoading = false
            }
        },

        setActiveInterluctor(interlocutor_id) {
            this.activeInterluctor = interlocutor_id
            this.getConversation()
        },

        async getConversation() {
            this.isLoading = true
            await axios
                .get(`/chat/${this.activeInterluctor}`)
                .then(response => {
                    console.log(response.data)
                    this.activeConversation = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            const scrollable = document.getElementById('test');
            scrollable.scrollTop = scrollable.scrollHeight;
            this.isLoading = false
        },

        async getInterlocutors() {
            this.isLoading = true
            await axios
                .get('/chat/')
                .then(response => {
                    this.interlocutors = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.isLoading = false
        },

        async submitForm() {
            if (this.body && this.activeInterluctor.length !==0) {
                await axios
                    .post('/chat/send/', {
                        body: this.body,
                        conversation_id: this.activeConversation.id
                    })
                    .then(response => {
                        this.activeConversation.messages.push(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.body = ''
            }

        },
        onResize() {
            this.small = window.innerWidth <= 768;
        },

        setShow() {
            if (this.show) {
                this.show = false
            }
            else {
                this.show = true
            }
        }
    }
}

</script>