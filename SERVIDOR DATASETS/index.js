var express = require('express');
var cors = require('cors');
var dateFormat = require('dateformat');
var request = require('request');
var fs = require('fs');
const nodemailer = require('nodemailer');
var app = express();
const formidable = require('formidable')

app.use(cors({ origin: "*" }));

app.post('/file', (req, res) => {
    var now = new Date();
    new formidable.IncomingForm().parse(req, (err, fields, files) => {
        if (err) {
            console.error('Error', err)
            throw err
        }
        console.log('Fields', fields)
        console.log(files["file1"]["name"])
        var spawn = require("child_process").spawn;
        var process = spawn('python', ["./python.py", files["file1"]["name"]]);
        process.stdout.on('data', function (data) {
            console.log("salida");
            console.log(data.toString());
            if (data.toString().includes("HECHO")) {
                console.log("listo enviando datos");
                //res.sendFile(__dirname + "/uploads/" + files["file1"]["name"] + "report.html")


                nodemailer.createTestAccount((err, account) => {
                    var transporter = nodemailer.createTransport({
                        host: 'smtp.googlemail.com', // Gmail Host
                        port: 465, // Port
                        secure: true, // this is true as port is 465
                        auth: {
                            user: 'ecarlosandres@gmail.com', //Gmail username
                            pass: 'contraseña' // Gmail password
                        }
                    });

                    let mailOptions = {
                        from: '"resultadosdatasetnoreply" <resultados@noreply.net>',
                        to: fields["email"], // Recepient email address. Multiple emails can send separated by commas
                        subject: 'Resultados Data set: ' + files["file1"]["name"],
                        text: 'This is the email sent through Gmail SMTP Server.',
                        html: {path: __dirname + "/uploads/" + files["file1"]["name"] + "report.html"},
                        attachments: [{
                            filename: files["file1"]["name"] + "report.html",
                            path: __dirname + "/uploads/" + files["file1"]["name"] + "report.html"
                        }]
                    };

                    transporter.sendMail(mailOptions, (error, info) => {
                        if (error) {
                            return console.log(error);
                        }
                        console.log('Mensaje enviado: %s', info.messageId);
                    });
                });

            }
        })
        res.sendStatus(200)
    }).on('fileBegin', (name, file) => {

        file.path = __dirname + '/uploads/' + file.name;
    })
        .on('file', (name, file) => {
            //console.log('Uploaded file', name, file)
        })
});

app.listen(3000, function () {
    console.log('PUERTO 3000!');
});




app.post('/link', (req, res) => {

    new formidable.IncomingForm().parse(req, (err, fields, files) => {
        if (err) {
            console.error('Error', err)
            throw err
        }

        console.log(fields)
        var file = fs.createWriteStream("./uploads/" + fields["name"] + ".csv");
        request(fields["link"], function (error, response, body) {
            response.pipe(file);
            file.on('finish', function () {
                file.close();  // close() is async, call cb after close completes.
            });
        })

    });

});