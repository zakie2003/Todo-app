<script setup>
import axios from 'axios';
import { ref } from 'vue';

const props = defineProps({
    inner_data: Object,
    delete_func: Function,
    get_data: Function
});

const showEditForm = ref(false); // To toggle the edit form
const updatedMessage = ref(props.inner_data?.message); // Binding to the existing data

// Function to toggle the visibility of the edit form
const edit = async (id) => {
    showEditForm.value = !showEditForm.value;
};


const updateTask = async () => {
    try {

        const response = await axios.post("https://todo-app-vemn.onrender.com/todo/edit_todo", {
            id: props.inner_data?.id,
            message: updatedMessage.value
        });
        console.log("Task updated:", response.data);
        props.get_data();
        showEditForm.value = false; 
    } catch (error) {
        console.error("Error updating task:", error);
    }
};
</script>

<template>
    <div class="w-full mb-3 max-w-6xl p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700">
        <div class="flex justify-between items-center">
            <div class="w-80">
                <p class="mb-3 font-normal text-gray-500 dark:text-gray-400">
                    {{ props.inner_data?.message }}
                </p>
            </div>
            <div class="flex space-x-5">
                <button class="btn text-white  hover:bg-white hover:text-black px-3 py-2 rounded transition duration-300 ease-in-out" @click="edit(props.inner_data?.id)">Edit</button>
                <button class="btn text-white  hover:bg-white hover:text-black px-3 py-2 rounded transition duration-300 ease-in-out" @click="props.delete_func(props.inner_data?.id)">Delete</button>
            </div>
        </div>

        <!-- Edit form visibility -->
        <div style="background-color: #0F172A;" v-if="showEditForm" class="mt-4 p-4 bg-gray-200 rounded-lg">
            <textarea 
                v-model="updatedMessage" 
                class="w-full p-2 mb-3 text-white bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                rows="3"
            ></textarea>
            <div class="flex justify-end gap-2">
                <button @click="showEditForm = false" class="px-4 py-2 bg-gray-600 text-white rounded-lg">Cancel</button>
                <button @click="updateTask" class="px-4 py-2 bg-blue-600 text-white rounded-lg">Save</button>
            </div>
        </div>
    </div>
</template>
