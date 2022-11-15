<script>
import {store} from '../util/livestore.js'
import { JSONEditor } from 'svelte-jsoneditor'

let storeContents = {json: {}}
store.subscribe(val => storeContents = {json: val})

function handleChange(updated, previous, {errors, patchResult}) {
    if(patchResult != null) {
        console.log(patchResult)
        store.jsonPatch(patchResult.redo)
    }
}
</script>

<main>
    <JSONEditor content={storeContents} onChange={handleChange}></JSONEditor>
</main>