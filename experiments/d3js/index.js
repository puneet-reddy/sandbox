
// index.js


// Selection
d3.select('h1').style('color', 'green')
.attr('class', 'heading')
.text('A heading or something');

const para1 = d3.select('body').append('p');
para1.text('first paragraph');


const svg = d3.select('svg').style('border', '1px solid red');
svg.attr('width', 500);
const width = parseFloat(svg.attr('width'));
const height = +svg.attr('height');


const eyeOffset = 100;
const eyeHeight = 70;

const g = svg.append('g')
    .attr('transform', `translate(0, 0)`);

const circle = g.append('circle')
    .attr('r', 200)
    .attr('cx', width/2)
    .attr('cy', height/2)
    .attr('fill', 'yellow')
    .attr('stroke', 'black');

const leftEye = g.append('circle')
    .attr('r', 30)
    .attr('cx', width / 2 - eyeOffset)
    .attr('cy', height / 2 - eyeHeight)
    .attr('fill', 'black');

const rightEye = g.append('circle')
    .attr('r', 30)
    .attr('cx', width / 2 + eyeOffset)
    .attr('cy', height / 2 - eyeHeight)
    .attr('fill', 'black');


const mouth = g.append('path')
    .attr('d', arc()({
        innerRadius: 80,
        outerRadius: 100,
        startAngle: 0,
        endAngle: Math.PI
    }));

// Data 