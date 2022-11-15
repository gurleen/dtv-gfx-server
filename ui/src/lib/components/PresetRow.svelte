<script>
  export let preset;
  // @ts-ignore
  import { Button, Icon, Row, Col } from "svelte-chota";
  import { store, sock } from "../../util/livestore";
  import { fade } from "svelte/transition";
  import { trashIcon, downArrowIcon } from "../../util/icons.js";
  import { removePreset } from "../../util/render";
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let open = false;
  let loading = false;
  let showDone = false;

  function renderClick() {
    loading = true;
    sock.emit("run_render", preset, () => {
      loading = false;
      showDone = true;
      setTimeout(() => (showDone = false), 5000);
    });
  }

  async function removeThisPreset() {
    await removePreset(preset.id)
    dispatch("remove")
  }
</script>

<tr>
  <td
    ><Button clear on:click={() => (open = !open)}
      ><Icon src={downArrowIcon} /></Button
    ></td
  >
  <td>{preset.output}</td>
  <td>{preset.project}</td>
  <td>{preset.comp}</td>
  <td>{preset.end_frame - preset.start_frame}</td>
  <td
    ><Button on:click={_ => dispatch("remove")}><Icon src={trashIcon} /></Button
    ></td
  >
</tr>
{#if open}
  <tr>
    <td colspan="6">
      <Row>
        <Col size="12"
          ><progress
            style="width: 100%;"
            value={$store[`render_job_${preset.id}_progress`] || 0}
          /></Col
        >
      </Row>
      <Row>
        <Col>
          <Button {loading} on:click={renderClick}>Render</Button>
        </Col>
        {#if showDone}
          <Col><p in:fade out:fade>Render complete!</p></Col>
        {/if}
      </Row>
    </td>
  </tr>
{/if}
