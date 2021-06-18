// Producto.js
const mongoose = require("mongoose");

const ProductoSchema = new mongoose.Schema({
    producto: {type: String, required: true}, // Nombre del producto
    categoria: { type: String, enum: ['tincturas', 'body lotion', 'gomitas', 'cremas', 'vapes'] }, // tincturas|body lotion|gomitas|cremas|vapes
    foto: [String], // Links a la fotografía
    descripcion: {type:String, required: true}, // Descripción del producto
    precio: {type:Number, required: true}, // Precio del producto
  }, 
  { timestamps: true }
);

ProductoSchema.methods.publicData = function(){
  return {
    id: this.id,
    producto: this.producto,
    categoria: this.categoria,
    foto: this.foto,
    descripcion: this.descripcion,
    precio: this.precio,
    createdAt: this.createdAt,
    updatedAt: this.updatedAt
  };
};

mongoose.model('Producto', ProductoSchema) //Define el modelo Producto, utilizando el esquema ProductoSchema.