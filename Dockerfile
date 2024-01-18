# Base stage for shared environment setup
FROM python:3.10.12-slim as base

# Set unbuffered mode for immediate log output
ENV PYTHONUNBUFFERED True
# ENV PYTHONPATH /app

# Set the working directory in the container
ENV APP_HOME /
WORKDIR $APP_HOME

# Copy the application files to the container
COPY . $APP_HOME/

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Test stage - runs tests
FROM base as tester

# Install test dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Run tests (adjust the command according to your test runner)
COPY run_tests.sh .
RUN ./run_tests.sh

# Final stage for the production image
FROM base as production

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN ls -la app
# Set the command to run the web service on container startup using gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app