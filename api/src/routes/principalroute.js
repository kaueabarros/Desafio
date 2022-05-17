const PrincipalController = require('../controllers/controller');
module.exports = (app) => {
   app.get('/listargrafo', PrincipalController.listargrafo);
   app.get('/listaramigos/:id', PrincipalController.listaramigos);
   app.get('/listarnivel2/:id', PrincipalController.listarnivel2);
   app.get('/cadastrarpessoa', PrincipalController.cadastrarpessoa);
}