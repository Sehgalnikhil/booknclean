const fs = require('fs');
fetch('https://raw.githubusercontent.com/matthewproctor/australianpostcodes/master/australian_postcodes.json')
  .then(res => res.json())
  .then(data => {
     const stateToCityAll = {
       'NSW': 'Sydney',
       'VIC': 'Melbourne',
       'QLD': 'Brisbane',
       'WA': 'Perth',
       'SA': 'Melbourne',
       'ACT': 'Sydney',
       'TAS': 'Melbourne',
       'NT': 'Brisbane'
     };
     
     const unique = new Set();
     const results = [];
     data.forEach(item => {
        const name = item.locality;
        const state = item.state;
        const city = stateToCityAll[state];
        if (!name || !city || !state) return;
        
        const formattedName = name.toLowerCase().replace(/\b\w/g, l => l.toUpperCase());
        const key = formattedName + '|' + state;
        if (!unique.has(key)) {
           unique.add(key);
           results.push({ n: formattedName, s: state, c: city });
        }
     });
     
     results.sort((a,b) => a.n.localeCompare(b.n));
     
     const fileContent = 'const SUBURBS = ' + JSON.stringify(results) + ';';
     fs.writeFileSync('suburbs.js', fileContent);
     console.log('Saved suburbs.js with ' + results.length + ' suburbs.');
  });
