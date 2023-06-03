FROM python:3.10-bullseye

# Define variables used by python
ENV PATH=/opt/python/bin:/driver:/home/app/.local/bin:$PATH
ENV PYTHONPATH=/app/src/
ENV PIP_EXTRA_INDEX_URL=''

# Upgrade libraries
RUN apt update && apt upgrade -y

# Copy repository content to app
COPY . /app
WORKDIR /app/src

# Pip dependencies
RUN --mount=type=secret,id=pip_extra_index_url PIP_EXTRA_INDEX_URL=`cat /run/secrets/pip_extra_index_url` && \
    pip install pip --upgrade && \
    pip install -r /app/requirements.txt --use-deprecated=legacy-resolver

# Expose api serving port
EXPOSE 5000

# Add deafult user and group app
RUN useradd -ms /bin/bash app
USER app

# Execute container with the following command
CMD ["uvicorn", "api_main:app", "--host", "0.0.0.0", "--port", "5000" ]
