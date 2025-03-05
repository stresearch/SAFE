FROM huggingface/competitions:latest
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY * .
CMD bash debug.sh