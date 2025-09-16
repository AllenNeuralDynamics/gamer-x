FROM python:3.11-slim

# Create a non-root user (required by Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency metadata first
COPY --chown=user pyproject.toml ./

# Install build requirements
RUN pip install --no-cache-dir --upgrade pip setuptools wheel build

# Copy the rest of the code
COPY --chown=user . /app

# Install your package and deps
RUN pip install --no-cache-dir .

# Hugging Face Spaces expect apps to listen on port 7860
EXPOSE 7860

# Run Chainlit app (adjust path if needed)
CMD ["chainlit", "run", "src/gamer_x/interface/app.py", "--host", "0.0.0.0", "--port", "7860"]

