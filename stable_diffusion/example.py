
# https://huggingface.co/models?pipeline_tag=text-to-image&p=3&sort=trending

# Packages
import torch
from diffusers import StableDiffusionPipeline


# Model to generate with
models = [
    "dreamlike-art/dreamlike-anime-1.0",
    "dreamlike-art/dreamlike-photoreal-2.0",
    "dreamlike-art/dreamlike-diffusion-1.0",
]
# Prompts
prompts = {
    "a":"An onimous apple tree. Impressionist style.",
    "b":"An ominous apple tree. Anime style. Black and white.",
    "c":"A subtley ominous apple tree, looming over a couple. Graphic novel noir style.",
    "d":"A group of cartoon animals in a forest. Adult colouring book style."
}


model = 0

for model_id in models:
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    for i, prompt in prompts.items():
        image = pipe(prompt).images[0]
        image.save(f'images/result_{model}_{i}.jpg')

    model+=1