const fs = require('fs');

const dictFullTxt = fs.readFileSync('source/dict-full.txt', 'utf-8')

var dictFull = document.getElementsById('dict-full')
dictFull.innerHTML = dictFullTxt