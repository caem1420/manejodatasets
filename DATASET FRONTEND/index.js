var opcioncsv = (valor) => {
  switch (valor) {
    case "file":
      document.getElementById("cuerpo").innerHTML = "";
      document.getElementById("cuerpo").innerHTML = " <br><form id='archivoform' class='form-group'enctype='multipart/form-data' method='post' name='archivo'>" +
        "<label>Ingrese el archivo</label>" +
        "<input name='file1' class='form-control' type='file' id='file' required>" +
        "<label>Nombre Dataset</label>" +
        "<input class='form-control' id='nombre' name='nombre' required>"+
        "<label>email</label>"+
        "<input type='email' class='form-control' id='email' name='email' required>"

      document.getElementById("cuerpo").innerHTML += "<input type='submit' onclick='envio(" + valor + ")' class='btn btn-primary btn-block'> </form>"
      console.log(valor);
      break;

    case "link":
      document.getElementById("cuerpo").innerHTML = "";
      document.getElementById("cuerpo").innerHTML = " <br><form id='linkform' class='form-group'enctype='multipart/form-data' method='post' name='link'>" +
        "<label>Ingrese el Link</label>" +
        "<input class='form-control' id='link' type='url' name='link' required>" +
        "<label>Nombre Dataset</label>" +
        "<input class='form-control' id='nombre' name='name' required>"

      document.getElementById("cuerpo").innerHTML += "<input type='submit' onclick='enviolink(" + valor + ")' class='btn btn-primary btn-block'> </form>"
      console.log(valor);
      break;
    default:
      document.getElementById("cuerpo").innerHTML = "";
      break;
  }
}

var form = document.forms.namedItem(document.getElementById("archivoform"));
var envio = (loq) => {
  console.log(loq)
  console.log("datos en archivo")
  oData = new FormData(document.getElementById("archivoform"));


  var oReq = new XMLHttpRequest();
  oReq.open("POST", "http://localhost:3000/file", true);
  oReq.onload = function (oEvent) {
    if (oReq.status == 200) {
      console.log("Uploaded!");
      console.log(oReq.response);
    } else {
      console.log("Error " + oReq.status + " occurred when trying to upload your file.<br \/>");
    }
  };

  oReq.send(oData);
  console.log("enviar")
}

var enviolink = (valor)=>{
  console.log("datos en link")
  oData = new FormData(document.getElementById("linkform"));


  var oReq = new XMLHttpRequest();
  oReq.open("POST", "http://localhost:3000/link", true);
  oReq.onload = function (oEvent) {
    if (oReq.status == 200) {
      console.log("Uploaded!");
    } else {
      console.log("Error " + oReq.status + " occurred when trying to upload your file.<br \/>");
    }
  };

  oReq.send(oData);
  console.log("enviar")
}