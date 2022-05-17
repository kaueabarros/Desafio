const path = require('path');
const scriptFilename = path.resolve(__dirname, "../../../backend");
const pythonfile = path.join(scriptFilename,'desafio.py');
function listagrafo(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile] );
    
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on("data", function (buffer) {
        var resultado = buffer;
        res.send(resultado);
    });
    
    processo.stdin.write(JSON.stringify({ args: ["listargrafo"] }) + "\n");
}
function listaamigos(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    
    processo.stdout.on("data", function (buffer) {
        var resultado = buffer;
        res.send(resultado);
    });
    
    processo.stdin.write(JSON.stringify({ args: ["listaramigos",req.params.id] }) + "\n");
}
function listanivel2(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on("data", function (buffer) {
        var resultado = buffer;
        res.send(resultado);
    });
    
    processo.stdin.write(JSON.stringify({ args: ["listarnivel2",req.params.id] }) + "\n");
}
function cadastropessoa(req, res) {
    var spawn = require("child_process").spawn;    
    var processo = spawn('python',[pythonfile] );
    processo.on("exit", (code) => console.log("exitCode:", code));
    processo.stdout.on("data", function (buffer) {
        var resultado = buffer;
        res.send(resultado);
    });
    
    processo.stdin.write(JSON.stringify({ args: ["cadastropessoa",req.query.pessoa,req.query.amigo] }) + "\n");}
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