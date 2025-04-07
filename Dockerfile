FROM huggingface/competitions:latest
WORKDIR /app/safe
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY * .
CMD bash debug.sh