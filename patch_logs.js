const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/function nxt\(f\)\{/, 'function nxt(f){ console.log("nxt called");');
html = html.replace(/if\(f===1&&!S\.ps\)\{/g, 'if(f===1){ if(!S.ps){showErr(f, "Please select a size ↑");return} console.log("validation passed"); }');
html = html.replace(/if\(f===2&&!S\.pt\)\{/g, 'if(f===2){ if(!S.pt){showErr(f, "Please select a type ↑");return} console.log("validation passed"); }');
html = html.replace(/if\(f===3&&!S\.ca\)\{/g, 'if(f===3){ if(!S.ca){showErr(f, "Please select an option ↑");return} console.log("validation passed"); }');
// For step 5
html = html.replace(/let ok=true;/g, 'let ok=true;'); // placeholder
// The actual step change
html = html.replace(/document\.getElementById\('fs'\+f\)\.classList\.remove\('act'\);/g, 'console.log("changing step"); document.getElementById("fs"+f).classList.remove("act");');

fs.writeFileSync('index.html', html);
