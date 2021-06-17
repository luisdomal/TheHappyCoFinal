const router = require('express').Router();
const {
  crearProducto,
  obtenerProductos,
  modificarProducto,
  eliminarProducto
} = require('../controllers/productos')
var auth = require('./auth');

router.get('/', auth.opcional,obtenerProductos)
router.get('/:id', auth.opcional, obtenerProductos)// nuevo endpoint con todos los detalles de producto
router.post('/', auth.opcional, crearProducto)
router.put('/:id',auth.opcional, modificarProducto)
router.delete('/:id',auth.opcional, eliminarProducto)

module.exports = router;