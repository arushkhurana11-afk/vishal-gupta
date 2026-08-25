const canvas = document.getElementById("animation-canvas");
const context = canvas.getContext("2d");

// We have 150 frames in the folder, named "frame (1).jpg" to "frame (150).jpg"
const frameCount = 150;

const currentFrame = index => (
    `frames/frame (${index}).jpg`
);

const images = [];
// Create an object to track which images have finished loading
const loadedImages = {};

const preloadImages = () => {
    for (let i = 1; i <= frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
        images[i] = img;
        
        img.onload = () => {
            loadedImages[i] = true;
            // Draw the first frame as soon as it's ready
            if (i === 1) {
                resizeCanvas();
                drawImage(images[1]);
            }
        };
    }
};

const drawImage = (img) => {
    if (!img) return;

    // Calculate aspect ratio and dimensions to cover the canvas without distorting
    const canvasRatio = canvas.width / canvas.height;
    const imgRatio = img.width / img.height;
    
    let drawWidth, drawHeight, offsetX, offsetY;

    if (canvasRatio > imgRatio) {
        drawWidth = canvas.width;
        drawHeight = canvas.width / imgRatio;
        offsetX = 0;
        offsetY = (canvas.height - drawHeight) / 2;
    } else {
        drawWidth = canvas.height * imgRatio;
        drawHeight = canvas.height;
        offsetX = (canvas.width - drawWidth) / 2;
        offsetY = 0;
    }

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
};

const updateCanvas = index => {
    // Frames are 1-indexed (1 to 150)
    if (!images[index] || !loadedImages[index]) return;
    
    requestAnimationFrame(() => {
        drawImage(images[index]);
    });
};

const resizeCanvas = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const html = document.documentElement;
    const scrollTop = html.scrollTop;
    const maxScrollTop = html.scrollHeight - window.innerHeight;
    const scrollFraction = maxScrollTop === 0 ? 0 : scrollTop / maxScrollTop;
    
    // Ensure we get a frame index between 1 and 150
    let frameIndex = Math.floor(scrollFraction * frameCount) + 1;
    if (frameIndex > frameCount) frameIndex = frameCount;
    if (frameIndex < 1) frameIndex = 1;
    
    if (images[frameIndex] && loadedImages[frameIndex]) {
        drawImage(images[frameIndex]);
    }
};

window.addEventListener('resize', resizeCanvas);

window.addEventListener('scroll', () => {  
    const html = document.documentElement;
    const scrollTop = html.scrollTop;
    const maxScrollTop = html.scrollHeight - window.innerHeight;
    const scrollFraction = maxScrollTop === 0 ? 0 : scrollTop / maxScrollTop;
    
    // Calculate the frame index based on scroll progress (1 to 150)
    let frameIndex = Math.floor(scrollFraction * frameCount) + 1;
    if (frameIndex > frameCount) frameIndex = frameCount;
    if (frameIndex < 1) frameIndex = 1;
    
    updateCanvas(frameIndex);
});

// Initialize
preloadImages();

const drawFirstFrameWhenReady = () => {
    if (loadedImages[1]) {
        // explicitly set canvas size and draw the first frame 
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        drawImage(images[1]);
    } else {
        requestAnimationFrame(drawFirstFrameWhenReady);
    }
};

// Start checking for the first frame immediately
drawFirstFrameWhenReady();

// Also update canvas normally when the full page finishes loading
window.addEventListener('load', () => {
    resizeCanvas();
});
