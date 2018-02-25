var http = require('http');

function onRequest (request, response) {
    console.log("Request Made " + request.url);
    response.writeHead(200, {"Context-Type": "text/plain"});
    response.write("Respond with data");
    response.end();

}

http.createServer(onRequest).listen(8888);
console.log("Server up........ \n");
