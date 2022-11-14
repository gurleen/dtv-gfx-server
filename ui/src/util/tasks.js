import {emit} from './livestore'

export async function getTasks() {
    return await emit('task_status')
}

export async function cancelTask(taskName) {
    return await emit('cancel_task', taskName)
}