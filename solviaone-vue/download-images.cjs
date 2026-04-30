const https = require('https');
const fs = require('fs');
const path = require('path');

const images = [
  { url: 'https://picsum.photos/seed/hero/800/600', name: 'hero-tech-team.jpg' },
  { url: 'https://picsum.photos/seed/office/800/600', name: 'office-meeting.jpg' },
  { url: 'https://picsum.photos/seed/tech/800/600', name: 'tech-infrastructure.jpg' },
  { url: 'https://picsum.photos/seed/server/800/600', name: 'server-room.jpg' },
  { url: 'https://picsum.photos/seed/modern-office/800/450', name: 'modern-office.jpg' },
  { url: 'https://picsum.photos/seed/ecommerce/800/450', name: 'ecommerce-platform.jpg' },
  { url: 'https://picsum.photos/seed/cloud/800/450', name: 'cloud-infrastructure.jpg' },
  { url: 'https://picsum.photos/seed/security/800/450', name: 'security.jpg' }
];

const dir = 'public/images';
if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

let completed = 0;
images.forEach(img => {
  const file = fs.createWriteStream(path.join(dir, img.name));
  https.get(img.url, (res) => {
    res.pipe(file);
    file.on('finish', () => {
      file.close();
      completed++;
      console.log('Downloaded:', img.name);
      if (completed === images.length) console.log('All done!');
    });
  }).on('error', (err) => {
    fs.unlink(img.name, () => {});
    console.error('Error:', err.message);
  });
});