const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Replace alerts with a visual error on the next button
html = html.replace("if(f===1&&!S.ps){alert('Please select a property size.');return}", "if(f===1&&!S.ps){showErr(f, 'Please select a size ↑');return}");
html = html.replace("if(f===2&&!S.pt){alert('Please select a property type.');return}", "if(f===2&&!S.pt){showErr(f, 'Please select a type ↑');return}");
html = html.replace("if(f===3&&!S.ca){alert('Please select a carpet option.');return}", "if(f===3&&!S.ca){showErr(f, 'Please select an option ↑');return}");

// Add showErr function right before nxt()
const showErrFunc = `function showErr(step, msg) {
  const btn = document.querySelector('#fs' + step + ' .bn');
  if(!btn) return;
  const originalText = btn.innerText;
  btn.innerText = msg;
  btn.style.background = '#d9381e'; // red
  btn.style.transform = 'translateY(0)';
  setTimeout(() => {
    btn.innerText = originalText;
    btn.style.background = '';
  }, 2000);
}

function nxt(f){`;

html = html.replace('function nxt(f){', showErrFunc);

fs.writeFileSync('index.html', html);
console.log("Fixed alerts in JS");
