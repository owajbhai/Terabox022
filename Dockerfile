# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Telegram API Token (replace with your actual token during deployment)
ENV TELEGRAM_API_TOKEN="your-telegram-bot-api-token"

# Expose port (optional, only needed if your app is a web server, but not needed for this bot)
# EXPOSE 8080

# Command to run the bot
CMD ["python", "bot.py"]
