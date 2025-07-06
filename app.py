import streamlit as st

def product_to_pack(length, width, height, fragility, channel):
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

    return {
        "Box Length": round(box_l, 2),
        "Box Width": round(box_w, 2),
        "Box Height": round(box_h, 2),
        "Style": style,
        "Material": material,
    }

st.set_page_config(page_title="AI Packaging Generator")

st.title("📦 AI Packaging Generator")
st.write("Enter your product specs to receive a packaging recommendation.")

length = st.number_input("Product Length (in)", min_value=0.0, value=6.0)
width = st.number_input("Product Width (in)", min_value=0.0, value=4.0)
height = st.number_input("Product Height (in)", min_value=0.0, value=3.0)
fragility = st.selectbox("Fragility Level", ["low", "medium", "high"])
channel = st.selectbox("Sales Channel", ["e-commerce", "retail"])

if st.button("Generate Recommendation"):
    result = product_to_pack(length, width, height, fragility, channel)
    st.subheader("📋 Recommendation:")
    for key, value in result.items():
        st.write(f"**{key}**: {value}")

