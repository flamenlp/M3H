import torch
from datasets import load_dataset
import torch.nn.functional as F
import pandas as pd

class get_filtered():
    def __init__(self, train_path=None, desc_train_array=None, ocr_train_array=None, variable=None):
        # if variable[0][0]:
        self.variable = variable
        if train_path:
            train_df = pd.read_json(train_path)
        if desc_train_array:
            self.descriptions = train_df['Description']
            self.descriptions_array = torch.load(desc_train_array)
        if ocr_train_array:
            self.ocrs = train_df['ocr_text']
            self.ocrs_array = torch.load(ocr_train_array)
            
    def get_filter_desc(self, input_tensor, top_k=1, return_text=False):
            cosine_similarities = []
            
            for tensor in self.descriptions_array:
                cosine_sim = F.cosine_similarity(input_tensor.unsqueeze(0), tensor.unsqueeze(0))
                cosine_similarities.append(cosine_sim.item())
            
            top_k_indices = sorted(range(len(cosine_similarities)), key=lambda i: cosine_similarities[i], reverse=True)[:top_k]
            
            if return_text==True:
                return (top_k_indices, [self.descriptions[n] for n in top_k_indices])
            return top_k_indices

    def get_filter_ocr_desc(self, input_tensor, top_k_tuple=(10,2), return_text=False):
            #stage 1 filter using ocr_texts
            top_k= top_k_tuple[0]
            cosine_similarities = []
            for tensor in self.ocrs_array:
                cosine_sim = F.cosine_similarity(input_tensor.unsqueeze(0), tensor.unsqueeze(0))
                cosine_similarities.append(cosine_sim.item())
            
            top_k_indices = sorted(range(len(cosine_similarities)), key=lambda i: cosine_similarities[i], reverse=True)[:top_k]

            #stage 2 filter using descriptions
            top_k= top_k_tuple[1]
            cosine_similarities = []
            
            filtered_descripions = [self.descriptions_array[n] for n in top_k_indices]
            for tensor in self.filtered_descripions:
                cosine_sim = F.cosine_similarity(input_tensor.unsqueeze(0), tensor.unsqueeze(0))
                cosine_similarities.append(cosine_sim.item())
            
            top_k_indices = sorted(range(len(cosine_similarities)), key=lambda i: cosine_similarities[i], reverse=True)[:top_k]
            
            if return_text==True:
                return (top_k_indices, [self.descriptions[n] for n in top_k_indices])
            return top_k_indices
    def get_filter_variable(self, input_tensor, top_k=1, return_text=False):
        cosine_similarities = []
        
        for tensor in self.variable:
            cosine_sim = F.cosine_similarity(tensor.unsqueeze(0), input_tensor.unsqueeze(0), dim=1)
            cosine_similarities.append(cosine_sim.item())  # Use `.item()` for scalar extraction when dim=1

        # Get indices of top_k highest cosine similarities
        top_k_indices = sorted(range(len(cosine_similarities)), key=lambda i: cosine_similarities[i], reverse=True)[:top_k]
        
        if return_text:
            return (top_k_indices, [self.variable[n] for n in top_k_indices])
        return top_k_indices
