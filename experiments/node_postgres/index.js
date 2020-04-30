const pgp = require('pg-promise')();

const cn = {
    host: 'localhost',
    port: 5432,
    database: 'postgres',
    user: 'postgres',
    password: 'postgres',
    max: 30
};

const db = pgp(cn);

db.any("select * from kb_dummy_data")
    .then(function(data){
        console.log("DATA: ", data)
    })
    .catch(function(error){
        console.log("ERROR: ", error)
    });