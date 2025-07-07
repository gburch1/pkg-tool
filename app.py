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
    padding_lookup = {"low": 0.25, "medium": 0.5, "high": 0.75}
    padding = padding_lookup[fragility]
    
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

    result = {
        "Box Style": style,
        "Material": material,
        "Box Dimensions (in)": f"{round(box_l, 2)} x {round(box_w, 2)} x {round(box_h, 2)}",
        "Eco Score": eco_score
    }

    if include_dunnage:
        if fragility == "high":
            dunnage_type = "Foam inserts or air pillows"
        elif fragility == "medium":
            dunnage_type = "Paper fill or molded pulp"
        else:
            dunnage_type = "Kraft paper or bubble wrap"
        
        result["Dunnage Type"] = dunnage_type
        result["Dunnage Dimensions"] = (
            f"Top & Bottom Pads: {round(length + padding, 2)}\" x {round(width + padding, 2)}\" x {round(padding, 2)}\""
        )
    else:
        result["Dunnage Type"] = "Not included"
        result["Dunnage Dimensions"] = "N/A"

    return result, style

# Action
if st.button("Generate Recommendation", key="generate_btn"):
    result, style = product_to_pack(length, width, height, fragility, channel, include_dunnage)
    st.markdown("---")
    st.success("✅ Packaging Recommendation Generated!")
    
    for k, v in result.items():
        st.write(f"**{k}:** {v}")

    # Image preview
    st.subheader("📦 Box Style Preview")
    if style == "Mailer Box (Roll-End Tuck Top)":
        st.image("https://i.imgur.com/EVuwgKF.png", caption="Mailer Box (RETT)", use_column_width=True)
    elif style == "Regular Slotted Container (RSC)":
        st.image("https://i.imgur.com/nz3S45b.png", caption="RSC Box", use_column_width=True)
