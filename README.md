
# Video OCR Analysis

This program analyzes a video file by performing Optical Character Recognition (OCR) on each frame using Tesseract OCR. It compares the performance of OCR on a GPU and CPU, generating performance metrics and visualizations based on the results.

## Features

- Performs OCR on video frames using Tesseract.
- Supports GPU and CPU processing, comparing performance metrics.
- Calculates frames per second (FPS), total characters detected, and average characters per frame.
- Outputs results to text files for both GPU and CPU processing.
- Visualizes performance comparisons using Matplotlib.

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- TensorFlow
- Matplotlib
- NumPy
- pytesseract
- OS module (standard library)

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python packages:
   ```bash
   pip install opencv-python pytesseract tensorflow matplotlib
   ```

3. **Install Tesseract OCR:**
   - Windows: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Linux: Install using the package manager (e.g., `sudo apt install tesseract-ocr`).

4. Ensure Tesseract is in your system's PATH or specify the path in the code.

## Usage

1. Update the video file path and output file paths in the script:
   ```python
   video_file_path = r"C:\path\to\your\video.mp4"
   output_file_path = r"C:\path\to\output\gpu_ocr_analysis_results.txt"
   output_file_path_cpu = r"C:\path\to\output\cpu_ocr_analysis_results.txt"
   ```

2. Run the script:
   ```bash
   python <your_script_name>.py
   ```

3. To exit the video display, press the 'q' key.

## Output

The program generates two text files containing the analysis results:
- `gpu_ocr_analysis_results.txt`: Metrics for the GPU processing.
- `cpu_ocr_analysis_results.txt`: Metrics for the CPU processing.

It also generates bar plots comparing:
- FPS performance
- Number of frames with detected text
- Total characters detected
- Processing time

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [TensorFlow](https://www.tensorflow.org/)
- [Matplotlib](https://matplotlib.org/)
