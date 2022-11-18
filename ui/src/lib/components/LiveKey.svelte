<script>
    export let key;
    // @ts-ignore
    import {Input} from 'svelte-chota'
    import {store} from '../../util/livestore.js'
</script>

<main>
    <Input bind:value={$store[key]} on:change={(e) => store.update({[key]: e.target.value})} />
</main>