<script>
import { cancelTask, getTasks } from '../util/tasks';
import {onMount} from 'svelte'
// @ts-ignore
import {Button, Icon} from 'svelte-chota'
  import { playIcon, stopIcon } from '../util/icons';

let tasks = []

onMount(async () => {
    tasks = await getTasks()
    console.log(tasks)
})
</script>

<main>
    <table class="striped">
        <thead>
            <tr>
                <th>Plugin Name</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {#each tasks as task}
                <tr>
                    <td>{task.name}</td>
                    <td>{task.running? 'Running' : 'Not Running'}</td>
                    <td>
                        {#if task.running}
                            <Button on:click={_ => cancelTask(task.name)}><Icon src={stopIcon}></Icon></Button>
                        {:else}
                            <Button><Icon src={playIcon}></Icon></Button>
                        {/if}
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
</main>