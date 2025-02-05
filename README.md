# [WIP] SAFE: Synthetic Audio Forensics Evaluation Challenge. 

## Overview

To advance the state of the art in audio forensics, we are launching a funded evaluation challenge at [IHM&MSEC2025](https://www.ihmmsec.org/cms/home/index.html) to drive innovation in detecting and attributing synthetic and manipulated audio artifacts. This challenge will focus on several critical aspects, including generalizability across diverse audio sources, robustness against evolving synthesis techniques, and computational efficiency to enable real-world applications. The rapid advancements in audio synthesis, fueled by the increasing availability of new generators and techniques, underscore the urgent need for effective solutions to authenticate audio content and combat emerging threats. Sponsored by the ULRI Digital Safety Research Institute, this initiative aims to mobilize the research community to address this pressing issue. The most promising solutions will be eligible for research grants to further advance their development. 

Sign up to receive updates [here]().

For info please contact: safe-challenge@domain.com

## Import Dates

- Competition Opens: February 24, 2025
- Round 1 Submission deadline: May 05, 2025 (the papers accepted in Round 1 will be published in the proceedings)
- Round 2 Submission deadline: June 02, 2025 (competition will close after Round 2)

## Data

The dataset will consists of human and machine generated speech audio tracks. 

- Human generated speech will be sources from multiple sources inlcuding but not limited to high quality in-studio and lower quality in-the-wild online recordings.
- Machine generated speech will be constructed using several  SOTA TTS (text to speech) models. The models will be either open-source or closed-source.
- The audio files will vary in length but no longer than 60 seconds
- Compression formats will also vary but the files will be saved as WAVs to simplify reading.
- The dataset will be balanced across sources. Each source (source of real audio and source of generated audio) will have equal number of samples. 
- **This competition will be fully blind.** No data will be released. Only a small sample dataset will be released as part of a sample model.
  
## Tasks  

The competition will consist of three detection task. For each task, the object is to detect if an audio file contains machine generated speech. Not all tasks will be

- Task 1: Detection on Raw Audio. Audio files are unmodified from the original output from the models or the pristine sources.
- Task 2: Detection on Processed Audio. Audio files will be compressed with several common audio compression codecs. The audio files will also be resampled according to several sampling rates.
- Task 3: Bonus Task (Details TBD)

## Model Submission

This is a code based competetion. No data is released. 

** Details on the submission process and the sample model submission will be posted soon. **

- Participants will be required to submit their model to be evaluated on the dataset.
- The model will be expected to read in the dataset and output file containing a **detection score and binary decision** for every input example.
- Common python ML frameworks like pytorch, onnx, etc will be supported.

## Evaluation

All submissions will be evalulated using balanced accuracy. Balanced accuracy is defined as an average of true positive rate and true negative rate. 

- After the competion closes, we'll provide additiona metrics broken down by source and other data attributes.
- This is why we ask you to provide a continous decision score for every input example in addition to a hard binary decision.

