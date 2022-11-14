const sock = io()

function emit(eventName) {
    return new Promise(function (resolve, reject) {
        sock.emit(eventName, (result) => {
            resolve(result)
        });
        setTimeout(reject, 1000);
    });
}

document.addEventListener('alpine:init', () => {
    Alpine.store('s', {
        data: {},
        update(payload) {
            this.data = { ...this.data, ...payload }
        }
    })

    Alpine.data('renderer', () => ({
        showingForm: false,
        presets: [],
        async getPresets() {
            this.presets = await emit("get_presets")
        },
        init() {
            this.getPresets()
        },
        async removePreset(id) {
            sock.emit("remove_preset", id, () => {
                this.getPresets()
            })
        }
    }))

    Alpine.data('presetRow', (presetItem) => ({
        preset: null,
        loading: false,
        init() {
            this.preset = presetItem
        },
        render() {
            this.loading = true
            sock.emit("run_render", this.preset, (resp) => {
                this.loading = false
            })
        }
    }))

    Alpine.data('renderForm', () => ({
        loading: false,
        showDoneMessage: false,
        form: {
            project: "/Users/gurleen/StartingFive.aep",
            comp: "BB Starting Lineups",
            start_frame: 0,
            end_frame: 543,
            output: "StartingLineups"
        },
        submit() {
            this.loading = true
            sock.emit("run_render", this.form, (_) => {
                this.loading = false
                this.showDoneMessage = true
                setTimeout(() => {
                    this.showDoneMessage = false
                }, 300)
            })
        },
        savePreset() {
            sock.emit("store_preset", this.form)
        },
    }))

    sock.on("store_init", (p) => Alpine.store("s").update(p))
    sock.on("store_patch", (p) => Alpine.store("s").update(p))
})

