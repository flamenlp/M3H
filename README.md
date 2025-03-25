# M3H

Overview

This project proposes a model that consists of three primary files:

1. get_embeddings.ipynb

This is the first file that needs to be executed.

It loads both the train and test datasets.

Preprocessing is performed to extract useful features.

Embeddings are generated for OCR text and triples (Common Sense Reasoning) using a sentence transformer.

The embeddings are stored in four .pt files.

2. get_top_k.ipynb

This script identifies the top K most relevant examples for a given meme.

It loads the .pt files generated in get_embeddings.ipynb.

Calls filter.py, which uses cosine similarity to find examples similar to the current input.

Outputs a final CSV file containing indices of memes similar to each input, stored in a DataFrame.

3. main.ipynb

Loads the final DataFrame generated in get_top_k.ipynb.

Formats the data into prompts.

Passes the prompts to the backbone model for final processing.

Classification Tasks

The model is designed to handle two types of classification problems:

1. Anxiety Data

Multiclass Single Label Classification

The model predicts a single category for each input.

2. Depressive Data

Multiclass Multi-Label Classification

The model predicts multiple categories for each input.

Implementation Considerations

The only modification required in the training loop is how the loss is computed:

For single-label classification, the model outputs a single class, and the loss function should be appropriate for this task (e.g., CrossEntropyLoss).

For multi-label classification, the model outputs multiple labels, and the loss function should be suitable for this task (e.g., BCEWithLogitsLoss).

Execution Order

Run get_embeddings.ipynb to generate embeddings.

Run get_top_k.ipynb to find similar memes.

Run main.ipynb to process the final dataset and pass it to the model.

Ensure that the appropriate classification method is applied based on the dataset being used.
