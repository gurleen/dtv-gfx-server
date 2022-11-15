<script>
  import { onMount } from "svelte";
  import { getPresets, removePreset } from "../util/render";
  // @ts-ignore
  import { Container, Icon, Button, Modal, Card, Row } from "svelte-chota";
  import PresetRow from "./components/PresetRow.svelte";
  import { refreshIcon } from "../util/icons";
  import NewPresetForm from "./components/NewPresetForm.svelte";

  let presets = [];

  async function refresh() {
    presets = await getPresets();
  }

  onMount(async () => {
    await refresh();
  });

  let isModalOpen = false;

  let selectedPresetId = null;
  let isRemoveModalOpen = false;
  async function removeModal(id) {
    selectedPresetId = id;
    isRemoveModalOpen = true;
  }

  async function modalClose() {
    isRemoveModalOpen = false;
    await removePreset(selectedPresetId);
    await refresh();
  }
</script>

<main>
  <Container>
    <Button on:click={refresh}><Icon src={refreshIcon} /> Refresh</Button>
    <Button on:click={(_) => (isModalOpen = true)}>New Preset</Button>
    <table class="striped">
      <thead>
        <tr>
          <th />
          <th>Name</th>
          <th>Project file</th>
          <th>Comp name</th>
          <th>Frames</th>
          <th />
        </tr>
      </thead>
      <tbody>
        {#each presets as preset}
          <PresetRow on:remove={(_) => removeModal(preset.id)} {preset} />
        {/each}
      </tbody>
    </table>
  </Container>
  <Modal bind:open={isModalOpen}>
    <NewPresetForm on:close={modalClose} />
  </Modal>
  <Modal bind:open={isRemoveModalOpen}>
    <Card>
      <h4>Are you sure you want to delete this preset?</h4>
      <Row class="is-center">
        <Button clear on:click={(_) => (isRemoveModalOpen = false)}>
            Cancel
        </Button>
        <Button error on:click={modalClose}>Delete</Button>
      </Row>
    </Card>
  </Modal>
</main>
