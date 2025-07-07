import streamlit as st

# Set page config
st.set_page_config(page_title="AI Packaging Generator", layout="centered")

# Page title
st.title("📦 AI Packaging Generator")
st.subheader("Enter your product specs to receive a packaging recommendation.")

# Input fields with unique keys
length = st.number_input("Product Length (in)", min_value=0.0, value=6.0, key="length")
width = st.number_input("Product Width (in)", min_value=0.0, value=4.0, key="width")
height = st.number_input("Product Height (in)", min_value=0.0, value=3.0, key="height")
fragility = st.selectbox("Fragility Level", ["low", "medium", "high"], key="fragility")
channel = st.selectbox("Sales Channel", ["e-commerce", "retail"], key="channel")

# Logic to generate recommendation
def product_to_pack(length, width, height, fragility, channel):
    packaging_type = "RSC Box" if max(length, width, height) < 18 else "Custom Die-Cut"
    if fragility == "high":
        insert = "Foam Insert"
    elif fragility == "medium":
        insert = "Corrugated Insert"
    else:
        insert = "None"

    eco_score = "🌿 High" if packaging_type == "RSC Box" and insert == "None" else "♻️ Medium"
    return {
        "Recommended Packaging": packaging_type,
        "Insert Type": insert,
        "Eco Score": eco_score,
        "Estimated Outer Dimensions (in)": f"{length+2} x {width+2} x {height+2}"
    }

# Generate button
if st.button("Generate Recommendation", key="generate_btn"):
    result = product_to_pack(length, width, height, fragility, channel)
    st.markdown("---")
    st.success("✅ Recommendation Generated!")
    for k, v in result.items():
        st.write(f"**{k}:** {v}")
