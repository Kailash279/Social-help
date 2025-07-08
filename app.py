import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="HelpXpress", layout="centered")

# Sidebar Navigation
page = st.sidebar.selectbox("Navigate", ["🏠 Home", "📦 Send Parcel", "🧳 Post Travel", "📍 Live Map", "🔗 Matches"])

# -------------------- Page: Home --------------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🚀 Welcome to HelpXpress</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>A trusted community for urgent parcel delivery using the help of nearby travelers.</p>", unsafe_allow_html=True)

    st.markdown("---")
       
    st.markdown("### 📘 About")
    st.markdown("""
    <p style='text-align: justify; font-size: 16px;'>
        <strong>HelpXpress</strong> is a community-driven platform that enables individuals to help each other by 
        delivering urgent parcels during their own travel. The idea is to create a network of trust where people can 
        share resources, reduce delivery delays, and make logistics more human and social. Kailash Kothari.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("### 🙏 Acknowledgment")
    st.markdown("""
    <p style='text-align: justify; font-size: 16px;'>
        We thank all open-source contributors, community supporters, and early users of HelpXpress who made this initiative possible.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3602/3602123.png", width=150)
        st.subheader("📦 Send a Parcel")
        st.write("Easily create a delivery request and get help from people already traveling.")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=150)
        st.subheader("🧳 Post Your Travel")
        st.write("Let others know your travel route and earn by carrying parcels safely.")

    st.markdown("---")
    st.success("🤝 Build a real human network that trusts and supports each other.")

# -------------------- Page: Send Parcel --------------------
elif page == "📦 Send Parcel":
    st.header("📦 Create Delivery Request")
    with st.form("request_form"):
        pickup = st.text_input("Pickup Location")
        drop = st.text_input("Drop Location")
        item_type = st.text_input("Item Type")
        budget = st.number_input("Budget (₹)", min_value=0)
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            st.success("✅ Request submitted successfully!")
            st.json({
                "pickup": pickup,
                "drop": drop,
                "item_type": item_type,
                "budget": budget
            })

# -------------------- Page: Post Travel --------------------
elif page == "🧳 Post Travel":
    st.header("🧳 Post Travel Info")
    with st.form("travel_form"):
        from_location = st.text_input("From")
        to_location = st.text_input("To")
        date = st.date_input("Travel Date")
        capacity = st.number_input("Available Capacity (kg)", min_value=0)
        submitted = st.form_submit_button("Post Travel")
        if submitted:
            st.success("✅ Travel info posted successfully!")
            st.json({
                "from": from_location,
                "to": to_location,
                "date": str(date),
                "capacity": capacity
            })

# -------------------- Page: Live Map --------------------
elif page == "📍 Live Map":
    st.header("📍 Live Delivery Map")
    st.write("Map showing default location (Delhi)")

    m = folium.Map(location=[28.6139, 77.2090], zoom_start=8)
    folium.Marker([28.6139, 77.2090], popup="Default Location (Delhi)").add_to(m)
    st_folium(m, width=700, height=500)

# -------------------- Page: Matches --------------------
elif page == "🔗 Matches":
    st.header("🔗 Matched Requests & Travelers")
    st.write("🚧 Matching logic coming soon...")
    st.table([
        {"Request": "Parcel A", "Traveler": "Ravi", "Match %": "80%"},
        {"Request": "Parcel B", "Traveler": "Sneha", "Match %": "72%"},
    ])
