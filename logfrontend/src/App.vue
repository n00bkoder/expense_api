<template>
  <div id="app">
    <h1>Your Entries</h1>

    <form @submit.prevent="makeEntry">
      <div class="form-group row pl-3">
        <div class="input-group col-md-3">
          <input
            v-model="entry.item"
            type="text"
            class="form-control"
            id="item"
            placeholder="Item"
          />
        </div>

        <div class="input-group col-md-3">
          <input
            v-model="entry.cost"
            type="text"
            class="form-control"
            id="cost"
            placeholder="Cost"
          />
        </div>

        <div class="input-group col-md 3">
          <button type="submit" class="btn btn-outline-success">
            Make Entry
          </button>
        </div>
      </div>
    </form>

    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Item</th>
          <th scope="col">Cost</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="entry in entries" :key="entry.id">
          <td>{{ entry.item }}</td>
          <td>&#36;{{ entry.cost }}</td>
          <td>{{ entry.timestamp | dateParse('YYYY.MM.DD') }}</td>
          <td>
            <a href=""
              ><button type="button" class="btn btn-outline-primary">
                Edit
              </button></a
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {

      entry : {

        'item': '',
        'cost': '',
        
      },


      entries: [],
    };
  },

  async created() {
    var response = await fetch("http://localhost:8000/entries/");
    this.entries = await response.json();
  },

  methods: {
    async makeEntry () {
      var response = await fetch("http://localhost:8000/entries/",{
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.entry)
      });
      this.entries.push(await response.json());
    }
  },
};
</script>

<style>
#app {
}
</style>
