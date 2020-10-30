<script>
  import Navbar from './Navbar.svelte';
  import Player from './Player.svelte';
  import AddPlayer from './AddPlayer.svelte';
  
  let players = [
	  {
		  name: "Player 1",
		  points: 35
	  },
	  {
		  name: "Player 2",
		  points: 100
	  },
	  {
		  name: "N()()8",
		  points: 9000
	  }
  ];

  const addPlayer = (e) => {
	  const newPlayer = e.detail;
	  players = [...players, newPlayer];
  }
  const removePlayer = (e) => {
	  const removedPlayer = e.detail;
	  players = players.filter((each) => {return each.name !== removedPlayer});
  }
</script>


<Navbar/>
<div class="container">
	<AddPlayer on:addplayer={addPlayer}></AddPlayer>
	{#if players.length === 0}
		<p>No Players</p>
		{:else}
		{#each players as player}
			<Player name={player.name} points={player.points} on:removeplayer={removePlayer}></Player>
		{/each}
	{/if}
</div>
