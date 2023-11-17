let {PythonShell} = require('python-shell')
var path = require('path')

function get_theme() {

    document.getElementById("anwser").textContent = "Calculating... May take a sec..";
    
    var options = {
        scriptPath : path.join(__dirname, '../engine/'),
    }

    let shell = new PythonShell('app.py', options)

    shell.on('message', function(message) {
        document.getElementById("anwser").textContent = message;
    })

    shell.end(function (err) {
        if (err){
            document.getElementById("anwser").textContent = "ERROR";
            throw err;
        };
        console.log('finished');
      });
}   
