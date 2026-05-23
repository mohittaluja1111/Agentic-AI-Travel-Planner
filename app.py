import streamlit as st
from main import generate_travel_plan
from fpdf import FPDF


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)


# ==========================================
# PREMIUM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #F7F9FF, #EAF3FF);
}

.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #4A00E0;
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #666;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 28px;
    border-radius: 24px;
    margin-bottom: 25px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.08);
    color: black;
}

.section-title {
    font-size: 34px;
    font-weight: bold;
    color: #222;
    margin-top: 25px;
    margin-bottom: 18px;
}

.stButton>button {
    background: linear-gradient(90deg, #4A00E0, #8E2DE2);
    color: white;
    border: none;
    border-radius: 14px;
    height: 3.3em;
    width: 100%;
    font-size: 20px;
    font-weight: bold;
}

.info-box {
    background: white;
    padding: 22px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.07);
    color: black;
    font-size: 18px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    "<div class='main-title'>🌍 AI Travel Planner</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Plan Luxury Trips With AI ✨</div>",
    unsafe_allow_html=True
)


# ==========================================
# INPUTS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:

    city = st.selectbox(
        "📍 Destination City",
        [
            "Mumbai",
            "Goa",
            "Delhi",
            "Jaipur",
            "Bangalore",
            "Hyderabad",
            "Chennai",
            "Kolkata"
        ]
    )

with col2:

    budget = st.selectbox(
        "💰 Budget",
        [
            10000,
            20000,
            30000,
            50000,
            75000,
            100000
        ]
    )

with col3:

    days = st.selectbox(
        "📅 Days",
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    )


# ==========================================
# PDF FUNCTION
# ==========================================

def create_pdf(result):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="AI Travel Plan", ln=True)

    pdf.ln(10)

    pdf.multi_cell(
        0,
        10,
        f"Destination: {result['city']}"
    )

    pdf.multi_cell(
        0,
        10,
        f"Budget: Rs {result['budget']}"
    )

    pdf.multi_cell(
        0,
        10,
        f"Days: {result['days']}"
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        "Weather Forecast:"
    )

    pdf.multi_cell(
        0,
        10,
        "Day 1: Sunny - 31C\nDay 2: Cloudy - 29C\nDay 3: Pleasant Breeze - 28C"
    )

    pdf.ln(5)

    pdf.multi_cell(
        0,
        10,
        "Budget Breakdown:"
    )

    pdf.multi_cell(
        0,
        10,
        "Flights: Rs 4,800\nHotels: Rs 6,400\nFood & Transport: Rs 2,500\nTotal: Rs 13,700"
    )

    pdf.output("travel_plan.pdf")


# ==========================================
# GENERATE BUTTON
# ==========================================

if st.button("🚀 Generate AI Travel Plan"):

    result = generate_travel_plan(
        city,
        budget,
        days
    )

    st.success("✅ AI Travel Plan Generated Successfully!")

    # ==========================================
    # CITY IMAGE
    # ==========================================

    city_images = {

        "Mumbai":
        "https://images.unsplash.com/photo-1529253355930-ddbe423a2ac7",

        "Goa":
        "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2",

        "Delhi":
        "https://images.unsplash.com/photo-1587474260584-136574528ed5",

        "Jaipur":
        "https://images.unsplash.com/photo-1599661046289-e31897846e41",

        "Bangalore":
        "https://images.unsplash.com/photo-1596176530529-78163a4f7af2",

        "Hyderabad":
        "https://images.unsplash.com/photo-1567157577867-05ccb1388e66",

        "Chennai":
        "https://images.unsplash.com/photo-1582510003544-4d00b7f74220",

        "Kolkata":
        "https://images.unsplash.com/photo-1558431382-27e303142255"
    }

    st.image(
        city_images[city],
        use_container_width=True
    )

    # ==========================================
    # ITINERARY
    # ==========================================

    st.markdown(
        "<div class='section-title'>🗓 Your Travel Itinerary</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class='card'>

    <h2>{days}-Day Trip To {city}</h2>

    <hr>

    <h3>✈️ Flight Selected</h3>

    <p>
    IndiGo Airlines — Departure From Delhi At 2:00 PM
    <br><br>
    Estimated Fare: <b>Rs 4,800</b>
    </p>

    <hr>

    <h3>🏨 Hotel Recommendation</h3>

    <p>
    Sea View Resort — Luxury 4-Star Stay
    <br><br>
    Cost: <b>Rs 3,200/Night</b>
    </p>

    <hr>

    <h3>📍 Suggested Plan</h3>

    <p>
    Day 1 — Explore Famous Tourist Attractions
    <br><br>
    Day 2 — Local Food & Shopping Experience
    <br><br>
    Day 3 — Cultural Exploration & Sightseeing
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # WEATHER
    # ==========================================

    st.markdown(
        "<div class='section-title'>🌤 Weather Forecast</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='info-box'>

    ☀️ <b>Day 1:</b> Sunny — 31°C

    <br><br>

    🌤 <b>Day 2:</b> Partly Cloudy — 29°C

    <br><br>

    🌥 <b>Day 3:</b> Pleasant Breeze — 28°C

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # BUDGET
    # ==========================================

    st.markdown(
        "<div class='section-title'>💰 Budget Breakdown</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='info-box'>

    ✈️ Flights: <b>Rs 4,800</b>

    <br><br>

    🏨 Hotels: <b>Rs 6,400</b>

    <br><br>

    🍴 Food & Local Travel: <b>Rs 2,500</b>

    <br><br>

    <h3>Total Estimated Cost: Rs 13,700</h3>

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # HOTELS
    # ==========================================

    st.markdown(
        "<div class='section-title'>🏨 Recommended Hotels</div>",
        unsafe_allow_html=True
    )

    for hotel in result["hotels"]:

        st.markdown(f"""
        <div class='card'>

        <h3>{hotel['name']}</h3>

        ⭐ {hotel['stars']} Star Hotel

        <br><br>

        💰 Rs {hotel['price_per_night']} Per Night

        <br><br>

        🛎 Amenities:
        {", ".join(hotel['amenities'])}

        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # PLACES
    # ==========================================

    st.markdown(
        "<div class='section-title'>📍 Tourist Attractions</div>",
        unsafe_allow_html=True
    )

    for place in result["places"]:

        st.markdown(f"""
        <div class='card'>

        <h3>{place['name']}</h3>

        ⭐ Rating: {place['rating']}

        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # TRAVEL TIPS
    # ==========================================

    st.markdown(
        "<div class='section-title'>🤖 AI Travel Tips</div>",
        unsafe_allow_html=True
    )

    tips = result["travel_tips"]

    st.markdown(f"""
    <div class='info-box'>

    📅 <b>Best Time To Visit:</b>
    {tips.get('best_time', 'October to March')}

    <br><br>

    🍴 <b>Famous Food:</b>
    {tips.get('food', 'Local Street Food & Regional Dishes')}

    <br><br>

    🛡 <b>Safety Tips:</b>
    {tips.get('safety', 'Keep valuables safe and avoid isolated areas at night.')}

    <br><br>

    🚌 <b>Transport:</b>
    {tips.get('transport', 'Use taxis, metro, buses, and rental cabs.')}

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # PDF DOWNLOAD
    # ==========================================

    create_pdf(result)

    with open("travel_plan.pdf", "rb") as file:

        st.download_button(
            label="📥 Download Travel Plan PDF",
            data=file,
            file_name="travel_plan.pdf",
            mime="application/pdf"
        )