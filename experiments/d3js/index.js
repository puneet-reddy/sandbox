
// index.js

// Selection
d3.select('h1').style('color', 'green')
.attr('class', 'heading')
.text('A heading or something');

d3.select('body').append('p').text('first para');

d3.selectAll('p').sytle('color', 'blue');


// Data 