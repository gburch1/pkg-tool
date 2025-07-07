import streamlit as st

# Title and instructions
st.title("📦 AI-Powered Packaging Generator")
st.subheader("Enter your product specs to receive a packaging recommendation.")

# --- PRODUCT DIMENSIONS ---
st.header("📐 Product Dimensions")
length = st.number_input("Product Length (in)", min_value=0.0, value=6.0, key="prod_len")
width = st.number_input("Product Width (in)", min_value=0.0, value=4.0, key="prod_wid")
height = st.number_input("Product Height (in)", min_value=0.0, value=2.0, key="prod_hei")

# --- PACKAGING STYLE SELECTION ---
st.header("📦 Packaging Style")
box_style = st.selectbox("Choose a box style", ["Mailer (RETT)", "RSC Box"], key="box_style")

# --- DUNNAGE OPTION ---
st.header("🧊 Dunnage Options")
use_dunnage = st.checkbox("Include dunnage (padding)?", key="dunnage")

if use_dunnage:
    dunnage_top = st.number_input("Top/Bottom Padding (in)", min_value=0.0, value=0.25, key="dun_top")
    dunnage_sides = st.number_input("Side Padding (in)", min_value=0.0, value=0.25, key="dun_side")
else:
    dunnage_top = 0
    dunnage_sides = 0

# --- CALCULATE BOX DIMENSIONS ---
st.header("📦 Recommended Box Dimensions")

box_length = length + (2 * dunnage_sides)
box_width = width + (2 * dunnage_sides)
box_height = height + (2 * dunnage_top)

st.markdown(f"**Box Size:** `{round(box_length, 2)} in x {round(box_width, 2)} in x {round(box_height, 2)} in`")

# --- PREVIEW BOX STYLE IMAGE ---
st.header("🖼️ Box Style Preview")

if box_style == "Mailer (RETT)":
    st.image(
        "https://raw.githubusercontent.com/openpackaging/ai-box-images/main/mailer-box.png",
        caption="Mailer Box (RETT)",
        use_container_width=True
    )
else:
    st.image(
        "https://raw.githubusercontent.com/openpackaging/ai-box-images/main/rsc-box.png",
        caption="RSC Box",
        use_container_width=True
    )

# --- FOOTER ---
st.markdown("---")
st.markdown("🔁 Adjust dimensions to explore different packaging fits. More features coming soon!")

