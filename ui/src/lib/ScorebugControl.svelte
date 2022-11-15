<script>
// @ts-ignore
import {Container, Row, Col, Button, Card, Input} from 'svelte-chota'
import ToggleButton from './components/ToggleButton.svelte'
import {store} from '../util/livestore.js'
  import AnimToggleButton from './components/AnimToggleButton.svelte';
</script>

<main>
    <Container>
        <Row>
            <Col><Card class="text-center">Scoreboard Control</Card></Col>
        </Row>
        <Row>
            <Col size="5">
                <Card class="is-center">
                    <ToggleButton liveKey="bugFlying" onText="SCOREBUG ON" offText="SCOREBUG OFF"></ToggleButton>
                </Card>
            </Col>
            <Col>
                <Card class="is-center">
                    <Row>Clock: {$store.clock}</Row>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col size="5">
                <Card class="is-center">
                    <Container>
                        <Row>
                            Home LTH: {$store.homePlayerNum}
                        </Row>
                        <Row>
                            <Input number on:change={(e) => store.update({homePlayerNum: String(e.target.value)})} />
                            <AnimToggleButton animName="Home Player Stats">PLAY</AnimToggleButton>
                        </Row>
                    </Container>
                </Card>
            </Col>
        </Row>
    </Container>
</main>