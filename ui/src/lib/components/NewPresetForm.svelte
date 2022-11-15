<script>
// @ts-ignore
import { Card, Row, Input, Col, Button } from 'svelte-chota'
import { createEventDispatcher } from 'svelte';
import { storePreset } from '../../util/render';

const dispatch = createEventDispatcher();

let formInput = {
    output: "",
    project: "",
    comp: "",
    start_frame: 0,
    end_frame: 0
}

async function submit() {
    await storePreset(formInput)
    dispatch('close')
}
</script>

<Card>
    <p class="text-center">New Preset</p>
    <p><Input placeholder="Output name" bind:value={formInput.output} /></p>
    <p><Input placeholder="Project filepath" bind:value={formInput.project} /></p>
    <p><Input placeholder="Comp name" bind:value={formInput.comp} /></p>
    <Row>
        <Col><Input number placeholder="Start frame" bind:value={formInput.start_frame} /> </Col>
        <Col><Input number placeholder="Start frame" bind:value={formInput.end_frame}   /> </Col>
    </Row>
    <p><Button on:click={submit}>Submit</Button></p>
</Card>
