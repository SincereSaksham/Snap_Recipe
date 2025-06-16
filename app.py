import streamlit as st
from PIL import Image
from backend.image_processing import extract_ingredients
from backend.recipe_generator import generate_recipe

st.set_page_config(page_title="RecipeSnap 🍳", layout="centered")

st.title("📸 RecipeSnap - AI Cooking Assistant")
st.markdown("Upload a picture of your fridge, and we'll generate recipes using the visible ingredients!")

uploaded_file = st.file_uploader("📂 Upload a fridge photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Analyzing image and detecting ingredients..."):
        ingredients = extract_ingredients(image)

    if ingredients:
        st.success("🧠 Ingredients Identified:")
        st.write(", ".join(ingredients))

        with st.spinner("🍳 Generating recipes with TinyLlama..."):
            recipe = generate_recipe(ingredients)

        st.markdown("## 🍲 Suggested Recipes")
        st.markdown(recipe)
    else:
        st.warning("⚠️ Could not identify any ingredients. Try another image.")
