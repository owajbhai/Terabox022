FROM python:3.10-slim

# ffmpeg install karo
RUN apt-get update && apt-get install -y ffmpeg

# Working directory
WORKDIR /app

# Dependencies copy & install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bot code copy
COPY . .

# Bot run command
CMD ["python", "bot.py"]
