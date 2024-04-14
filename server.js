const express = require('express');
const Raspistill = require('node-raspistill').Raspistill;
const path = require('path');

const app = express();
const camera = new Raspistill({
  width: 640,
  height: 480,
  noPreview: true // Disable preview window
});

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route to serve the camera feed images
app.get('/camera-feed', async (req, res) => {
  const imageBuffer = await camera.takePhoto();
  res.writeHead(200, { 'Content-Type': 'image/jpeg' });
  res.end(imageBuffer);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

