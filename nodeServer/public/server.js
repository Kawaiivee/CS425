var connect = require('connect');
var http=require('http');
var fs=require('fs');
var app = connect() //module.exports = express.createServer();  


//404 response
function profile(request,response){
    console.log("user request profile");
}
function forum(request,response){
    console.log("user request profile");
}

app.use('/profile',profile);
app.use('/forum',forum)

http.createServer(app).listen(8888);
console.log("Server is now running...");