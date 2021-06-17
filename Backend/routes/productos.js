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
router.post('/', auth.requerido, crearProducto)
router.put('/:id',auth.requerido, modificarProducto)
router.delete('/:id',auth.requerido, eliminarProducto)

module.exports = router;