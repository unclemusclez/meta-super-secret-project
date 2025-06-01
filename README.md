# Chat UI App

## Overview
The Chat UI App is a project that provides a user interface for interacting with various AI models and APIs to gather information about nearby landmarks. It uses a React frontend and a Flask backend.

## How to Run
1. Install the required dependencies for both the frontend and backend.
2. Set the necessary environment variables in a `.env` file.
3. Start the Flask backend using `python chat-ui-app/app.py`.
4. Start the React frontend using `npm run start` in the `chat-ui-app/react-frontend` directory.

## Future Plans
1. Implement MCP tooling for STT (Speech-to-Text) to enable voice-operated tools on mobile devices.
2. Use environment variables for model names.
3. Implement two models: one for tooling with MCP calls and gathering Google API information, and another for compiling the complete narrative.
4. Pipeline the narrative output to a TTS (Text-to-Speech) server.
5. Enhance the application with image-to-text features for Google Places landmark information.

## Contact
For more information, contact Devin J. Dawson (unclemusclez) at discord.waterpistol.co.
## Warning: JavaScript is Doodoosauce

We refuse to conform to the JavaScript frontend. Python and Streamlit is our preferred choice.