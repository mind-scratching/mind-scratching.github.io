const fs = require('fs')

const dictFullTxt = fs.readFileSync('dict-full.txt', 'utf-8')

document.getElementById('dict-full').innerHTML = dictFullTxt