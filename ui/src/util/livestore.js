import { writable } from 'svelte/store'
import { io } from "socket.io-client"
import { apply_patch } from 'jsonpatch';

export const sock = io("localhost:8080")

export function emit(eventName, ...params) {
    return new Promise(function (resolve, reject) {
        sock.emit(eventName, ...params, (result) => {
            resolve(result)
        });
        setTimeout(reject, 1000);
    });
}

function createLiveStore() {
    const { subscribe, set, update } = writable({
        bugFlying: false,
        clock: "0",
        homePlayerNum: "0",
        awayPlayerNum: "0",
        textSliderTitle: "",
        textSliderSubtitle: "",
        caa_games: [],
        homeScore: "0",
        awayScore: "0"
    })

    return {
        subscribe,
        patch: (payload) => {
            update((s) => {
                return {...s, ...payload}
            })
        },
        update(payload) {
            this.patch(payload)
            sock.emit("store_update", payload)
        },
        toggle(key) {
            let payload = {}
            update((s) => {
                payload[key] = !s[key]
                return {...s, ...payload}
            })
            sock.emit("store_update", payload)
        },
        jsonPatch(op) {
            update((s) => {
                s = apply_patch(s, op)
                console.log("After patch", s)
                return s
            })
        }
    }
}

export const store = createLiveStore()
sock.on("store_init", store.patch)
sock.on("store_patch", store.patch)