<script setup>
import { ref } from 'vue'
import SearchBar from '../components/SearchBar.vue'

const input = ref(null)
</script>

<template>
  <div class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">NBA Stat Explorer</h1>
        <p class="py-6">
          Discover NBA player stats: Explore performance, milestones, and insights like never
          before!
          {{ input }}
        </p>
        <SearchBar v-model:input="input" />
      </div>
    </div>
  </div>
</template>
