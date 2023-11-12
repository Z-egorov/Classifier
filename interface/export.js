const {download} = require('electron-dl');
const {BrowserWindow} = require('electron');

function export_data() {
    var options = { scriptPath : path.join(__dirname, '../engine/') }
    let shell = new PythonShell('export.py', options)

    shell.on('message', function(message) {
        document.getElementById("anwser").textContent = '';
        swal({
            title: "Success!",
            text: "Data successfully exported ",
            buttons: false,
            timer: 1500,
          });

          document.getElementById('download').click();

    })

    shell.end(function (err) {
        if (err){
            document.getElementById("anwser").textContent = "ERROR";
            throw err;
        };
      });

}