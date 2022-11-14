import {emit} from './livestore'

export async function getPresets() {
    return await emit("nexrender_get_all_presets")
}

export async function storePreset(preset) {
    return await emit("nexrender_store_preset", preset)
}