const https = require('https');
const fs = require('fs');

https.get('https://vk.com/bsekat', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const regex = /https:\/\/sun[0-9\-a-z\.]+\.userapi\.com\/[a-zA-Z0-9\/\-_]+\.(jpg|png)/g;
    const matches = [...new Set(data.match(regex))];
    console.log(JSON.stringify(matches, null, 2));
  });
});
