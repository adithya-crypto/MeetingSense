# MeetingSense: AI-Powered Meeting Transcription & Summarization

An intelligent web application that transcribes and summarizes audio recordings, turning lengthy meetings into actionable insights.

## Overview

MeetingSense is a Flask-based web application that leverages AI to transcribe audio recordings and generate comprehensive summaries. This tool is designed to help teams capture key discussion points, decisions, and action items from meetings, saving time and improving documentation.

## Key Features

- **Audio Transcription**: Converts spoken content to text using OpenAI's Whisper
- **Intelligent Summarization**: Generates concise, structured summaries with Gemma LLM
- **Multiple Audio Formats**: Supports various audio formats including WAV, MP3, OGG, M4A, FLAC
- **In-Browser Recording**: Record audio directly in your browser
- **User-Friendly Interface**: Simple upload, record, and review workflow
- **Responsive Design**: Works on desktop and mobile devices

## Technical Components

- **Flask Backend**: Handles file uploads, processing, and serving results
- **OpenAI Whisper**: State-of-the-art speech recognition model for transcription
- **Gemma LLM**: Generates meaningful summaries from transcribed text
- **Ollama Integration**: Local AI model deployment
- **Asynchronous Processing**: Background task handling for long-running operations

## Requirements

- Python 3.8+
- Flask
- OpenAI Whisper
- Ollama
- PyTorch
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/meetingsense.git
   cd meetingsense
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Whisper and Ollama:
   ```
   pip install git+https://github.com/openai/whisper.git
   curl -fsSL https://ollama.com/install.sh | sh
   ```

4. Pull the Gemma model:
   ```
   ollama pull gemma
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Access the application at http://localhost:5000

## Usage

1. Upload an audio file or record directly in browser
2. Wait for processing (transcription and summarization)
3. Review the generated summary with sections for:
   - Key discussion points
   - Important decisions made
   - Action items and assignments
   - Follow-up tasks

## Project Structure

- `app.py`: Main Flask application
- `summarize.py`: Core logic for audio transcription and text summarization
- `config.py`: Application configuration
- `/templates`: HTML templates for the web interface
- `/uploads`: Storage for uploaded audio files
- `/transcriptions`: Storage for generated transcripts

## Processing Pipeline

1. Audio upload/recording
2. Transcription with Whisper
3. Summarization with Gemma LLM
4. Presentation of formatted results

## Future Enhancements

- Speaker diarization (identifying who said what)
- Meeting analytics and insights
- Integration with calendar and task management systems
- Team collaboration features
- Custom summary templates

## Acknowledgments

- OpenAI Whisper for speech recognition capabilities
- Google's Gemma for text summarization
- Ollama for local AI model serving
