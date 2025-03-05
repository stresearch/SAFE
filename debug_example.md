# Debugging Example

To debug your submission, you can reproduce all the steps locally.

See example [Dockerfile](Dockerfile):

```Dockerfile
FROM huggingface/competitions:latest
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY * .
CMD bash debug.sh
```

and [debug.sh](debug.sh):

```shell
# change this to your HF token if you accessing private repos
export HF_TOKEN=mytoken 
export SAFE_DATASET_REPO=safe-challenge/safe-challenge-practice-dataset
# change this to your model that you want to test
export MODEL_REPO=safe-challenge/safe-example-submission
export DATASET_PATH=/tmp/data
export MODEL_PATH=/tmp/model 

echo "STEP 2: downloading dataset"
python download_dataset.py

echo "STEP 3: downloading model"
python download_model.py

cd $MODEL_PATH
echo "STEP 4: running script.py"
python script.py
cat "submission.csv"
```

There are 4 steps:
- base image is pulled and common requirements are installed
- dataset is downloaded to the container 
- your model is downloaded to the container
- `script.py` is run (which should save out `submission.csv`)

To test your own private repo, you would need to set your huggingface token as an environment variable somewhere. In the Dockerfile: `export HF_TOKEN=mytoken`

You can build: `docker build . -t safe-test`  
Then run: `docker run --rm --gpus all safe-test`   

You can map volumes to docker if you want to see the results, etc.


