const fs = require('fs');
const path = require('path');

const sydneySuburbs = [
  "Bondi", "Bondi Junction", "Surry Hills", "Newtown", "Parramatta", "Chatswood", "Manly", "Cronulla", "Mosman", "Randwick", "Darlinghurst", "Paddington", "Glebe", "Leichhardt", "Balmain", "Ryde", "Hornsby", "Liverpool", "Campbelltown", "Penrith", "Blacktown", "Bankstown", "Hurstville", "Kogarah", "Strathfield", "Auburn", "Burwood", "Eastwood", "Dee Why", "Brookvale"
];
const melbourneSuburbs = [
  "Richmond", "Fitzroy", "Collingwood", "South Yarra", "St Kilda", "Carlton", "Brunswick", "Prahran", "Hawthorn", "Camberwell", "Box Hill", "Doncaster", "Footscray", "Sunshine", "Dandenong", "Frankston", "Ringwood", "Chadstone", "Glen Waverley", "Oakleigh", "Northcote", "Preston", "Coburg", "Essendon", "Moonee Ponds", "Point Cook", "Werribee", "Craigieburn", "Epping", "Narre Warren"
];
const brisbaneSuburbs = [
  "South Brisbane", "Fortitude Valley", "New Farm", "Paddington", "Indooroopilly", "Chermside", "Carindale", "Mt Gravatt", "Sunnybank", "Logan", "Ipswich", "Redcliffe", "Nundah", "Lutwyche", "Kedron", "Stafford", "Aspley", "Everton Park", "Mitchelton", "The Gap", "Kenmore", "Toowong", "Auchenflower", "Milton", "Woolloongabba", "Annerley", "Greenslopes", "Coorparoo", "Camp Hill", "Capalaba"
];
const perthSuburbs = [
  "Subiaco", "Fremantle", "Cottesloe", "Scarborough", "Joondalup", "Mandurah", "Midland", "Armadale", "Rockingham", "Cannington", "Belmont", "Victoria Park", "South Perth", "Como", "Applecross", "Melville", "Bibra Lake", "Cockburn Central", "Baldivis", "Success", "Ellenbrook", "Mirrabooka", "Malaga", "Morley", "Dianella", "Stirling", "Innaloo", "Osborne Park", "Wembley", "Floreat"
];

const allSuburbs = [
  ...sydneySuburbs.map(s => ({ name: s, region: "Sydney" })),
  ...melbourneSuburbs.map(s => ({ name: s, region: "Melbourne" })),
  ...brisbaneSuburbs.map(s => ({ name: s, region: "Brisbane" })),
  ...perthSuburbs.map(s => ({ name: s, region: "Perth" }))
];

// Clean duplicates just in case (e.g. Paddington is in both Sydney and Brisbane)
// We'll keep the first one we find for simplicity, or we can just iterate them all.
const uniqueSuburbs = [];
const seen = new Set();
for (const sub of allSuburbs) {
  if (!seen.has(sub.name)) {
    seen.add(sub.name);
    uniqueSuburbs.push(sub);
  }
}

const template = fs.readFileSync('index.html', 'utf8');

uniqueSuburbs.forEach(sub => {
    const suburb = sub.name;
    const region = sub.region;
    let content = template;
    
    // Replace Title
    content = content.replace(
        '<title>Bond Cleaning | Fixed Price End of Lease Cleaning — Book & Clean</title>',
        `<title>Bond Cleaning in ${suburb} | Fixed Price End of Lease Cleaning</title>`
    );
    
    // Replace OG Title
    content = content.replace(
        '<meta property="og:title" content="Bond Cleaning | Fixed Price End of Lease Cleaning — Book & Clean">',
        `<meta property="og:title" content="Bond Cleaning in ${suburb} | Fixed Price End of Lease Cleaning">`
    );

    // Replace Description
    content = content.replace(
        '<meta name="description" content="Fixed-price bond cleaning with a written bond-back guarantee. Instant online quote, no phone call needed.">',
        `<meta name="description" content="Fixed-price bond cleaning in ${suburb} with a written bond-back guarantee. Instant online quote, no phone call needed.">`
    );
    
    // Replace OG Description
    content = content.replace(
        '<meta property="og:description" content="Fixed-price bond cleaning with a written bond-back guarantee. Oven deep clean always included. Instant online quote.">',
        `<meta property="og:description" content="Fixed-price bond cleaning in ${suburb} with a written bond-back guarantee. Oven deep clean always included.">`
    );

    // Replace Hero Text
    content = content.replace(
        '>Fixed Price Bond Cleaning<',
        `>Fixed Price Bond Cleaning in ${suburb}<`
    );
    
    // Pre-fill suburb in JS payload
    content = content.replace(
        `id="suburbInput" placeholder="🔍 Enter your suburb (e.g. Bondi)"`,
        `id="suburbInput" placeholder="🔍 Enter your suburb (e.g. Bondi)" value="${suburb}, ${region === 'Sydney' ? 'NSW' : region === 'Melbourne' ? 'VIC' : region === 'Brisbane' ? 'QLD' : 'WA'}"`
    );

    // Set the hidden city input
    content = content.replace(
        `id="isub" value=""`,
        `id="isub" value="${region}"`
    );

    // Set the default JS state variables for pricing calculation
    content = content.replace(
        `city:''`,
        `city:'${region}'`
    );
    content = content.replace(
        `sub:''`,
        `sub:'${suburb}'`
    );

    // Make URL friendly name
    const slug = suburb.toLowerCase().replace(/\s+/g, '-');
    const filename = `bond-cleaning-${slug}.html`;
    
    fs.writeFileSync(filename, content);
});

console.log(`Successfully generated ${uniqueSuburbs.length} SEO landing pages.`);
