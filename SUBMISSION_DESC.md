## Model Submission

This is a code based competetion. No data will be released before the competition. A subset of the data may be released after the competition. We will be using [hugginface competions platform](https://github.com/huggingface/competitions).

- Participants will be required to submit their model to be evaluated on the dataset by creating a [huggingface](https://huggingface.co) model repository  (it can be private or public).
- The model will be expected to read in the dataset and output file containing a **detection score and binary decision** for every input example.
- The dataset will be downloaded to `/tmp/data` inside the container during evalation run.
- The only requirement is to have a `script.py` in the top level of the repo that saves a `submission.csv` file with the following columns:
  - `id` : id of the example, strig
  - `pred` : binary decision, string, "generated" or "pristine"
  - `score`: decision score such as log likelihood score. Postive scores correspond to generated and negative to pristine. (This is optional and not used in evaluation but will help with analysis later)  
- All submissions will be evaluated using the same resources: NVIDIA `T4-medium` GPU instance. It has 8vCPUs, 30GB RAM, 16GB VRAM.
- All submissions will be evaluated in the same container that supports common ML frameworks and libraries:
  - Dockerfile: https://github.com/huggingface/competitions/blob/main/Dockerfile
  - Docker Image: https://hub.docker.com/r/huggingface/competitions/tags
  - Requirements File: [requirements.txt](requirements.txt)
  - If you'd like to add another package to the requirments file create an issue here: https://github.com/stresearch/SAFE
  - **During evalation, container will not have access to the internet**. Participants should include all other required dependencies in the model repo.
- Once your model is ready    
  - Go the task submision space (there is a seperate space for every task)
  - Login with your Huggingface Credentials
  - Enter the name of your model e.g. `safe-challenge/safe-example-submission` and click submit! 🎉

**🆘 Helpful Stuff**. We provide an example model submission repo and a practice competition for troubleshooting.  
- Take a look at an example model repo: https://huggingface.co/safe-challenge/safe-example-submission
- We encourage you to submit to a practice competion: https://huggingface.co/spaces/safe-challenge/SAFEChallengePractice
- It's using this pracice dataset: https://huggingface.co/datasets/safe-challenge/safe-challenge-practice-dataset