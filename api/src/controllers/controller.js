const path = require('path');
const scriptFilename = path.resolve(__dirname, "../../../backend");
const pythonfile = path.join(scriptFilename,'desafio.py');
function listagrafo(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile,"listargrafo"] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on('data', function(data) { 
        var resultado = data.toString();             
        res.send(resultado); 
    } ) 
}
function listaamigos(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile,"listaramigos",req.params.id] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on('data', function(data) { 
        var resultado = data.toString();             
        res.send(resultado); 
    } ) 
}
function listanivel2(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile,"listarnivel2",req.params.id] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on('data', function(data) { 
        var resultado = data.toString();             
        res.send(resultado); 
    } ) 
}
function cadastropessoa(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile,"cadastropessoa",req.query.pessoa,req.query.amigo] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on('data', function(data) { 
        var resultado = data.toString();             
        res.send(resultado); 
    } ) 
}
 exports.listargrafo = (req, res) => {    
    listagrafo(req, res);
 };
 exports.listaramigos = (req, res, next) => {
     listaamigos(req, res)
 };
 exports.listarnivel2 = (req, res, next) => {
    listanivel2(req, res)
};
exports.cadastrarpessoa = (req, res, next) => {
    cadastropessoa(req, res)
};