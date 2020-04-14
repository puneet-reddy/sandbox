<template>
  <div>
    <b-card no-body>
      <b-tabs pills card vertical class="v_tab">
        <b-tab title="Tab 1" active>
          <b-card-text>Tab contents 1</b-card-text>
        </b-tab>
        <b-tab title="Tab 2">
          <b-card-text>Tab contents 2</b-card-text>
        </b-tab>
        <b-tab title="Tab 3">
          <b-card-text>Tab contents 3</b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "VerticalTab"
};
</script>

<style>
.v_tab {
  height: 100vh;
  color: #333;
}
</style>