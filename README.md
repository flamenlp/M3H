# AxiOM & M3H: Figurative and Commonsense Mental Health Meme Classification

This repository contains the **AxiOM** and **RESTORE** datasets along with the implementation of the **M3H** framework, as proposed in our WWW’25 paper:

📄 **Paper**: [Figurative-cum-Commonsense Knowledge Infusion for Multimodal Mental Health Meme Classification](https://arxiv.org/abs/2501.15321)  
📅 **Conference**: The Web Conference (WWW), 2025  

---
## To get the access to the M3H Dataset, kindly fill the google form given below:
Google Form: https://forms.gle/9hGoVRLzuHXJyVrN6

## 📊 Dataset Statistics

### 🧠 AxiOM (Anxiety Meme Dataset)
- **Total memes**: 3,582
- **Task**: Multiclass classification
- **Label categories** (based on GAD-7 symptoms):
  - `NV`: Nervousness  
  - `LWC`: Lack of Worry Control  
  - `EW`: Excessive Worry  
  - `DR`: Difficulty Relaxing  
  - `RST`: Restlessness  
  - `ID`: Impending Doom  

---

### 🧩 RESTORE (Depression Meme Dataset)
- **Total memes**: 7,396  
- **Task**: Multilabel classification  
- **Label categories** (based on PHQ-9, excluding "Lack of Energy"):
  - `LOI`: Lack of Interest  
  - `FD`: Feeling Down  
  - `ED`: Eating Disorder  
  - `SD`: Sleeping Disorder  
  - `CP`: Concentration Problem  
  - `LSE`: Low Self-Esteem  
  - `SH`: Self-Harm  

---

## If you use the Our dataset, please cite:


```bibtex
Axiom Dataset Citation (Anxiety)

@article{mazhar2025figurative,
  title={Figurative-cum-Commonsense Knowledge Infusion for Multimodal Mental Health Meme Classification},
  author={Mazhar, Abdullah and Srivastava, Aseem and Ruhnke, Polly and Vaddavalli, Lavanya and Katragadda, Sri Keshav and Yadav, Shweta and Akhtar, Md Shad and others},
  journal={arXiv preprint arXiv:2501.15321},
  year={2025}
}
```
```bibtex
Restore Dataset Citation (Depressive)

@inproceedings{yadav2023towards,
  title={Towards identifying fine-grained depression symptoms from memes},
  author={Yadav, Shweta and Caragea, Cornelia and Zhao, Chenye and Kumari, Naincy and Solberg, Marvin and Sharma, Tanmay},
  booktitle={Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={8890--8905},
  year={2023}
}
```


