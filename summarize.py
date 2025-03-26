import subprocess
import os
import shutil
import warnings
import ollama
import json
import time
import torch
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")


def move_transcriptions(audio_name: str, transcr_folder: str) -> str:
    """Move transcription files to appropriate folder and return json path."""
    try:
        audio_stem = Path(audio_name).stem
        transcr_path = os.path.join(transcr_folder, audio_stem)

        os.makedirs(transcr_path, exist_ok=True)

        curr_path = os.getcwd()
        json_file = None

        for ext in ["json", "srt", "tsv", "txt", "vtt"]:
            files = list(Path(curr_path).glob(f"*.{ext}"))
            for file in files:
                dest_file = Path(transcr_path) / file.name
                shutil.move(str(file), str(dest_file))
                if ext == "json":
                    json_file = str(dest_file)

        return json_file
    except Exception as e:
        logger.error(f"Error in move_transcriptions: {str(e)}")
        return None


def audio_to_text(file_path: str) -> str:
    """Transcribe audio to text using Whisper."""
    try:
        logger.info(f"Starting transcription for {file_path}")

        # Auto-detect language
        cmd = f"whisper {file_path} --verbose False"
        subprocess.run(cmd, shell=True, check=True)

        transcr_folder = os.path.join(os.getcwd(), "transcriptions")
        dest_path = move_transcriptions(file_path, transcr_folder)

        if not dest_path:
            raise Exception("Transcription files not found")

        logger.info(f"Transcription completed successfully for {file_path}")
        return dest_path
    except Exception as e:
        logger.error(f"Error in audio_to_text: {str(e)}")
        return None


def text_summarization(dest_path: str) -> str:
    """Summarize transcribed text using Gemma."""
    try:
        with open(dest_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        text = data["text"]
        logger.info("Starting summary generation")

        if torch.cuda.is_available():
            torch.cuda.set_device(0)

        system_prompt = """
        Your task is to generate a comprehensive summary of the meeting transcript provided.
        Focus on:
        1. Key discussion points
        2. Important decisions made
        3. Action items and assignments
        4. Follow-up tasks
        
        Format the summary with appropriate sections and bullet points.
        Use clear, professional language.
        Preserve any specific numbers, dates, or names mentioned.
        """

        response = ollama.chat(
            model="gemma",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )

        summary = response["message"]["content"]
        logger.info("Summary generated successfully")
        return summary
    except Exception as e:
        logger.error(f"Error in text_summarization: {str(e)}")
        return None


def generate_summary(file_path: str) -> str:
    """Main function to generate summary from audio file."""
    try:
        start_time = time.time()
        logger.info(f"Starting summary generation for {file_path}")

        dest_path = audio_to_text(file_path)
        if not dest_path:
            raise Exception("Transcription failed")

        summary = text_summarization(dest_path)
        if not summary:
            raise Exception("Summarization failed")

        end_time = time.time()
        logger.info(
            f"Summary generation completed in {end_time - start_time:.2f} seconds"
        )

        return summary
    except Exception as e:
        logger.error(f"Error in generate_summary: {str(e)}")
        return None
