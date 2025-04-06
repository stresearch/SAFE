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

> all the files are in the [main repo](https://github.com/stresearch/SAFE/)

To test your own private repo, you would need to set your huggingface token as an environment variable somewhere. In the Dockerfile: `export HF_TOKEN=mytoken`

You can build: `docker build . -t safe-test`  
Then run: `docker run --rm --gpus all safe-test`   

You can map volumes to docker if you want to see the results, etc.

The [sample_practice_submission.csv](sample_practice_submission.csv) should look like this:
```csv
id,pred,score,time
9712245a-548d-584c-a82d-a543f1ea21ac,generated,0.8955863118171692,18.962587118148804
07bd0843-74a6-53ec-a3f0-00dfc31d6e2a,pristine,-0.4735659658908844,0.03756999969482422
06704fa4-5a0c-540c-86e6-c98af1528478,generated,0.4556829333305359,0.027454853057861328
c3e008aa-e4ba-5d2a-b37e-dd6d0ae640cb,pristine,-0.05135703459382057,0.03614068031311035
12dae22b-3251-5204-ad61-bdf55ccfff51,generated,0.752806544303894,0.03131747245788574
b681b921-7842-5942-b378-c491372dff93,pristine,-2.2116477489471436,0.03128170967102051
b2373bde-1e59-56cd-877b-c38dbce7e1d2,pristine,-1.3747910261154175,0.03574991226196289
6beaf7e5-2049-5640-bcad-2b77e31a3956,generated,0.5170786380767822,0.0328369140625
d346af27-f9f2-597d-b848-8e9d57a00847,pristine,-0.7394500374794006,0.031241655349731445
4cc52c06-b8d4-5b83-9069-a602bd2d71ef,pristine,-0.3091548681259155,0.03464174270629883
a7d079be-525a-547e-bc4a-984f1d61aa6f,pristine,-0.304933100938797,0.02721118927001953
a657caf4-4b97-5797-8c57-775fbd78aedd,generated,1.1447159051895142,0.025275468826293945
ec9778de-9c5c-5e20-b242-847ce24a10e1,pristine,-0.9481428265571594,0.03555035591125488
55117a10-2d11-5b76-adc5-39070c4987ca,pristine,-1.9522984027862549,0.02613973617553711
e08e97ff-ec7e-531f-afda-1749b550d4bf,generated,0.5286235809326172,0.03823685646057129
```



