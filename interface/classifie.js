let {PythonShell} = require('python-shell')
var path = require('path')

function get_theme() {
    
    var link = document.getElementById("link").value

    var options = {
        scriptPath : path.join(__dirname, '../engine/'),
        args : [link]
    }

    let shell = new PythonShell('app.py', options)

    shell.on('message', function(message) {
        document.getElementById("anwser").textContent = message;
    })
    document.getElementById("link").value = "";

    shell.end(function (err) {
        if (err){
            document.getElementById("anwser").textContent = "ERROR";
            throw err;
        };
        console.log('finished');
      });
}   
