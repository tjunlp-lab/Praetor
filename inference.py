from transformers import AutoModelForCausalLM, AutoTokenizer
import vllm
import torch

def vllm_inference(model, sampling_params, tokenizer, prompts):
    new_prompts = []
    for prompt in prompts:
        messages = [
            {"role": "user", "content": prompt}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        new_prompts.append(text)

    pred_list = model.generate(new_prompts, sampling_params)
    pred_list = [it.outputs[0].text.strip() for it in pred_list]
    return pred_list


model_path = ''     # Praetor_model_path
model = vllm.LLM(model=model_path, tensor_parallel_size=1, dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(model_path)
sampling_params = vllm.SamplingParams(
    repetition_penalty=1.05,
    temperature=0,
    top_p=0.8,
    top_k=20,
    max_tokens=2048
)

prompts = []    # prompt
result = vllm_inference(model, sampling_params, tokenizer, prompts)