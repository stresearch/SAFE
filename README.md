**❗Some are seeing a message when submitting: `Hugging Face Hub is unreachable, please try again later`. We are working to resolve this issue. Please hold off from submitting anything new. We will let you know when it's working again.**

# SAFE: Synthetic Audio Forensics Evaluation Challenge    <!-- omit from toc -->

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20-Hugging%20Face-yellow)](https://huggingface.co/safe-challenge) [![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/bxNsutKmTH)

![](logo.jpg)

**👉 All participants are required to register for the competition by filling out this [Google Form](https://forms.gle/5J8Yuh41Lv8GAF7w8)**

[📊 Overview](#-overview) • [🥇 Detailed Leaderboard](#-detailed-leaderboard) • [🏆 Prize](#-prize) • [📜 Paper Submission and Dates](#-paper-submission-and-dates) • [📝 Tasks](#-tasks) • [📈 Data](#-data) • [🤖 Model Submission](#-model-submission) • [📂 Create Model Repo](#-create-model-repo) • [🔘 Submit](#-submit) • [🆘 Helpful Stuff](#-helpful-stuff) • [🔍 Evaluation](#-evaluation) • [⚖️ Rules](#️-rules)

## 📣 Updates

2025-03-25
- Added two baselines to the leaderboard
- Added [discord server](https://discord.gg/bxNsutKmTH) for additional help/support/discussion/etc.

2025-04-03  
- Task 2 is now open. Detection of Processed Audio. [https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask2](https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask2)
- 🔥 [Example on including a custom environment in your model repo](https://huggingface.co/safe-challenge/safe-example-submission-custom-env)

2025-04-04
- New detailed public [leaderboard space](https://huggingface.co/spaces/safe-challenge/leaderboard-public)

2025-04-07
- Updated [debug example](debug_example.md) to turn off network access when running model to better reproduce submissions on HF

2025-04-08
- Provided updated information on Round 1 and Round 2 paper and poster submission processes. 


## 📊 Overview

To advance the state of the art in audio forensics, we are launching a funded evaluation challenge at [IH&MMSEC2025](https://www.ihmmsec.org) to drive innovation in detecting and attributing synthetic and manipulated audio artifacts. This challenge will focus on several critical aspects, including generalizability across diverse audio sources, robustness against evolving synthesis techniques, and computational efficiency to enable real-world applications. The rapid advancements in audio synthesis, fueled by the increasing availability of new generators and techniques, underscore the urgent need for effective solutions to authenticate audio content and combat emerging threats. Sponsored by the ULRI Digital Safety Research Institute, this initiative aims to mobilize the research community to address this pressing issue.  

Sign up here to participate and receive updates: [Google Form](https://forms.gle/5J8Yuh41Lv8GAF7w8)

## 🥇 Detailed Leaderboard
[Public Leaderboard](https://safe-challenge-leaderboard-public.hf.space)
<!--  [![leaderboard](leaderboard_latest.png)](leaderboard_latest.png) -->
<iframe
	src="https://safe-challenge-leaderboard-public.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>


## 🏆 Prize

The most promising solutions may be eligible for research grants to further advance their development. A travel stipend will be available to the highest-performing teams to support attendance at the IH&MMSEC workshop, where they can present their technical approach and results.

**All participants are required to register for the competition**

- Sign up here to participate and receive updates: [Google Form](https://forms.gle/5J8Yuh41Lv8GAF7w8)
- For info please contact: SafeChallenge2025@gmail.com
- You can also create an issue: [https://github.com/stresearch/SAFE](https://github.com/stresearch/SAFE)
- See instructions on how to submit and [🆘 Helpful Stuff](#-helpful-stuff), [debug example](debug_example.md), open issues for reference or join our [discord server](https://discord.gg/bxNsutKmTH)

## 📜 Paper Submission and Dates

All papers for this special session undergo the regular review procedure and must be submitted through the workshop paper submission system following the link given on home page: [https://www.ihmmsec.org](https://www.ihmmsec.org). For this special session in particular, authors must select the track "COMPETITION TRACK" on the submission website during the submission.

- ~~Practice Submission Opens: February 26, 2025~~
- ~~Competition Opens: March 3, 2025~~
- Round 1 Submission deadline: May 05, 2025 (the papers accepted in Round 1 will be published in the proceedings for IH&MMSEC 2025 and will be presented during the oral session of the conference)
- Round 2 Submission deadline: June 02, 2025 (performers participating in Round 1 whose algorithms score well in the system will be invited to present a poster at the IH&MMSEC workshop)

For any question regarding paper submission, please contact chairs: acm.ihmmsec25@gmail.com.

## 📝 Tasks  

The competition will consist of three detection tasks. For each task, the object is to detect if an audio file contains machine generated speech. Not all tasks will be open at the same time. 
- Practice (✅ Open): A practice task to troubleshoot model submission.
        [https://huggingface.co/spaces/safe-challenge/SAFEChallengePractice](https://huggingface.co/spaces/safe-challenge/SAFEChallengePractice)
- Task 1 (✅ Open): Detection of Generated Audio. Audio files are unmodified from the original output from the models or the pristine sources.
        [https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask1](https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask1)
- Task 2 (✅ Open): Detection of Processed Audio. Audio files will be compressed with several common audio compression codecs. The audio files will also be resampled according to several sampling rates. Only the geneated files are augmented. The pristines remain the same.
        [https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask2](https://huggingface.co/spaces/safe-challenge/SAFEChallengeTask2)
- Task 3 (❌ Closed): Bonus Task (Details TBD)


## 📈 Data

The dataset will consist of human and machine generated speech audio tracks. 

- Human generated speech will be sourced from multiple sources and in multiple languages including but not limited to high quality in-studio and lower quality in-the-wild online recordings.
- Machine generated speech will be constructed using several SOTA TTS (text-to-speech) models. The models will be either open-source or closed-source.
- The audio files will vary in length but will be no longer than 60 seconds.
- Compression formats will also vary. (See practice submission and dataset on how to load the input data)
- The dataset will be balanced across sources. Each source (source of real audio and source of generated audio) will have an equal number of samples. 
- **This competition will be fully blind.** No data will be released. Only a small sample dataset will be released as part of a sample model.
  
## 🤖 Model Submission

This is a script based competetion. No data will be released before the competition. A subset of the data may be released after the competition. We will be using [hugginface competions platform](https://github.com/huggingface/competitions).

### 📂 Create Model Repo  
Participants will be required to submit their model to be evaluated on the dataset by creating a [huggingface](https://huggingface.co/new) model repository. Please use [the example model repo](https://huggingface.co/safe-challenge/safe-example-submission) as a template.
- **The model that you submit will remain private**. No one inlcuding the challenge organizers will have access to the model repo unless you decide to make the repo public.
- The model will be expected to read in the dataset and output file containing a **detection score, binary decision and inference time** for every input example.
- The dataset will be downloaded to `/tmp/data` inside the container during the evaluation run. See example model on how to load it.
- The only requirement is to have a `script.py` in the top level of the repo that saves a `submission.csv` file with the following columns. See [sample practice submission file](sample_practice_submission.csv).
  - `id` : id of the example, strig
  - `pred` : binary decision, string, "generated" or "pristine"
  - `score`: decision score such as log likelihood score. Postive scores correspond to generated and negative to pristine. (This is optional and not used in evaluation but will help with analysis later)  
  - `time` : inference time for every example in seconds
- All submissions will be evaluated using the same resources: NVIDIA `T4-medium` GPU instance. It has 8vCPUs, 30GB RAM, 16GB VRAM.
- All submissions will be evaluated in the same container that supports common ML frameworks and libraries:
  - Dockerfile: [https://github.com/huggingface/competitions/blob/main/Dockerfile](https://github.com/huggingface/competitions/blob/main/Dockerfile)
  - Docker Image: [https://hub.docker.com/r/huggingface/competitions/tags](https://hub.docker.com/r/huggingface/competitions/tags)
  - Requirements File: [requirements.txt](requirements.txt)
  - If you'd like to add another package to the requirments file create an issue here: [https://github.com/stresearch/SAFE](https://github.com/stresearch/SAFE)
  - **During evalation, container will not have access to the internet**. Participants should include all other required dependencies in the model repo.
  - **💡 Remember: you can add anything to your model repo** like models, python packages, etc.

### 🔘 Submit  
Once your model is ready, it's time to submit:   
  - Go the task submision space (there is a seperate space for every task)
  - Login with your Huggingface Credentials
  - Teams consisting of multiple individuals should plan to submit under one Huggingface account to facilitate review and analysis results
  - Enter the name of your model e.g. `safe-challenge/safe-example-submission` and click submit! 🎉
  - Please use the same user name for all your submissions from the same team.

### 🆘 Helpful Stuff

We provide an example model submission repo and a practice competition for troubleshooting.
- Take a look at an example model repo: [https://huggingface.co/safe-challenge/safe-example-submission](https://huggingface.co/safe-challenge/safe-example-submission)
- We encourage you to submit to a practice competition: [https://huggingface.co/spaces/safe-challenge/SAFEChallengePractice](https://huggingface.co/spaces/safe-challenge/SAFEChallengePractice)
- It's using this pracice dataset: [https://huggingface.co/datasets/safe-challenge/safe-challenge-practice-dataset](https://huggingface.co/datasets/safe-challenge/safe-challenge-practice-dataset)
- 💡 To reproduce all the steps in the submission locally, take a look at the debugging example: [debug example](debug_example.md)
- You won't be able to see any detailed error if your submission fails since it's run in a private space. *You can open a ticket or email us with your submission id, and we can look up the logs.* The easiest way is to trouble shoot locally using the above example.
- *🔥New* [Example on including a custom environment in your model repo](https://huggingface.co/safe-challenge/safe-example-submission-custom-env)

## 🔍 Evaluation

All submissions will be evalulated using balanced accuracy. Balanced accuracy is defined as an average of true positive rate and true negative rate. 

The competition page will maintain a public leaderboard and a private leaderboard. The data will be devided along the sources such that public leaderboard will be a subset of the private leaderboard. Public leaderboard will also show error rates for every source, However, the specific source name will be anonymized. For example, public leaderboard will show scores for 4 sources while the private leaderboard will be score on additional 4 sources for 8 sources total. See the following table as an example.

<img width="1572" alt="image" src="https://github.com/user-attachments/assets/ec4339ef-589b-4f76-ae2f-a03a6ed6d7d3" />

- After the competition closes, we will provide additional metrics broken down by source and other data attributes.
- This is why we ask you to provide a continous decision score for every input example in addition to a hard binary decision.

## ⚖️ Rules

To ensure a fair and rigorous evaluation process for the SAFE: Synthetic Audio Forensics Evaluation Challenge (SAFE), the following rules must be adhered to by all participants:

1. **Leaderboard**:
   - The competition will maintain both a public and a private leaderboard.
   - The public leaderboard will show error rates for each anonymized source.
   - The private leaderboard will be used for the final evaluation and will include non-overlapping data from the public leaderboard.

2. **Submission Limits**:
   - Participants will be limited in submissions per day.

3. **Confidentiality**:
   - Participants agree not to publicly compare their results with those of other participants until the other participant’s results are published outside of the IH&MMSEC2025 venue.
   - Participants are free to use and publish their own results independently.

4. **Compliance**:
   - Participants must comply with all rules and guidelines provided by the organizers.
   - Failure to comply with the rules may result in disqualification from the competition and exclusion from future evaluations.

By participating in the SAFE challenge, you agree to adhere to these evaluation rules and contribute to the collaborative effort to advance the field of audio forensics.
