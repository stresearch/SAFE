# change this to your HF token if you accessing private repos
# export HF_TOKEN=mytoken 
export SAFE_DATASET_REPO=safe-challenge/safe-challenge-practice-dataset
# change this to your model that you want to test
export MODEL_REPO=safe-challenge/safe-example-submission
export DATASET_PATH=/tmp/data
export MODEL_PATH=/tmp/model 

echo -e "\n\n\n*******************\n\n\n"

echo "STEP 2: downloading dataset"
python download_dataset.py
echo "downloaded dataset"
ls -R $DATASET_PATH

echo -e "\n\n\n*******************\n\n\n"

echo "STEP 3: downloading model"
python download_model.py
echo "downloaded model"
ls -R $MODEL_PATH

echo -e "\n\n\n*******************\n\n\n"

cd $MODEL_PATH
echo "STEP 4: running script.py"
cat "script.py"
python script.py

echo -e "\n\n\n*******************\n\n\n"

echo "output file"
cat "submission.csv"

