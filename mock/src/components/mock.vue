<template>
  <div class="page">
      <ul>
          <li class="img"><img src="" alt=""></li>
          <li><h1>1</h1></li>
      </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {},
  mounted() {
    this.getlist();
  },
  methods: {
    getlist() {
      console.log(1)    
      // $.ajax({
      //   url: "../../data.json",
      //   contentType:'application/json',
      //   timeout:5000,
      //   type: "get",
      //   dataTyepe: "json",
      //   success:function(res){
      //     console.log(res)
      //   }              
      // });
      this.$http.get('/api/list').then(res=>{
         console.log(res.data)
       })
      }
    }
};
</script>

<style scoped>
li {
  list-style: none;
}
</style>
