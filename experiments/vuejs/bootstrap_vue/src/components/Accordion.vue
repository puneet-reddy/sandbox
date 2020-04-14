<template>
  <div role="tablist">
    <b-card no-body class="mb-1" v-for="post in posts" v-bind:key="post.ID">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle="'accordion-'+post.ID" variant="dark">{{ post.title }}</b-button>
      </b-card-header>
      <b-collapse v-bind:id="'accordion-'+post.ID" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <div class="row">
            <a :href=post.link_to class="col-sm-2 h-100" target="new">
              <b-card-img
                class="bg-secondary img-responsive"
                style="padding: 8px;"
                :src="post.logo_url"
              ></b-card-img>
            </a>
            <b-card-text class="text-left col-sm-10">{{ post.text }}</b-card-text>
          </div>
          <div class="row">
            <p></p>
          </div>
          <div class="row">
            <b-card-text>Testing to see if a second text block acts like a paragraph</b-card-text>
          </div>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "Accordion",
  data() {
    return {
      posts: [
        {
          ID: "1",
          logo_url:
            "https://www.csscorp.com/wp-content/uploads/2017/03/logo-1-5.png",
          link_to: "https://www.csscorp.com/",
          title: "Css Corp.",
          text: `
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
          richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor
          brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon
          tempor, sunt aliqua put a bird on it squid single-origin coffee nulla
          assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore
          wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher
          vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic
          synth nesciunt you probably haven't heard of them accusamus labore VHS.
        `
        },
        {
          ID: "2",
          logo_url:
            "https://uploads-ssl.webflow.com/5cf9058299b2c44049b064b4/5cf907c58e7d8a6315dfeb86_3LOQ.png",
          link_to: "https://www.3loq.com/",
          title: "3LOQ",
          text: `
          Testing to see if I can get Vue accordions to work with for based list rendering.
        `
        },
        {
          ID: "3",
          logo_url:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/New_Bloomberg_Logo.svg/330px-New_Bloomberg_Logo.svg.png",
          link_to: "https://www.bloomberg.com/",
          title: "Bloomberg LLP",
          text: `
          List out what I did at bloomberg with some examples (where legal)
          `
        }
      ]
    };
  }
};
</script>
