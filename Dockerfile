# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /Cocktail-App

# Copy your application code
COPY . .

# Install dependencies (replace 'requirements.txt' with your actual file)
RUN pip install -r requirements.txt

# Expose the port your application runs on 4000
EXPOSE 4000

# Run the application command
CMD [ "python3", "app.py" ]