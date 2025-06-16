from PIL import Image
from models.caption_model import generate_caption
from models.detection_model import detect_objects

import re

def clean_caption(caption: str) -> list[str]:
    """
    Extract possible ingredient-like words from caption using basic keyword filtering.
    """
    # Remove punctuation
    caption = re.sub(r"[^\w\s]", "", caption.lower())
    words = caption.split()

    # Basic filter: keep only alphabetic and reasonably long tokens
    return [word for word in words if word.isalpha() and len(word) > 2]

def merge_ingredients(caption_words: list[str], detected_objects: list[str]) -> list[str]:
    combined = caption_words + detected_objects
    return sorted(set([item.strip().lower() for item in combined]))

def extract_ingredients(image: Image.Image) -> list[str]:
    caption = generate_caption(image)
    print(f"📝 Caption: {caption}")

    caption_keywords = clean_caption(caption)
    print(f"🔍 Caption Keywords: {caption_keywords}")

    detected_objects = detect_objects(image)
    print(f"📦 Detected Objects: {detected_objects}")

    ingredients = merge_ingredients(caption_keywords, detected_objects)
    print(f"✅ Final Ingredients: {ingredients}")

    return ingredients
