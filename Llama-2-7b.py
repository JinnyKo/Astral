from transformers import LlamaTokenizer, LlamaForCausalLM
import torch
import tensorflow as tf

api_token = "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"

# 토큰 설정
from huggingface_hub import HfApi, HfFolder
HfFolder.save_token(api_token)
#model load 
tokenizer = LlamaTokenizer.from_pretrained("meta-llama/LLaMA-2-7B-hf")
model = LlamaForCausalLM.from_pretrained("meta-llama/LLaMA-2-7B-hf")
model.eval() 