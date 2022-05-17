const path = require('path');
const scriptFilename = path.resolve(__dirname, "../../../backend");
const pythonfile = path.join(scriptFilename,'desafio.py');
function listagrafo(req, res) {
    var spawn = require("child_process").spawn;
    var processo = spawn('python',[pythonfile,"listargrafo"] );
    
    processo.stdout.on('data', function(data) { 
        var resultado = data.toString();             
        res.send(resultado); 
    } ) 
    //processo.stdout.on('data', function(buffer) { 
        //const response = JSON.parse(buffer);
        //console.log(response);
    //} ) 
    //child.stdin.write(JSON.stringify({ args: [2, 3] }) + "\n");
}
exports.post = (req, res, next) => {
    res.status(201).send('Rota POST!');
 };
 
 exports.put = (req, res, next) => {
    let id = req.params.id;
    res.status(201).send(`Rota PUT com ID! --> ${id}`);
 };
  
 exports.delete = (req, res, next) => {
    let id = req.params.id;
    res.status(200).send(`Rota DELETE com ID! --> ${id}`);  
 };
  
 exports.get = (req, res, next) => {
    res.status(200).send('Rota GET!');
 };
  
 exports.listargrafo = (req, res) => {    
    listagrafo(req, res);
 };
 exports.getById = (req, res, next) => {
    let id = req.params.id;
    res.status(200).send(`Rota GET com ID! ${id}`);
 };