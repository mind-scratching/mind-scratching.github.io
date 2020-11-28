var codeTags = document.getElementsByTagName("code")
var i;
for (i = 0; i < codeTags.length; i++) {
  if (codeTags[i].className != "code") {
    codeTags[i].className = "prettyprint lang-python"
  }
}

var preBlocks = document.getElementsByClassName("prettyprint lang-python")
var i;
for (i = 0; i < preBlocks.length; i++) {
  preBlocks[i].innerHTML = preBlocks[i].innerHTML.replace(/\s+$/, "\n")
  preBlocks[i].innerHTML = preBlocks[i].innerHTML.replace(/^\s+/, "")
}

var codeBlocks = document.getElementsByClassName("code")
var i;
for (i = 0; i < codeBlocks.length; i++) {
  codeBlocks[i].innerHTML = codeBlocks[i].innerHTML.replace(/\s+$/, "")
  codeBlocks[i].innerHTML = codeBlocks[i].innerHTML.replace(/^\s+/, "")
  codeBlocks[i].innerHTML = codeBlocks[i].innerHTML + "\n"
}