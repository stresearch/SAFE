# Debugging Example

To debug your submission, you can reproduce all the steps locally.

See example [Dockerfile](Dockerfile):

```Dockerfile
FROM huggingface/competitions:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
# change this to your HF token if you accessing private repos
ENV HF_TOKEN=mytoken 
ENV SAFE_DATASET_REPO=safe-challenge/safe-challenge-practice-dataset
RUN huggingface-cli download ${SAFE_DATASET_REPO} --local-dir /tmp/data --repo-type dataset
# change this to your model that you want to test
ENV MODEL_REPO=safe-challenge/safe-example-submission 
RUN huggingface-cli download ${MODEL_REPO} --local-dir /tmp/model --repo-type model
WORKDIR /tmp/model
CMD python script.py
```

There are 4 steps:
- base image is pulled and common requirements are installed
- dataset is downloaded to the container 
- your model is downloaded to the container
- `script.py` is run (which should save out `submission.csv`)

To test your own private repo, you would need to set your huggingface token as an environment variable somewhere. In the Dockerfile: `ENV HF_TOKEN=mytoken`

You can build: `docker build . -t safe-test`  
Then run: `docker run --rm --gpus all safe-test`   

You can map volumes to docker if you want to see the results.
