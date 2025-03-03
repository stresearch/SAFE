# Debugging Example

To debug your submission, you can reproduce all the steps locally.

See example [Dockerfile](Dockerfile):

```Dockerfile
FROM huggingface/competitions:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV SAFE_DATASET_REPO=safe-challenge/safe-challenge-practice-dataset
RUN huggingface-cli download ${SAFE_DATASET_REPO} --local-dir /tmp/data --repo-type dataset
ENV MODEL_REPO=safe-challenge/safe-example-submission
RUN huggingface-cli download ${MODEL_REPO} --local-dir /tmp/model --repo-type model
WORKDIR /tmp/model
CMD python script.py
```

There are 4 steps:
- base image is pulled and common requirements are installed
- dataset is downloaded to the container 
- your model is downloaed to the container
- `scipt.py` is run (which should should save out `submission.csv`)


You can build: `docker build . -t safe-test`  
Then run: `docker run --rm --gpus all safe-test`   