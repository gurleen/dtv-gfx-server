<script>
// @ts-ignore
import {Container, Row, Col, Button, Card, Input} from 'svelte-chota'
import {store, emit} from '../util/livestore.js'
import AnimToggleButton from './components/AnimToggleButton.svelte';
import LiveKey from './components/LiveKey.svelte';
import {get} from 'svelte/store'

const WEIGHTS = [
	"125lb",
	"133lb",
	"141lb",
	"149lb",
	"157lb",
	"165lb",
	"174lb",
	"184lb",
	"197lb",
	"285lb"
]

const WIN_METHODS = [
	"DECISION",
	"MAJOR DECISION",
	"TECH FALL",
	"DQ",
	"FORFEIT",
	"MED. FORFEIT",
	"INJURY DEFAULT",
	"FALL"
]

let homeRoster = [{"name": "E. ANTHONY", "weight": "285lb"}, {"name": "E. BARCZAK", "weight": "285lb"}, {"name": "B. BONINO", "weight": "165lb"}, {"name": "D. D'AGOSTINO", "weight": "165lb"}, {"name": "A. DIABY", "weight": "174lb"}, {"name": "L. DIETRICH", "weight": "174lb"}, {"name": "D. FINDORA", "weight": "133lb"}, {"name": "G. GIAMPIETRO", "weight": "133lb"}, {"name": "J. HILDEBRANDT", "weight": "157lb"}, {"name": "J. JANDA", "weight": "157lb"}, {"name": "N. LAPINSKI", "weight": "125lb"}, {"name": "C. LEVEY", "weight": "125lb"}, {"name": "J. MARONEY", "weight": "184/197lb"}, {"name": "M. MARTINAK", "weight": "184/197lb"}, {"name": "A. MININNO", "weight": "149lb"}, {"name": "S. MORINA", "weight": "149lb"}, {"name": "L. NICHTER", "weight": "157/165lb"}, {"name": "T. NICHTER", "weight": "157/165lb"}, {"name": "M. O'MALLEY", "weight": "174lb"}, {"name": "S. O'MALLEY", "weight": "174lb"}, {"name": "G. ONORATO", "weight": "197lb"}, {"name": "R. ONORATO", "weight": "197lb"}, {"name": "D. PETRACCI", "weight": "149lb"}, {"name": "D. PLEASANT", "weight": "149lb"}, {"name": "D. PLEASANT", "weight": "165lb"}, {"name": "J. SORIANO", "weight": "165lb"}, {"name": "G. SPAIN", "weight": "184lb"}, {"name": "J. STILLINGS", "weight": "184lb"}, {"name": "J. TIMM", "weight": "285lb"}, {"name": "C. TROWBRIDGE", "weight": "285lb"}, {"name": "T. UPDEGRAFF", "weight": "157lb"}, {"name": "C. WALSH", "weight": "157lb"}, {"name": "K. WATERMAN", "weight": "125lb"}, {"name": "T. WILLIAMS", "weight": "125lb"}, {"name": "E. WILSON", "weight": "141lb"}]

let awayRoster = [{"name": "C. BAER", "weight": "165lb"}, {"name": "J. BAKER", "weight": "184lb"}, {"name": "C. BEVIS", "weight": "197lb"}, {"name": "C. BURNS", "weight": "285lb"}, {"name": "B. CASSELLA", "weight": "174lb"}, {"name": "C. DAY", "weight": "285lb"}, {"name": "C. DECKER", "weight": "157lb"}, {"name": "L. DEPREZ", "weight": "197lb"}, {"name": "S. DEPREZ", "weight": "174lb"}, {"name": "W. EBERT", "weight": "165lb"}, {"name": "D. GAMKRELIDZE", "weight": "165lb"}, {"name": "C. GANNONE", "weight": "141lb"}, {"name": "I. GARCIA", "weight": "133lb"}, {"name": "L. GUMBLE", "weight": "157lb"}, {"name": "T. KELLISON", "weight": "133lb"}, {"name": "N. LUCIER", "weight": "141lb"}, {"name": "T. MARTIN", "weight": "157lb"}, {"name": "F. NADEAU", "weight": "149lb"}, {"name": "J. NOLAN", "weight": "184lb"}, {"name": "M. ROES", "weight": "125lb"}, {"name": "M. SCHREIBER", "weight": "125lb"}, {"name": "A. SOBOTKER", "weight": "133lb"}, {"name": "C. TIBBITTS", "weight": "285lb"}, {"name": "M. ZARIF", "weight": "149lb"}]

function addScore(side, name, amount) {
	let suffix = amount == 1? "PT" : "PTS"
	store.update({scoringText: `${name.toUpperCase()}: ${amount} ${suffix}`})
	emit("play_anim", {anim: "Score Description"})
	let isHome = side == "home"
	let currentScore = isHome? get(store).homeScore : get(store).awayScore
	console.log(store)
	console.log(currentScore)
	let payload = {}
	payload[`${side}Score`] = parseInt(currentScore) + amount
	setTimeout(() => store.update(payload), 1000)
}
</script>

<main>
	<Container>
		<Row>
			<Col>
				<Card class="text-center">Wrestling Controller</Card>
			</Col>
		</Row>
		
		<Row>
			<Col size="5">
				<Card class="is-center">
					<Container>
						<Row>Clock: {$store.clock}</Row>
						<Row>
							<AnimToggleButton animName="Main Timeline">Toggle Bug</AnimToggleButton>
							<AnimToggleButton animName="Score Description">Score Description</AnimToggleButton>
							Home Score: <LiveKey key="homeScore"></LiveKey>
							Away Score: <LiveKey key="awayScore"></LiveKey>
						</Row>
						<Row>
							<select on:change={(e) => store.update({weight: e.target.value})}>
								{#each WEIGHTS as wt}
									<option value={wt}>{wt}</option>
								{/each}
							</select>
						</Row>
						<Row>
							<select on:change={(e) => store.update({period: e.target.value})}>
								<option value="1st">1st</option>
								<option value="2nd">2nd</option>
								<option value="3rd">3rd</option>
								<option value="OT">OT</option>
							</select>
						</Row>
						<Row>
							Home Wrestler:
							<select on:change={(e) => store.update({homeWrestler: e.target.value})}>
								{#each homeRoster as player}
									<option value={player.name}>{player.name} - {player.weight}</option>
								{/each}
							</select>
						</Row>
						<Row>
							Home Rank:
							<LiveKey key="homeRank"></LiveKey>
						</Row>
						<Row>
							Away Wrestler:
							<select on:change={(e) => store.update({awayWrestler: e.target.value})}>
								{#each awayRoster as player}
									<option value={player.name}>{player.name} - {player.weight}</option>
								{/each}
							</select>
						</Row>
						<Row>
							Away Rank:
							<LiveKey key="awayRank"></LiveKey>
						</Row>
						<Row>
							Home Win Reason:
							<select on:change={(e) => store.update({homeWinText: `WIN BY ${e.target.value}`})}>
								{#each WIN_METHODS as method}
									<option value={method}>{method}</option>
								{/each}
							</select>
							<AnimToggleButton animName="Home Win">HOME WIN</AnimToggleButton>
						</Row>
						<Row>
							Away Win Reason:
							<select on:change={(e) => store.update({awayWinText: `WIN BY ${e.target.value}`})}>
								{#each WIN_METHODS as method}
									<option value={method}>{method}</option>
								{/each}
							</select>
							<AnimToggleButton animName="Away Win">AWAY WIN</AnimToggleButton>
						</Row>
					</Container>
				</Card>
			</Col>
			
			<Col size="5">
				<Card>
					<Container>
						<Col>
							Home Scoring
							<Button on:click={() => addScore("home", "TAKEDOWN", 2)}>TAKEDOWN: +2</Button>
							<Button on:click={() => addScore("home", "STALLING", 1)}>STALLING: +1</Button>
							<Button on:click={() => addScore("home", "STALLING", 2)}>STALLING: +2</Button>
							<Button on:click={() => addScore("home", "REVERSAL", 2)}>REVERSAL: +2</Button>
							<Button on:click={() => addScore("home", "NEAR FALL", 2)}>NEAR FALL: +2</Button>
							<Button on:click={() => addScore("home", "NEAR FALL", 4)}>NEAR FALL: +4</Button>
						</Col>
						<Col>
							Away Scoring
							<Button on:click={() => addScore("away", "TAKEDOWN", 2)}>TAKEDOWN: +2</Button>
							<Button on:click={() => addScore("away", "STALLING", 1)}>STALLING: +1</Button>
							<Button on:click={() => addScore("away", "STALLING", 2)}>STALLING: +2</Button>
							<Button on:click={() => addScore("away", "REVERSAL", 2)}>REVERSAL: +2</Button>
							<Button on:click={() => addScore("away", "NEAR FALL", 2)}>NEAR FALL: +2</Button>
							<Button on:click={() => addScore("away", "NEAR FALL", 4)}>NEAR FALL: +4</Button>
						</Col>
					</Container>
				</Card>
			</Col>
		</Row>
	</Container>
</main>