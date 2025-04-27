// Access the camera feed
const cameraFeed = document.getElementById('camera-feed');
const captureButton = document.getElementById('capture-btn');

async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraFeed.srcObject = stream;
    } catch (error) {
        console.error('Error accessing camera:', error);
    }
}

// Capture image from camera feed
function captureImage() {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = cameraFeed.videoWidth;
    canvas.height = cameraFeed.videoHeight;
    context.drawImage(cameraFeed, 0, 0, canvas.width, canvas.height);

    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    // Implement OCR library integration here to extract text from the image
    // Example: const extractedText = yourOCRFunction(imageData);

    // Do something with the extracted text
    console.log('Extracted Text:', extractedText);
}

captureButton.addEventListener('click', captureImage);
startCamera();

const words = ["word1", "word2", "word3", "word4"]; // Sample words for practice
let currentIndex = 0;

const wordDisplay = document.getElementById("wordDisplay");
const nextButton = document.getElementById("nextButton");
const practiceButton = document.getElementById("practiceButton");

function displayWord(index) {
    wordDisplay.textContent = words[index];
}

nextButton.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % words.length;
    displayWord(currentIndex);
});

practiceButton.addEventListener("click", () => {
    // Implement practice functionality, e.g., interactive exercises
    console.log("Practicing:", words[currentIndex]);
    // Track usage counts
    // Update UI or move to the next word
});
