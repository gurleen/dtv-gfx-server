<script>
    export let animName
    // @ts-ignore
    import {Button} from 'svelte-chota'
    import {emit} from '../../util/livestore.js'

    function toggle() {
        emit("play_anim", {anim: animName})
    }
</script>

<main>
    <Button on:click={toggle}>
        <slot></slot>
    </Button>
</main>