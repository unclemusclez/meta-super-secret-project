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