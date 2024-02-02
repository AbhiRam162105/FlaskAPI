FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001
EXPOSE 8000

# Define environment variable for production
ENV FLASK_ENV=production

# Run app.py when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "apis:app"]
