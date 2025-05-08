FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get install -y cron

# Copy app and crontab
COPY . .

# Install crontab (user-based, no `root` keyword)
RUN crontab crontab.txt

# Create log file
RUN touch /var/log/cron.log

# Keep container running with cron
CMD ["cron", "-f"]
