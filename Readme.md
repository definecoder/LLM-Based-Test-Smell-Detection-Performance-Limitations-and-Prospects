# Datasets:

## All datasets and evaluation Results

- All datasets and Evaluation Results are available in the Google Drive. To access the datasets and results: [Click Here](https://drive.google.com/drive/folders/118jruNqK02wO70D1wht2tEvRRF5P9U2h?usp=sharing)

## Raw Dataset Sheet links:

- **GIT RAW LINK SCRAPED DATASET**: [Click Here](https://docs.google.com/spreadsheets/d/1jw7_nFlQjdaiPj1q1ExzccAfgv5BHZJ61OiKlKVoq1w/edit?usp=sharing)

- **TSDetect Labeled Dataset**: [Click Here](https://docs.google.com/spreadsheets/d/1iFYwOpNd8uun2cNhAd5dqq4a3AiQXj9VREMOj23yi7A/edit?usp=sharing)

- **TsDetect + Gemini Natural Language Labeled Dataset**: [Click Here](https://docs.google.com/spreadsheets/d/1qS_3bNU_SsHtJAc8-i1E_4frO6l8Kn3RCWEUKlbvqok/edit?usp=sharing)

## Dataset Published in Hugging face for Fine Tuning LLM for Test Smell Detection

- TS Detect + Gemini Explained Dataset: [Click Here](https://huggingface.co/datasets/shawon-majid/ts-detect-test-smell-gemini-explained)

- Human Labeled Dataset for only 4 test smells: [Click Here](https://huggingface.co/datasets/shawon-majid/codes-for-test-smells)

## Evaluations:

- **Evaluation Results**: [Click Here](https://docs.google.com/spreadsheets/d/1AVjW2OF86z3tmKSiFJ-PjDpcb11kIOSFlXP9o3a75h0/edit?usp=sharing)

# Fine Tuned Model

Our Fine Tuned Model is available at Hugging Face Model Hub. You can use it for your own test smell detection task. Click here to access the model: [Click Here](https://huggingface.co/shawon-majid/llama-3-8B-Instruct-test-smell-detection-raw)

# Code Links:

## Code extractor script from GitHub

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/github_code_extractor/data_scraper.py)

## Raw file extractor script

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/github_code_extractor/raw_file_extractor.py)

## Default Branch Mapper

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/github_code_extractor/github_branch.py)

## Test Code Parser From Git Raw Link CSV:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/app.py)

## Initial Test Smell Cleaning and Preprocessing:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/smell-clean/cleaner.py)

## Test Code - Production Code Downloading Script:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/code-test-pair-for-tsDetect/code-test-file-downloader.py)

## CSV Formatter for TsDetect:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/code-test-pair-for-tsDetect/tsDetectCSVmaker.py)

## LLM Friendly Dataset Generator:

### Helpers:

- [CSV Splitter](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/llmFriendlyDataset/splitCSV.py)
- [CSV Combiner](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/llmFriendlyDataset/combine_csv.py)

### LLM Friendly Dataset Generator:

[Click here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/llmFriendlyDataset/llmFriendlyDatasetMaker.py)

## Fine Tuning Notebooks:

1. Fine tuning with only labeled data for four test smell using unsloth: click [here](./fine-tune-notebooks/0_Fine_Tuning_with_Labeled_Data_using_unsloth.ipynb)

2. Fine tuning with tsDetect Generated gemini explained dataset using unsloth: click [here](./fine-tune-notebooks/1_finetuning_with_explained_data_using_unsloth.ipynb)

3. Raw Fine tuning with tsDetect Generated gemini explained dataset: click [here](./fine-tune-notebooks/2_fine_tuning_llama_3_llm_for_test_smell_detection.ipynb)

## Evaluation:

### Helpers:

- [Groq Agent](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/groqAgent.py)
- [huggingFace Agent](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/huggingFaceAgent.py)
- [HuggingFace Middleware (Serializer)](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/huggingFaceMiddleware.py)
- [Manual Model Loader](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/manualHuggingFace.py)
- [Finetuned Model Evaluator](https://colab.research.google.com/drive/1RXyYLsA3MSkyedHin0iVlLoeMVuBCdxx?usp=sharing)
- [TP, FP, TN, FN Calculator](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/tptnfpfn_calculator.py)

### GPT & Claude Agent:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/agent.py)

### Overall Evaluator:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/langchainGenericSmellDetector/evaluator_better.py)

### Evaluation Results:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/tree/main/langchainGenericSmellDetector/result)

## Mixtral Of Agent(MOA) Architecture:

[Click Here](https://github.com/definecoder/LLM-Based-Test-Smell-Detection-Performance-Limitations-and-Prospects/blob/main/MOA_AGENT/moa.ipynb)
