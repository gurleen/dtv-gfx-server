<script>
  // @ts-ignore
  import { Card, Row, Input, Checkbox, Button } from "svelte-chota";
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let preset = {
    template: {
      src: "",
      composition: "",
    },
    assets: [],
  };

  function addAdjust(type) {
    if (type == "text") {
      preset.assets.push({
        __TYPE__: "text",
        __IS_LIVE_KEY__: false,
        type: "data",
        layerName: "",
        property: "Source Text",
        value: "",
      });
    } else if (type == "color") {
      preset.assets.push({
        __TYPE__: "color",
        __IS_LIVE_KEY__: false,
        type: "data",
        layerName: "",
        property: "Color",
        color: [0, 0, 0],
      });
    } else if (type == "image") {
      preset.assets.push({
        __TYPE__: "image",
        __IS_LIVE_KEY__: false,
        type: "image",
        src: "",
        layerName: "",
        extension: "",
      });
    }
    preset.assets = preset.assets;
  }

  function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? [
          parseInt(result[1], 16),
          parseInt(result[2], 16),
          parseInt(result[3], 16),
        ]
      : null;
  }

  function removeAdjust(idx) {
    preset.assets.splice(idx, 1)
    preset = preset
  }

  function save() {
    dispatch("save", preset)
  }
</script>

<Card>
  <p class="text-center">New Preset</p>
  <p><Input placeholder="Project Path" bind:value={preset.template.src} /></p>
  <p>
    <Input
      placeholder="Composition Name"
      bind:value={preset.template.composition}
    />
  </p>
  <br />

  <p class="text-center">Adjustments</p>
  <Row class="is-center">
    <Button on:click={(_) => addAdjust("text")}>+ Text</Button>
    <Button on:click={(_) => addAdjust("color")}>+ Color</Button>
    <Button on:click={(_) => addAdjust("image")}>+ Image</Button>
  </Row>

  <br />

  <div style="max-height: 400px; overflow: scroll;">
    {#each preset.assets as adjust, idx}
      {#if adjust.__TYPE__ == "text"}
        <Card>
          <Row>
            <p>Text</p>
          </Row>
          <p>
            <Input placeholder="Layer Name" bind:value={adjust.layerName} />
          </p>
          <p><Input placeholder="Value" bind:value={adjust.value} /></p>
          <p>
            <input type="checkbox" checked={adjust.__IS_LIVE_KEY__} /> Use live key
          </p>
          <Button on:click={_ => removeAdjust(idx)} error>Delete</Button>
        </Card>
      {:else if adjust.__TYPE__ == "color"}
        <Card>
          <Row>
            <p>Color</p>
          </Row>
          <p>
            <Input placeholder="Layer Name" bind:value={adjust.layerName} />
          </p>
          <p>
            <input type="checkbox" bind:checked={adjust.__IS_LIVE_KEY__} /> Use live
            key
          </p>
          {#if adjust.__IS_LIVE_KEY__}
            <p><Input placeholder="Value" bind:value={adjust.value} /></p>
          {:else}
            <p>
              <Input color on:input={(c) => (adjust.value = hexToRgb(c))} />
            </p>
          {/if}
          <Button on:click={_ => removeAdjust(idx)} error>Delete</Button>
        </Card>
      {:else if adjust.__TYPE__ == "image"}
        <Card>
          <Row>
            <p>Image</p>
          </Row>
          <p>
            <Input placeholder="Layer Name" bind:value={adjust.layerName} />
          </p>
          <p><Input placeholder="Value" bind:value={adjust.value} /></p>
          <p>
            <input type="checkbox" checked={adjust.__IS_LIVE_KEY__} /> Use live key
          </p>
          <Button on:click={_ => removeAdjust(idx)} error>Delete</Button>
        </Card>
      {/if}
    {/each}
  </div>
  <Button on:click={save}>Save</Button>
</Card>
