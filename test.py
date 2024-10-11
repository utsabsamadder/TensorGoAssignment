import tensorflow as tf
import pytesseract
import cv2

# Check for available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"Using GPU: {gpus}")
else:
    print("No GPU found, running on CPU.")

# Load your image using a raw string
image_path = r"C:\Users\USER\Videos\Valorant\Valorant Screenshot 2023.06.26 - 22.56.34.55.png"
img = cv2.imread(image_path)

# Preprocess the image (resize, grayscale, thresholding, etc.)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Perform OCR using pytesseract (a common OCR tool)
# pytesseract will run on CPU, TensorFlow on GPU
ocr_result = pytesseract.image_to_string(threshold_img)
print("OCR Result (GPU):")
print(ocr_result)

# Continue processing or apply TensorFlow models on the image if needed.
# TensorFlow operations will run on GPU if a GPU is detected.
