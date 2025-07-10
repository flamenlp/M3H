# M3H-Dataset: Figurative and Commonsense Mental Health Meme Dataset

This repository contains two curated datasets used in our [WWW'25](https://arxiv.org/abs/2501.15321) paper:

- **AxiOM** (Anxiety Meme Dataset)
- **RESTORE** (Depression Meme Dataset)

These datasets support multimodal research on mental health memes by providing:
- Visual data (memes)
- OCR-extracted text
- Commonsense reasoning triples
- Annotated labels

---

## Download Instructions

### Anxiety Dataset (AxiOM)

**Image Folders**
- Train: `M3H-Dataset/anxiety_final/anxiety_train_image`
- Test: `M3H-Dataset/anxiety_final/anxiety_test_image`

**Metadata CSVs (use these commands in terminal):**
```bash
# Train CSV
wget https://raw.githubusercontent.com/flamenlp/M3H/main/M3H-Dataset/anxiety_final/anxiety_train_gpt_new.csv -O anxiety_train_gpt_new.csv

# Test CSV
wget https://raw.githubusercontent.com/flamenlp/M3H/main/M3H-Dataset/anxiety_final/anxiety_test_gpt_new.csv -O anxiety_test_gpt_new.cs
```
### Depression Dataset (RESTORE)

**Image Folders**
All images: M3H-Dataset/Depressive_Data/Images

**Metadata CSVs (use these commands in terminal):**
```bash
# Train JSON
wget https://raw.githubusercontent.com/flamenlp/M3H/main/M3H-Dataset/Depressive_Data/train.json -O train.json

# Validation JSON
wget https://raw.githubusercontent.com/flamenlp/M3H/main/M3H-Dataset/Depressive_Data/val.json -O val.json

