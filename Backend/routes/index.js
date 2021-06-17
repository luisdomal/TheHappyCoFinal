var router = require('express').Router();

router.get('/', (req, res)=>{
  res.send('welcome to The Happy CO');
});

router.use('/usuarios', require('./usuarios'));
router.use('/mascotas', require('./productos'));


module.exports = router;
