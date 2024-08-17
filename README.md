# Audio Splitter

This script splits an audio file into multiple files based on silence gaps. Each non-silent segment is saved as a separate audio file, with optional silence padding before and after the segment.

## Requirements

- `pydub` library
- `ffmpeg` or `libav` installed on your system (required by `pydub`)

All Python dependencies can be installed using `requirements.txt`.

## Installation

1. **Clone the repository or download the script**:

```sh
git clone <repository_url>
cd <repository_directory>
```

2. **Install the required Python libraries**:

```sh
pip install -r requirements.txt
```

3. **Install `ffmpeg`**:

   - **On Ubuntu**:
     ```sh
     sudo apt-get install ffmpeg
     ```
   - **On macOS**:
     ```sh
     brew install ffmpeg
     ```
   - **On Windows**:
     Download the executable from the [ffmpeg official website](https://ffmpeg.org/download.html) and follow the installation instructions.

## Usage

Run the script with the following command-line arguments:

```sh
python audio_splitter.py <audio_file> --out-dir <output_directory> [--padding <padding_duration>] [--min-silence-length <silence_length>]
```

### Arguments

- `<audio_file>`: The input audio file (e.g., `audio.mp3`).
- `--out-dir`: The directory to save the split audio files.
- `--padding`: (Optional) Duration of silence padding before and after each segment (in milliseconds). Default is `1000` ms.
- `--min-silence-length`: (Optional) Minimum duration of silence to use for splitting (in milliseconds). Default is `500` ms.

### Example

To split `audio.mp3` into segments based on silence and save the segments in the `output` directory:

```sh
python audio_splitter.py audio.mp3 --out-dir output --padding 500 --min-silence-length 300
```

## License

This project is licensed under the MIT License.

---

Happy splitting! 🎶