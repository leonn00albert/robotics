const express = require('express');
const app = express();
const { spawn } = require('child_process');

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/templates/index.html');
});

// Stream video when requested
app.get('/video', (req, res) => {
    const raspividProcess = spawn('/usr/bin/raspivid', [
        '-t', '0', // Continuous capture
        '-w', '640',
        '-h', '480',
        '-o', '-' // Output to stdout
    ]);

    const ffmpegProcess = spawn('ffmpeg', [
        '-i', 'pipe:0', // Input from stdin
        '-f', 'mp4', // Output format
        '-movflags', 'frag_keyframe+empty_moov', // Flags for streaming-friendly MP4
        '-reset_timestamps', '1', // Reset timestamps for streaming
        '-vcodec', 'copy', // Use same video codec (H.264)
        '-r', '25', // Framerate (adjust as needed)
        '-y', // Overwrite output file if it exists
        'pipe:1' // Output to stdout
    ]);

    raspividProcess.stdout.pipe(ffmpegProcess.stdin);
    ffmpegProcess.stdout.pipe(res);

    raspividProcess.on('exit', (code, signal) => {
        console.log(`raspivid process exited with code ${code} and signal ${signal}`);
        ffmpegProcess.kill(); // Kill ffmpeg process when raspivid exits
    });

    raspividProcess.on('error', (err) => {
        console.error('Error spawning raspivid:', err);
        res.status(500).send('Error streaming video');
    });

    ffmpegProcess.on('error', (err) => {
        console.error('Error spawning ffmpeg:', err);
        res.status(500).send('Error streaming video');
    });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

