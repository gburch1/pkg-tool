import streamlit as st

st.set_page_config(page_title="AI Packaging Generator", layout="centered")

st.title("📦 AI Packaging Generator")
st.subheader("Enter your product specs to receive a packaging recommendation.")

# Inputs
length = st.number_input("Product Length (in)", min_value=0.0, value=6.0, key="length")
width = st.number_input("Product Width (in)", min_value=0.0, value=4.0, key="width")
height = st.number_input("Product Height (in)", min_value=0.0, value=3.0, key="height")
fragility = st.selectbox("Fragility Level", ["low", "medium", "high"], key="fragility")
channel = st.selectbox("Sales Channel", ["e-commerce", "retail"], key="channel")
include_dunnage = st.checkbox("Include Dunnage Recommendation", key="dunnage")

# Logic
def product_to_pack(length, width, height, fragility, channel, include_dunnage):
    padding = {"low": 0.25, "medium": 0.5, "high": 0.75}[fragility]
    box_l = length + 2 * padding
    box_w = width + 2 * padding
    box_h = height + 2 * padding

    style = "Mailer Box (Roll-End Tuck Top)" if channel == "e-commerce" else "Regular Slotted Container (RSC)"
    material = (
        "Double-wall corrugated" if fragility == "high"
        else "32 ECT single-wall" if fragility == "medium"
        else "Kraft chipboard"
    )
    eco_score = "🌿 High" if material == "Kraft chipboard" else "♻️ Medium"

    # Dunnage logic
    dunnage = None
    if include_dunnage:
        if fragility == "high":
            dunnage = "Foam inserts or air pillows"
        elif fragility == "medium":
            dunnage = "Paper fill or molded pulp"
        else:
            dunnage = "Kraft paper or bubble wrap"

    return {
        "Box Style": style,
        "Material": material,
        "Box Dimensions (in)": f"{round(box_l, 2)} x {round(box_w, 2)} x {round(box_h, 2)}",
        "Eco Score": eco_score,
        "Dunnage Recommendation": dunnage if include_dunnage else "Not included"
    }

# Action
if st.button("Generate Recommendation", key="generate_btn"):
    result = product_to_pack(length, width, height, fragility, channel, include_dunnage)
    st.markdown("---")
    st.success("✅ Packaging Recommendation Generated!")
    for k, v in result.items():
        st.write(f"**{k}:** {v}")
