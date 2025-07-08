# AxiOM & M3H: Figurative and Commonsense Mental Health Meme Classification

This repository contains the implementation of **M3H**, a framework proposed in the paper:

**“Figurative-cum-Commonsense Knowledge Infusion for Multimodal Mental Health Meme Classification”**  
📄 [Read the Paper](https://arxiv.org/abs/2501.15321)  
📅 Presented at: *The Web Conference (WWW) 2025*

---

## Overview

M3H is a multimodal framework designed to classify mental health symptoms expressed in memes. It infuses commonsense and figurative reasoning into the model pipeline using a combination of visual features, OCR-extracted text, and knowledge triples.

---

## Repository Structure

The project consists of three core notebooks:

### 1. `get_embeddings.ipynb`

- Loads training and testing datasets.
- Extracts features from meme text (OCR) and commonsense triples.
- Generates embeddings using a SentenceTransformer.
- Saves outputs into `.pt` files:
  - `train_ocr.pt`, `test_ocr.pt`
  - `train_triplet.pt`, `test_triplet.pt`

### 2. `get_top_k.ipynb`

- Loads the `.pt` embedding files.
- Uses cosine similarity (via `filter.py`) to find top-K similar examples for each input.
- Saves the retrieved indices as a DataFrame in a `.csv` file.

### 3. `main.ipynb`

- Loads the retrieved meme indices.
- Formats the data into prompts combining:
  - OCR text  
  - Figurative reasoning  
  - Retrieved similar examples
- Feeds the prompts into a classification model for inference.

---

## Classification Tasks

The framework supports two datasets and task settings:

### Anxiety (AxiOM Dataset)
- **Type**: Multiclass, Single-label Classification  
- **Loss Function**: `CrossEntropyLoss`

### Depression (RESTORE Dataset)
- **Type**: Multiclass, Multi-label Classification  
- **Loss Function**: `BCEWithLogitsLoss`

---

##  Execution Order

Follow this order for proper pipeline execution:

```bash
1. Run get_embeddings.ipynb    # Generate OCR + triple embeddings
2. Run get_top_k.ipynb         # Retrieve Top-K similar examples using cosine similarity
3. Run main.ipynb              # Prompt construction + model inference/classification
