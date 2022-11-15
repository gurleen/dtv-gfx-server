<script>
    export let liveKey;
    export let onText;
    export let offText;
    // @ts-ignore
    import {Button} from 'svelte-chota'
    import {store} from '../../util/livestore'

    $: value = $store[liveKey] || false
    $: buttonText = value? offText : onText
</script>

<main>
    <Button success={!value} error={value} on:click={store.toggle(liveKey)}>{buttonText}</Button>
</main>