# Dockerfile Plan for chat-ui-app

## Overview
The chat-ui-app project requires a Dockerfile that handles both the React frontend and the Flask backend.

## Dockerfile Content
```dockerfile
# Stage 1: Build React Frontend
FROM node:18 AS frontend-builder
WORKDIR /app/react-frontend
COPY chat-ui-app/react-frontend/package*.json ./
RUN npm install
COPY chat-ui-app/react-frontend/ .
RUN npm run build

# Stage 2: Prepare Python Backend
FROM python:3.9-slim AS backend
WORKDIR /app
COPY chat-ui-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY chat-ui-app/ .

# Copy built React frontend to Flask static directory
COPY --from=frontend-builder /app/react-frontend/dist /app/chat-ui-app/static

# Expose port and set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

# Run Flask application
CMD ["flask", "run", "--port=5000"]
```

## Instructions
1. Create a new file named `Dockerfile` in the root directory.
2. Copy the above Dockerfile content into this new file.
3. Build the Docker image using the command: `docker build -t chat-ui-app .`
4. Run the Docker container using: `docker run -p 5000:5000 chat-ui-app`

## Environment Variables
Ensure to set the following environment variables when running the container:
- `API_ENDPOINT`
- `API_KEY`

Example: `docker run -e API_ENDPOINT='your_api_endpoint' -e API_KEY='your_api_key' -p 5000:5000 chat-ui-app`