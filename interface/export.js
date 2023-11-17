const {download} = require('electron-dl');
const {BrowserWindow} = require('electron');

function export_data() {

        swal({
            title: "Success!",
            text: "Data successfully exported ",
            buttons: false,
            timer: 1500,
          });

        document.getElementById("download").click();
}