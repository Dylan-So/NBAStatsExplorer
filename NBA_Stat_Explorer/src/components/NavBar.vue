<script lang="ts">
import ThemeToggle from './ThemeToggle.vue'
export default {
  components: {
    ThemeToggle
  }
}
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h7"
            />
          </svg>
        </div>
        <ul
          tabindex="0"
          class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
        >
          <li><RouterLink :to="{ name: 'Home' }">Homepage</RouterLink></li>
          <li><a>Portfolio</a></li>
          <li><RouterLink :to="{ name: 'Home' }">About</RouterLink></li>
        </ul>
      </div>
    </div>
    <div class="navbar-center">
      <RouterLink class="btn btn-ghost text-xl" :to="{ name: 'Home' }">
        NBA Stat Explorer
      </RouterLink>
    </div>
    <div class="navbar-end">
      <ThemeToggle></ThemeToggle>
    </div>
  </div>
</template>
