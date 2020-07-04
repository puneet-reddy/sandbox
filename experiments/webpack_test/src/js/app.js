// alert(require('./people.js'));

require('../css/style.css');

import people from './people.js';
import $, { each } from 'jquery';



each(people, function(key, value){
    $('body').append('<h1>'+value.name+'</h1>');
})

console.log(people[0].name);