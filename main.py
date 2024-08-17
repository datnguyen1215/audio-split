import argparse
import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def split_audio_on_silence(audio_path, out_dir, min_silence_len=500, silence_thresh=-40, padding_duration=1000):
    """
    Splits the audio file based on silent chunks and saves the non-silent parts in the output directory.
    
    :param audio_path: Path to the input audio file.
    :param out_dir: Directory to save the output chunks.
    :param min_silence_len: Minimum length of silence to be used for a split (in ms).
    :param silence_thresh: Silence threshold (in dBFS). Consider segments below this threshold as silence.
    :param padding_duration: Duration of silence to add before and after each chunk (in ms).
    """
    
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # get file name without extension
    audio_file_name = os.path.splitext(os.path.basename(audio_path))[0]
    
    # Detect non-silent chunks
    nonsilent_chunks = detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    # Silence segment for padding
    silence = AudioSegment.silent(duration=padding_duration)
    
    # Split and save each non-silent chunk
    for i, (start, end) in enumerate(nonsilent_chunks):
        chunk = audio[start:end]
        # Add silence before and after the chunk
        chunk_with_padding = silence + chunk + silence
        chunk_filename = os.path.join(out_dir, f'{audio_file_name}_{i + 1}.mp3')
        chunk_with_padding.export(chunk_filename, format='mp3')
        print(f'Saved {chunk_filename}')

def main():
    parser = argparse.ArgumentParser(description="Split an audio file into multiple files based on silence gaps.")
    parser.add_argument('audio_file', type=str, help="The input audio file (e.g., audio.mp3)")
    parser.add_argument('--out-dir', type=str, required=True, help="Output directory to save the split audio files")
    parser.add_argument('--padding', type=int, default=1000, help="Duration of silence padding before and after each chunk (in ms)")
    parser.add_argument('--min-silence-length', type=int, default=500, help="Duration of silence threshold to detect silence (in ms)")
    
    args = parser.parse_args()
    
    split_audio_on_silence(args.audio_file, args.out_dir, padding_duration=args.padding, min_silence_len=args.min_silence_length)

if __name__ == "__main__":
    main()