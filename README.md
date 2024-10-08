# MMORPG Asset Generator

This project aims to fine-tune image generation models based on MMORPG game assets to create a tool for generating unique game assets and skills. It has been specifically used to generate character profile pictures and skin items for in-game use.

## Project Components

1. Dataset Creation and Upload
2. Model Fine-tuning
3. Image Generation
4. API System for Inference

## Dataset

A custom dataset of MMORPG assets has been created and uploaded to the Hugging Face Hub as a private dataset:

Dataset Name: Tomd7/charactergen-private

This dataset contains high-quality MMORPG asset images with detailed prompts for advanced fine-tuning of image generation models.

## Fine-tuned Models

Multiple models have been fine-tuned on the custom dataset:

1. Stable Diffusion XL: 
   Model Name: Tomd7/mmorpg_asset_model_improved

2. Additional fine-tuned models (not present in this repository)

These models have been optimized for different aspects of MMORPG asset generation.

## Usage

1. Dataset Creation: Run the dataset creation script to process your images and upload them to Hugging Face.
2. Model Fine-tuning: Use the fine-tuning script to train the Stable Diffusion XL model on your dataset.
3. Image Generation: Utilize the image generation script to create new MMORPG assets using the fine-tuned models.

## API System

An API system has been developed to enable inference calls from the game's website to a GPU-equipped machine. This allows for real-time asset generation within the game environment.

## Purpose

The main goal of this project is to build a tool that can create unique assets and skills for MMORPG games. By fine-tuning image generation models on existing game assets, we can produce new, creative designs that fit seamlessly into the game's aesthetic.

This tool can be invaluable for game developers and designers, allowing them to quickly generate ideas for new items, characters, or abilities, streamlining the asset creation process and fostering creativity in game development.

## Specific Applications

This project has been successfully used to generate:

1. Character profile pictures: Creating unique avatars for players in the game.
2. Skin items: Generating new cosmetic items and character skins to enhance player customization options.

These applications demonstrate the versatility of the models in creating both character-centric and item-based assets for MMORPG environments.

The integration of the API system allows for dynamic asset generation, enhancing the game's ability to provide unique, on-demand content to players.