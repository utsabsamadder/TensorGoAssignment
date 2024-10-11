import os
import re
import matplotlib.pyplot as plt

# File paths for GPU and CPU analysis results
gpu_results_file = r"C:\Users\USER\Documents\TensorGo Assignment\gpu_ocr_analysis_results.txt"
cpu_results_file = r"C:\Users\USER\Documents\TensorGo Assignment\cpu_ocr_analysis_results.txt"

# Function to parse the analysis file and extract key metrics
def parse_results(file_path):
    results = {}
    with open(file_path, 'r') as file:
        content = file.read()
        # Extract metrics using regex
        results['total_frames'] = int(re.search(r"Total frames processed: (\d+)", content).group(1))
        results['frames_with_text'] = int(re.search(r"Frames with detected text: (\d+)", content).group(1))
        results['total_characters'] = int(re.search(r"Total characters detected: (\d+)", content).group(1))
        results['average_characters_per_frame'] = float(re.search(r"Average characters per frame: ([\d.]+)", content).group(1))
        results['processing_time'] = float(re.search(r"Processing time \(seconds\): ([\d.]+)", content).group(1))
        results['fps'] = float(re.search(r"Average FPS: ([\d.]+)", content).group(1))
    return results

# Parse the results for both GPU and CPU
gpu_results = parse_results(gpu_results_file)
cpu_results = parse_results(cpu_results_file)

# Function to compare results and print the conclusion
def compare_results(gpu_results, cpu_results):
    print("--- GPU vs CPU OCR Performance Comparison ---\n")
    
    # Compare FPS
    print(f"GPU FPS: {gpu_results['fps']:.2f} | CPU FPS: {cpu_results['fps']:.2f}")
    
    # Compare frames with detected text
    print(f"Frames with detected text: GPU: {gpu_results['frames_with_text']} | CPU: {cpu_results['frames_with_text']}")
    
    # Compare total characters detected
    print(f"Total characters detected: GPU: {gpu_results['total_characters']} | CPU: {cpu_results['total_characters']}")
    
    # Compare processing time
    print(f"Processing time (seconds): GPU: {gpu_results['processing_time']:.2f} | CPU: {cpu_results['processing_time']:.2f}")

    # Return data for plotting
    return {
        'fps': [gpu_results['fps'], cpu_results['fps']],
        'frames_with_text': [gpu_results['frames_with_text'], cpu_results['frames_with_text']],
        'total_characters': [gpu_results['total_characters'], cpu_results['total_characters']],
        'processing_time': [gpu_results['processing_time'], cpu_results['processing_time']]
    }

# Perform the comparison and collect data for plotting
data = compare_results(gpu_results, cpu_results)

# Plot the comparison using matplotlib
def plot_comparison(data):
    labels = ['GPU', 'CPU']
    
    # Plot FPS comparison
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data['fps'], color=['blue', 'orange'])
    plt.title('FPS Comparison (GPU vs CPU)')
    plt.ylabel('Frames Per Second (FPS)')
    plt.show()
    
    # Plot Frames with detected text comparison
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data['frames_with_text'], color=['blue', 'orange'])
    plt.title('Frames with Detected Text (GPU vs CPU)')
    plt.ylabel('Number of Frames with Text')
    plt.show()
    
    # Plot Total characters detected comparison
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data['total_characters'], color=['blue', 'orange'])
    plt.title('Total Characters Detected (GPU vs CPU)')
    plt.ylabel('Total Characters Detected')
    plt.show()
    
    # Plot Processing time comparison
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data['processing_time'], color=['blue', 'orange'])
    plt.title('Processing Time (GPU vs CPU)')
    plt.ylabel('Processing Time (seconds)')
    plt.show()

# Call the plotting function
plot_comparison(data)
