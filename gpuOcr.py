import cv2
import pytesseract
import tensorflow as tf
import time

# Check for GPU availability
if tf.config.list_physical_devices('GPU'):
    print("GPU is available, using GPU")
else:
    print("GPU not found, using CPU")

# Specify the video file path
video_file_path = r"C:\Users\USER\Documents\TensorGo Assignment\TensorGoVideoTrain.mp4"
# Specify the output file path for storing metrics
output_file_path = r"C:\Users\USER\Documents\TensorGo Assignment\gpu_ocr_analysis_results.txt"

# Initialize video capture from the file
cap = cv2.VideoCapture(video_file_path)

# Variables for FPS calculation and EDA
total_frames = 0
frames_with_text = 0
total_characters = 0
start_time = time.time()

# Function to perform OCR using pytesseract
def ocr_image(frame):
    # Convert the frame to grayscale for better OCR results
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR on the grayscale frame
    text = pytesseract.image_to_string(gray_frame)
    
    return text

# Process video frames
with open(output_file_path, 'w') as f:  # Open file for writing results
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video or error in reading video file.")
            break
        
        # Increment total frames count
        total_frames += 1
        
        # OCR the frame
        text = ocr_image(frame)
        
        # Count frames with text
        if text.strip():
            frames_with_text += 1
            total_characters += len(text)
        
        # Write frame text to the file
        f.write(f"Frame {total_frames}: Detected text: {text}\n")
        
        # Display the frame (optional)
        cv2.imshow('Video OCR', frame)
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # End time for FPS calculation
    end_time = time.time()

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

# Calculate FPS
elapsed_time = end_time - start_time
fps = total_frames / elapsed_time

# Exemplary Data Analysis summary
average_characters_per_frame = total_characters / total_frames if total_frames > 0 else 0

# Write EDA summary to the output file
with open(output_file_path, 'a') as f:
    f.write("\n--- Exemplary Data Analysis ---\n")
    f.write(f"Total frames processed: {total_frames}\n")
    f.write(f"Frames with detected text: {frames_with_text}\n")
    f.write(f"Total characters detected: {total_characters}\n")
    f.write(f"Average characters per frame: {average_characters_per_frame:.2f}\n")
    f.write(f"Processing time (seconds): {elapsed_time:.2f}\n")
    f.write(f"Average FPS: {fps:.2f}\n")

# Print EDA summary to console
print("\n--- Exemplary Data Analysis ---")
print(f"Total frames processed: {total_frames}")
print(f"Frames with detected text: {frames_with_text}")
print(f"Total characters detected: {total_characters}")
print(f"Average characters per frame: {average_characters_per_frame:.2f}")
print(f"Processing time (seconds): {elapsed_time:.2f}")
print(f"Average FPS: {fps:.2f}")
