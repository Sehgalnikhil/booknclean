const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace handleInteraction
const originalHandle = `  const handleInteraction = (e) => {
    // Handle Navigation Buttons
    const btnNav = e.target.closest('[data-nxt], [data-prv]');`;

const newHandle = `  const handleInteraction = (e) => {
    // Handle Navigation Buttons
    const btnNav = e.target.closest('[data-nxt], [data-prv]');
    if (btnNav && btnNav.hasAttribute('data-nxt')) {
      console.log("button tapped", e.type, "target:", e.target.tagName);
    }`;

html = html.replace(originalHandle, newHandle);

// Replace nxt
html = html.replace(/function nxt\(f\)\{/, 'function nxt(f){ console.log("nxt called");');
html = html.replace(/if\(f===1&&!S\.ps\)\{showErr\(f, 'Please select a size ↑'\);return\}/g, 'if(f===1){ if(!S.ps){showErr(f, "Please select a size ↑");return} console.log("validation passed"); }');
html = html.replace(/if\(f===2&&!S\.pt\)\{showErr\(f, 'Please select a type ↑'\);return\}/g, 'if(f===2){ if(!S.pt){showErr(f, "Please select a type ↑");return} console.log("validation passed"); }');
html = html.replace(/if\(f===3&&!S\.ca\)\{showErr\(f, 'Please select an option ↑'\);return\}/g, 'if(f===3){ if(!S.ca){showErr(f, "Please select an option ↑");return} console.log("validation passed"); }');
html = html.replace(/document\.getElementById\('fs'\+f\)\.classList\.remove\('act'\);/g, 'console.log("changing step"); document.getElementById("fs"+f).classList.remove("act");');

fs.writeFileSync('index.html', html);
