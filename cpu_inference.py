import torch
from diffusers import DiffusionPipeline, AutoencoderKL
import time
from huggingface_hub import login


# Load the base model and VAE
vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float32)
pipeline = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    vae=vae,
    torch_dtype=torch.float32,
    use_safetensors=True
)

# Load your fine-tuned LoRA weights
pipeline.load_lora_weights("Tomd7/mmorpg_asset_model_improved")

# Move the pipeline to CPU
pipeline = pipeline.to("cpu")

# Test prompts
test_prompts = [
    "a highly detailed MMORPG asset of a magical sword with intricate engravings, glowing runes, and a gem-encrusted hilt, 4k resolution, cinematic lighting",
    "an MMORPG asset of a mystical staff with swirling energy patterns, ornate carvings, and floating crystals, 4k resolution, game art style",
    "an MMORPG asset of an enchanted armor set with glowing sigils, ethereal aura, and intricate metalwork, 4k resolution, fantasy game design"
]

# Function to generate image and measure time
def generate_image(prompt, num_inference_steps=50):
    start_time = time.time()
    image = pipeline(prompt=prompt, num_inference_steps=num_inference_steps).images[0]
    end_time = time.time()
    return image, end_time - start_time

# Generate images and print timing information
for i, prompt in enumerate(test_prompts):
    print(f"Generating image {i+1}...")
    image, generation_time = generate_image(prompt)
    print(f"Image {i+1} generated in {generation_time:.2f} seconds")
    image.save(f"generated_image_{i+1}.png")
    print(f"Image saved as generated_image_{i+1}.png")
    print()

print("All images generated!")