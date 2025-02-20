<script setup>
import Cards from '@/components/Cards.vue';
import axios from 'axios';
import { defineProps } from 'vue';

const props = defineProps({
    card_data: Object,
    get_data: Function
});

const delete_data = async (id) => {
    try {
        await axios.post('https://todo-app-vemn.onrender.com/todo/delete_data', { 'id': id });
        props.get_data();
    } catch (err) {
        console.log(err);
    }
};
</script>

<template>
    <div class="flex justify-center mt-2">
        <div class="flex flex-col items-center gap-4">
            <div v-if="props.card_data.length >0">
                <Cards v-for="i in props.card_data" :delete_func="delete_data" :inner_data="i" class="w-full max-w-4xl"/>
            </div>
            <div v-else>
                <h2 class="text-white">No Data Found</h2>
            </div>
        </div>
    </div>
</template>

<style>
</style>