const fs = require('fs');
let css = fs.readFileSync('style.css', 'utf8');

css = css.replace(/\.obtn \*, \.cbtn \*, \.adck \* \{\n  pointer-events: none;\n\}/g, "/* pointer-events removed to fix iOS click bug */");

fs.writeFileSync('style.css', css);
console.log("Fixed pointer-events in CSS");
