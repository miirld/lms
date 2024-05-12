<template>
    <div class="chat">
        <div class="section">
            <div class="container">
                <div class="columns">
                    <div class="column" v-if="small"><button class="button is-primary mb-3" @click="setShow"><b-icon
                                icon="dots-horizontal">
                            </b-icon></button></div>
                    <div class="column is-3 pl-2" v-if="!small || show">
                        <div class="columns is-multiline">
                            <div class="column is-12 pr-5">
                                <div class="field has-addons">
                                    <div class="control is-expanded">
                                        <input class="input is-primary" type="text" placeholder="Введите имя" >
                                    </div>
                                    <div class="control">
                                        <a class="button is-primary">
                                            <b-icon icon="magnify">
                                            </b-icon>
                                        </a>
                                    </div>
                                </div>
                            </div>
                            <div class="column is-12 scrollable">
                                <aside class="menu">
                                    <ul class="menu-list">
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
                                        <li>
                                            <a>
                                                <div class="columns is-mobile">
                                                    <div class="column is-narrow pr-0">
                                                        <figure class="image is-48x48 mx-0">
                                                            <img class="is-rounded" src="https://placehold.co/48x48" />
                                                        </figure>
                                                    </div>
                                                    <div class="column">
                                                        <p>
                                                            <strong><text-clamp text="Рудаков Михаил Дмитриевич"
                                                                    :max-height="20" auto-resize /></strong>
                                                            <small><text-clamp text="Ученик 10Б Гимназии №3"
                                                                    :max-height="20" auto-resize /></small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </li>
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
                            <div class="p-3 chat-wrap">
                                <div class="p-5 overflow-chat">
                                    <div class="custom-message">
                                        <div class="message-outer">
                                            <div class="message-inner is-flex-direction-row ">
                                                <div class="message-avatar">
                                                    <figure class="image is-48x48 my-1 mr-2">
                                                        <img class="is-rounded" src="https://placehold.co/48x48" />
                                                    </figure>
                                                </div>
                                                <div class="message-content">
                                                    <div class="message-bubble has-background-light">Привет!</div>
                                                    <p style="text-align: left;">
                                                        <small>15 минут назад</small>
                                                    </p>
                                                </div>
                                                <div class="message-spacer"></div>
                                            </div>
                                        </div>

                                    </div>
                                    <div class="custom-message">
                                        <div class="message-outer">
                                            <div class="message-inner is-flex-direction-row-reverse ">
                                                <div class="message-avatar">
                                                    <figure class="image is-48x48 my-1 ml-2">
                                                        <img class="is-rounded" src="https://placehold.co/48x48" />
                                                    </figure>
                                                </div>
                                                <div class="message-content">
                                                    <div class="message-bubble has-background-primary"
                                                        style="justify-content: flex-end; margin-left: auto;">Привет!
                                                    </div>
                                                    <div style="text-align: right;">
                                                        <small>15 минут назад</small>
                                                    </div>
                                                </div>
                                                <div class="message-spacer"></div>
                                            </div>
                                        </div>

                                    </div>
                                    <div class="custom-message">
                                        <div class="message-outer">
                                            <div class="message-inner is-flex-direction-row ">
                                                <div class="message-avatar">
                                                    <figure class="image is-48x48 my-1 mr-2">
                                                        <img class="is-rounded" src="https://placehold.co/48x48" />
                                                    </figure>
                                                </div>
                                                <div class="message-content">
                                                    <div class="message-bubble has-background-light">По своей сути
                                                        рыбатекст
                                                        является альтернативой традиционному lorem ipsum, который
                                                        вызывает у
                                                        некторых людей недоумение при попытках прочитать рыбу текст. В
                                                        отличии от lorem ipsum, текст рыба на русском языке наполнит
                                                        любой
                                                        макет непонятным смыслом и придаст неповторимый колорит
                                                        советских
                                                        времен.</div>
                                                    <p style="text-align: left;">
                                                        <small>15 минут назад</small>
                                                    </p>
                                                </div>

                                                <div class="message-spacer"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="custom-message">
                                        <div class="message-outer">

                                            <div class="message-inner is-flex-direction-row-reverse ">
                                                <div class="message-avatar">
                                                    <figure class="image is-48x48 my-1 ml-2">
                                                        <img class="is-rounded" src="https://placehold.co/48x48" />
                                                    </figure>
                                                </div>
                                                <div class="message-content">
                                                    <div class="message-bubble has-background-primary"
                                                        style="float: right;">По своей сути
                                                        рыбатекст
                                                        является альтернативой традиционному lorem ipsum, который
                                                        вызывает у
                                                        некторых людей недоумение при попытках прочитать рыбу текст. В
                                                        отличии от lorem ipsum, текст рыба на русском языке наполнит
                                                        любой
                                                        макет непонятным смыслом и придаст неповторимый колорит
                                                        советских
                                                        времен.</div>
                                                    <p style="text-align: right;">
                                                        <small>15 минут назад</small>
                                                    </p>
                                                </div>
                                                <div class="message-spacer"></div>
                                            </div>
                                        </div>
                                    </div>





                                </div>
                            </div>
                            <div class="p-3">

                                <textarea class="textarea is-primary mb-3 " rows="2" placeholder="Введите сообщение"
                                    style="resize: none;"></textarea>
                                <button class="button is-primary">Отправить</button>

                            </div>
                        </div>



                    </div>
                </div>
            </div>
        </div>
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
    margin: 20px auto;
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
</style>


<script>
import axios from 'axios'
export default {
    name: 'messages',
    data() {
        return {
            small: false,
            show: false
        }
    },
    mounted() {
        document.title = 'Общение | Роснефть класс'
        this.getConversations()
    },
    created() {
        window.addEventListener('resize', this.onResize);
        this.onResize();
    },
    destroyed() {
        window.removeEventListener('resize', this.onResize)
    },
    methods: {
        getConversations() {
            console.log('getConversations')
            axios
                .get('/chat/')
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
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