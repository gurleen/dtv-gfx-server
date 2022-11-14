import {emit} from './livestore'

export async function getPresets() {
    return await emit("get_presets")
}

export async function runRender(preset) {
    await emit("run_render", preset)
}

export async function storePreset(preset) {
    await emit("store_preset", preset)
}

export async function removePreset(presetId) {
    await emit("remove_preset", presetId)
}