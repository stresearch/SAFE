FROM huggingface/competitions:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV SAFE_DATASET_REPO=safe-challenge/safe-challenge-practice-dataset
RUN huggingface-cli download ${SAFE_DATASET_REPO} --local-dir /tmp/data --repo-type dataset
ENV MODEL_REPO=safe-challenge/safe-example-submission
RUN huggingface-cli download ${MODEL_REPO} --local-dir /tmp/model --repo-type model
WORKDIR /tmp/model
CMD python script.py