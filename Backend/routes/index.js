var router = require('express').Router();

router.get('/', (req, res)=>{
  res.send('welcome to The Happy CO');
});

router.use('/usuarios', require('./usuarios'));
router.use('/productos', require('./productos'));


module.exports = router;
