<template>
  <div role="tablist">
    <b-card no-body class="mb-1" v-for="post in posts" v-bind:key="post.ID">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle="'accordion-'+post.ID" variant="dark">{{ post.title }}</b-button>
      </b-card-header>
      <b-collapse v-bind:id="'accordion-'+post.ID" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <div class="row">
            <a :href="post.link_to" class="col-sm-2 h-100" target="new">
              <b-card-img
                class="bg-secondary img-responsive"
                style="padding: 8px;"
                :src="post.logo_url"
              ></b-card-img>
            </a>
            <b-card-text class="text-left col-sm-10"><p style="text-indent: 1.5em;">{{ post.text[0] }}</p></b-card-text>
          </div>
          <div v-for="(para, index) in post.text.slice(1)" v-bind:key="index">
            <div class="row">
              <b-card-text class="text-left"><p style="text-indent: 1.5em;">{{ para }}</p></b-card-text>
            </div>
          </div>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
// TODO: Move the data below into an API call somewhere.
export default {
  name: 'Accordion',
  data () {
    return {
      posts: [
        {
          ID: '1',
          logo_url:
            'https://www.csscorp.com/wp-content/uploads/2017/03/logo-1-5.png',
          link_to: 'https://www.csscorp.com/',
          title: 'CSS Corp. (May 2017 - Present)',
          text: [
            `CSS Corp started out as a customer support and call center operation. 
            In recent years (2015 onwards) they have branched out into the digital
            and analytics space and by the time I joined them in 2017 they had 
            already laid the groundwork required for a division specializing in 
            effective AI/ML solution development.`,
            `Joining such a new department certainly had it's advantages, as I was 
            able to jump right into the exciting work of designing and implementing
            a chat-bot. The basic skeleton for this had already been ideated by
            my colleagues Prashath and Nishanth and when I joined they were in the
            midst of figuring out the techinical aspects of the implementation as
            well as the best architecture for the computer science side of things. 
            Given such an opportunity, I dived right into the world of NLP and 
            linguistics and four months and several thousand lines of code later, 
            we had a working bot.`,
            `Once a prototype of the bot was ready and the sales & marketing guys
            where in a position to use it for client demos there wasn't a whole lot
            to be done till we found a client who was interested enough in it and willing
            to sponsor further development. However, my ability to internalise complex
            systems and to make the best decisions when choosing between architectural
            paths had already been noticed. All this while, the department had
            focused solely on building a team good at machine learning. My work on the
            bot was a realization. Good software engineering and design could speed 
            things up! I was in demand!`,
            `For the next few months, I was hopping between projects and clients. 
            Never really part of one team, but simultaneously consulting with 
            nearly every team in the fledgling department. I worked on everything.
            From helping find C libraries to speed up OCR written in python, to
            setting up Spark clusters to fine tuning regex code to helping migrate
            from SQL to NoSQL, to model evaluation and hyper-parameter tuning; 
            EVERYTHING. It was an exciting time for sure, but all good things must
            eventually come to an end.`,
            `There was a new client on the engineering side of the business who 
            wanted a web portal developed and all their existing code as well as 
            their own expertise was in python based development. This was not a 
            skill that CSS Corp. had in ready supply. Most of their existing team
            was only trained in Java and PHP. Looking around the organization, they
            found that I had the requried expertise in Flask & Django and web 
            development in general. I was promptly conscripted for the job.`,
            'This unexpectedly turned out to be quite a challenge.'
          ]
        },
        {
          ID: '2',
          logo_url:
            'https://uploads-ssl.webflow.com/5cf9058299b2c44049b064b4/5cf907c58e7d8a6315dfeb86_3LOQ.png',
          link_to: 'https://www.3loq.com/',
          title: '3LOQ (Nov 2014 - Apr 2017)',
          text: [
            `
            Coming soon!.
            `,
            `
            Watch this space.
            `,
            `
            There will be an interesting story here soon\u2122.
            `
          ]
        },
        {
          ID: '3',
          logo_url:
            'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/New_Bloomberg_Logo.svg/330px-New_Bloomberg_Logo.svg.png',
          link_to: 'https://www.bloomberg.com/',
          title: 'Bloomberg LLP (Feb 2013 - Jul 2014)',
          text: [
            `
            Coming soon!.
            `,
            `
            Watch this space.
            `,
            `
            There will be an interesting story here soon\u2122.
            `
          ]
        }
      ]
    }
  }
}
</script>
