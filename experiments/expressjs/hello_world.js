const express = require('express');
const path = require('path');
const members = require('./Members');
const exphbs = require('express-handlebars');

// Init express
const app = express();

// Simple middleware
// const logger = require('./middleware/logger')
// app.use(logger);

// Adding the handlebars middleware
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// Create your endpoints (route handlers)
// app.get('/', (req, res) => {
//     res.sendFile(path.join(__dirname, 'public', 'index.html'));
//     // res.send('<h1>Hello World from Express!</h1>');
// });

// Setting a static folder
// app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.render('index', {
        title: 'Express JS test',
        members: members
    });
});

// Body parser middleware
app.use(express.json());
app.use(express.urlencoded({extended: false}));

// Members API
app.use('/api/members', require('./routes/api/members'));

const PORT = process.env.PORT || 5000;

// Listen on a port
app.listen(PORT, () => console.log(`Running simple express server on port ${PORT}...`));