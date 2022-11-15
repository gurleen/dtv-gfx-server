<script>
  import { refreshIcon } from "../util/icons";
  // @ts-ignore
  import { Container, Icon, Button, Modal, Card, Row } from "svelte-chota";
  import { getPresets } from "../util/nexrender";
  import NewNexrenderPresetForm from "./components/NewNexrenderPresetForm.svelte";

  let presets = []
  let newPresetWindowOpen = false

  async function refresh() {
    presets = await getPresets()
    console.log(presets)
  }

  async function save(preset) {
    console.log(preset)
    newPresetWindowOpen = false
  }

</script>

<main>
    <Container>
        <Button on:click={refresh}><Icon src={refreshIcon} /> Refresh</Button>
        <Button on:click={_ => newPresetWindowOpen = !newPresetWindowOpen}>New Preset</Button>
        <table class="striped">

        </table>
    </Container>

    <Modal bind:open={newPresetWindowOpen}>
        <NewNexrenderPresetForm on:save={save}></NewNexrenderPresetForm>
    </Modal>
</main>