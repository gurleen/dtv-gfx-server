<script>
// @ts-ignore
import {Container, Nav, Row, Col, Button, Modal, Card, Input} from 'svelte-chota'
import logo from './assets/DrexelDragonsAlt.png'
import AfterEffects from './lib/AfterEffects.svelte';
import Nexrender from './lib/Nexrender.svelte';
import Plugins from './lib/Plugins.svelte';
import ScorebugControl from './lib/ScorebugControl.svelte';
import Stats from './lib/Stats.svelte';
import Wrestling from './lib/Wrestling.svelte';


const TABS = {
    "Scorebug": ScorebugControl,
    "After Effects": Nexrender,
    "Plugins": Plugins,
    "Stats": Stats,
    "Wrestling": Wrestling
}

let selectedTab = "Scorebug"
$: contentComponent = TABS[selectedTab]

function msToTime(s) {
  let sign = s > 0? "-" : "+"
  var ms = s % 1000;
  s = (s - ms) / 1000;
  var secs = s % 60;
  s = (s - secs) / 60;
  var mins = s % 60;
  var hrs = (s - mins) / 60;

  return "T" + sign + hrs + ':' + mins + ':' + secs;
}

let showTimeDelta = ""
let timeUntilModalShowing = false
let showTime = null
$: timeUntil = showTime === null? "No Show" : showTimeDelta

let clock = ""
function time() {
  var d = new Date();
  var s = d.getSeconds();
  var m = d.getMinutes();
  var h = d.getHours();
  clock = 
    ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
  if(showTime != null) {
    let sd = new Date(showTime)
    // @ts-ignore
    let td = sd - d
    showTimeDelta = msToTime(td)
  }
}
setInterval(time, 250);
</script>

<main>
  <Nav>
    <!-- svelte-ignore a11y-missing-content -->
    <a href="#" slot="left" class="bg-light" on:click={_ => timeUntilModalShowing = true}>{timeUntil}</a>
    <a href="/" slot="center"><img alt="Drexel Logo" src={logo} /></a>
    <!-- svelte-ignore a11y-invalid-attribute -->
    <a href="#" slot="right" class="bg-light">{clock}</a>
  </Nav>
  <Container>
    <Row>
      <Col size="2">
        {#each Object.keys(TABS) as tab}
          <Row
            ><Button
              primary={selectedTab === tab}
              on:click={() => (selectedTab = tab)}>{tab}</Button
            ></Row
          >
        {/each}
      </Col>
      <Col>
        <svelte:component this={contentComponent} />
      </Col>
    </Row>
  </Container>
  <Modal bind:open={timeUntilModalShowing}>
    <Card>
      <h3>Set Show Time</h3>
      <Input bind:value={showTime} type="datetime-local" />
      <Button on:click={_ => timeUntilModalShowing = false}>Set</Button>
    </Card>
  </Modal>
</main>
