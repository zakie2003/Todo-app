<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import axios from "axios";
import Listing from "@/views/Lisitng.vue";

const showForm = ref(false); 
const message = ref(""); 
const card_data = ref({});
const searchQuery = ref(""); 
let searchTimeout: NodeJS.Timeout;

const toggleForm = () => {
    showForm.value = !showForm.value;
};

const add_data = async () => {
    try {
        const response = await axios.post("https://todo-app-vemn.onrender.com/todo/add_data", { message: message.value });
        console.log(response.data);
        message.value = "";
        toggleForm();
        getData();
    } catch (error) {
        console.error(error);
    }
};

const getData = async (query = "") => {
    try {
        const response = await axios.get("https://todo-app-vemn.onrender.com/todo/get_data", { params: { search: query } });
        card_data.value = response.data.data;
        console.log(response.data);
    } catch (error) {
        console.error(error);
    }
};

onMounted(() => {
    getData();
});

watch(searchQuery, (newQuery) => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        getData(newQuery);
    }, 300); 
});
</script>

<template>
    <nav class="sticky top-3 z-[9998] w-full max-w-screen-lg px-6 py-3 mx-auto bg-slate-800 bg-opacity-90 shadow-lg backdrop-blur-lg rounded-lg">
        <div class="container flex items-center justify-between mx-auto">
            <a href="#" class="text-xl font-bold text-white">Todo App</a>

            <div class="hidden lg:flex items-center gap-4">
                <button @click="toggleForm" class="btn text-white  hover:bg-white hover:text-black px-3 py-2 rounded transition duration-300 ease-in-out">
                    Add
                </button>

                <input 
                    type="text" 
                    v-model="searchQuery"
                    placeholder="Search..."
                    class="px-4 py-2 text-white bg-transparent border border-white rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>

            <button class="lg:hidden p-2 text-white hover:bg-slate-700 rounded-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
    </nav>

    <div v-if="showForm" class="fixed z-[9999] inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-slate-800 bg-opacity-95 p-6 rounded-lg shadow-lg max-w-md w-full">
            <h2 class="text-white text-xl font-semibold mb-4">Add New Task</h2>
            <form @submit.prevent="add_data">
                <textarea 
                    v-model="message" 
                    placeholder="Task Details" 
                    class="w-full p-2 mb-3 text-white bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    rows="3"
                    required
                ></textarea>
                <div class="flex justify-end gap-2">
                    <button type="button" @click="toggleForm" class="px-4 py-2 bg-gray-600 text-white rounded-lg">Cancel</button>
                    <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-lg">Add</button>
                </div>
            </form>
        </div>
    </div>

    <div class="container px-6 py-6">
        <Listing :card_data="card_data" :get_data="getData" />
    </div>
</template>
