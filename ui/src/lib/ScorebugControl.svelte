<script>
// @ts-ignore
import {Container, Row, Col, Button, Card, Input} from 'svelte-chota'
import ToggleButton from './components/ToggleButton.svelte'
import {store, emit} from '../util/livestore.js'
  import AnimToggleButton from './components/AnimToggleButton.svelte';
  import LiveKey from './components/LiveKey.svelte';

function updateHome(e) {
    store.update({homePlayerNum: String(e.target.value)})
    emit("run_home_update")
}

function updateAway(e) {
    store.update({awayPlayerNum: String(e.target.value)})
    emit("run_away_update")
}

let compStatValue = ""
function updateComp() {
    store.update({compStat: compStatValue})
    emit("run_comp_update")
}

let textSliderPresets = [
    {title: "COMMENTATORS", subtitle: "ROB BROOKS & MIKE TUBEROSA"},
    {title: "OFFICIALS", subtitle: "OFFICIAL 1, OFFICIAL 2, OFFICIAL 3"},
    {title: "VENUE", subtitle: "DASKALAKIS ATHLETIC CENTER, PHILADELPHIA"}
]

let currentPreset = {title: "", subtitle: ""}

function setPreset() {
    store.update({textSliderTitle: currentPreset.title, textSliderSubtitle: currentPreset.subtitle})
}
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
                            Select sport:
                            <select on:change={(e) => store.update({sport: e.target.value})}>
                                <option value="mbb">Men's Basketball</option>
                                <option value="wbb">Women's Basketball</option>
                            </select>
                        </Row>
                        <Row>
                            Home LTH: {$store.homePlayerNum}
                        </Row>
                        <Row>
                            <Input number on:change={updateHome} />
                            <AnimToggleButton animName="Home Player Stats">PLAY</AnimToggleButton>
                        </Row>
                        <Row>
                            Away LTH: {$store.awayPlayerNum}
                        </Row>
                        <Row>
                            <Input number on:change={updateAway} />
                            <AnimToggleButton animName="Away Player Stats">PLAY</AnimToggleButton>
                        </Row>
                        <Row>
                            Home Trend:
                            <select on:change={(e) => store.update({homeTrend: e.target.value})}>
                                <option value="homeLastScore">Scoring Drought</option>
                                <option value="homeLastFG">FG Drought</option>
                            </select>
                            <AnimToggleButton animName="Home Trend">PLAY</AnimToggleButton>
                        </Row>
                        <Row>
                            Away Trend:
                            <select on:change={(e) => store.update({awayTrend: e.target.value})}>
                                <option value="awayLastScore">Scoring Drought</option>
                                <option value="awayLastFG">FG Drought</option>
                            </select>
                            <AnimToggleButton animName="Away Trend">PLAY</AnimToggleButton>
                        </Row>
                    </Container>
                </Card>
            </Col>
            <Col size="5">
                <Card class="is-center">
                    <Container>
                        <Row>
                            Comparison Stat
                            <select bind:value={compStatValue} on:change={updateComp}>
                                <option value="assists">Assists</option>
                                <option value="bench_points">Bench Points</option>
                                <option value="biggest_scoring_run">Biggest Scoring Run</option>
                                <option value="blocks">Blocks</option>
                                <option value="field_goals_fraction">Field Goals</option>
                                <option value="field_goal_percentage">FG%</option>
                                <option value="fouls_personal">Personal Fouls</option>
                                <option value="fouls_team">Team Fouls</option>
                                <option value="free_throws_percentage">FT%</option>
                                <option value="free_throws_fraction">Free Throws</option>
                                <option value="offensive_rebounds">Offensive Rebounds</option>
                                <option value="points_fast_break">Fast Break Points</option>
                                <option disabled value="points_in_the_paint_made">Points in the Paint</option>
                                <option value="rebounds_total">Rebounds</option>
                                <option value="steals">Steals</option>
                                <option value="three_pointers_percentage">3FG%</option>
                                <option value="three_pointers_fraction">Three Pointers</option>
                                <option value="time_leading">Time Leading</option>
                                <option value="turnovers">Turnovers</option>
                            </select>
                            <Button on:click={updateComp}>UPDATE</Button>
                            <AnimToggleButton animName="Comp Stat">PLAY</AnimToggleButton>
                        </Row>
                    </Container>
                </Card>
                <Card class="is-center" style="margin-top: 5px;">
                    <Container>
                        <Row>
                            Text Slider
                        </Row>
                        <Row>
                            <select bind:value={currentPreset}>
                                {#each textSliderPresets as preset}
                                    <option value={preset}>{preset.title} - {preset.subtitle}</option>
                                {/each}
                            </select>
                            <Button on:click={setPreset}>Set Preset</Button>
                        </Row>
                        <Row>
                            <LiveKey key="textSliderTitle" />
                        </Row>
                        <Row>
                            <LiveKey key="textSliderSubtitle" />
                        </Row>
                        <Row>
                            <AnimToggleButton animName="Text Slider Content Change">Update Text</AnimToggleButton>
                            <AnimToggleButton animName="Text Slider">PLAY</AnimToggleButton>
                        </Row>
                    </Container>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col size="5">
                <Card class="is-center">
                    <Container>
                        <Row>
                            <h4>CAA Out of Town Scoreboard</h4>
                        </Row>
                        <Row>
                            <AnimToggleButton animName="Out of Town Score">PLAY</AnimToggleButton>
                        </Row>
                        <Row>
                            <select on:change={(e) => store.update({ootGame: $store.caa_games[e.target.value]})}>
                                {#each $store.caa_games as game, index}
                                    <option value={index}>{game.awayName} @ {game.homeName}</option>
                                {/each}
                            </select>
                            <AnimToggleButton animName="Out of Town Score Change">UPDATE</AnimToggleButton>
                        </Row>
                    </Container>
                </Card>
            </Col>
        </Row>
    </Container>
</main>