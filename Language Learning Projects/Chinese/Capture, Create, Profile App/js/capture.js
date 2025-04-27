// Example JavaScript for the Capture section
const cameraFeed = document.getElementById('camera-feed');
const captureButton = document.getElementById('capture-button');

// Access the user's camera
async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraFeed.srcObject = stream;
    } catch (error) {
        console.error('Error accessing camera:', error);
    }
}

// Capture image from camera feed
captureButton.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = cameraFeed.videoWidth;
    canvas.height = cameraFeed.videoHeight;
    
    const ctx = canvas.getContext('2d');
    ctx.drawImage(cameraFeed, 0, 0, canvas.width, canvas.height);

    const imageDataURL = canvas.toDataURL('image/png');

    // Integrate Tesseract.js for OCR processing
    Tesseract.recognize(
        imageDataURL,
        'eng', // Language code (English)
        { logger: m => console.log(m) } // Logging options
    ).then(({ data: { text } }) => {
        console.log('Extracted Text:', text);

        // Now you can use the extracted text for further processing
        // For example, send it to your language analysis component.
    }).catch(error => {
        console.error('OCR Error:', error);
    });
});

// Start the camera when the page loads
startCamera();
