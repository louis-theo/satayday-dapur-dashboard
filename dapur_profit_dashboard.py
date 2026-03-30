import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SATAYDAY @ Dapur | Proposal Dashboard",
    page_icon="📈",
    layout="wide",
)

# -------------------------------------------------
# Data and assumptions
# -------------------------------------------------
DAPUR_SHARE_PCT = 25
PRICE_PER_PORTION = 8.0
DAPUR_PER_PORTION = PRICE_PER_PORTION * (DAPUR_SHARE_PCT / 100)
MONDAYS_PER_MONTH = 4
SATURDAYS_PER_MONTH = 4

saturday_data = pd.DataFrame(
    {
        "Scenario": [
            "Baseline Target",
            "Busy Day",
            "High Volume Day",
            "Peak Performance",
        ],
        "Customers": [60, 120, 240, 300],
        "Total Revenue": [480, 960, 1920, 2400],
        "Dapur Profit": [120, 240, 480, 600],
    }
)

monday_data = pd.DataFrame(
    {
        "Scenario": ["Conservative", "Moderate", "Strong Day"],
        "Portions Sold": [15, 30, 50],
        "Total Revenue": [120, 240, 400],
        "Dapur Profit": [30, 60, 100],
    }
)


def format_currency(value: float) -> str:
    return f"£{value:,.0f}"


# -------------------------------------------------
# Styling
# -------------------------------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f4ec;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .hero-box {
            background: linear-gradient(135deg, #111714 0%, #1b211d 100%);
            padding: 1.8rem;
            border-radius: 22px;
            border: 1px solid #2e3a33;
            margin-bottom: 1rem;
            color: #f7efd8;
        }
        .hero-sub {
            color: #ddc07a;
            font-size: 1.05rem;
        }
        .card {
            background: #ffffff;
            padding: 1.2rem;
            border-radius: 18px;
            border: 1px solid #eadfce;
            box-shadow: 0 8px 24px rgba(0,0,0,0.05);
            height: 100%;
        }
        .dark-card {
            background: linear-gradient(135deg, #121816 0%, #1b211d 100%);
            padding: 1.2rem;
            border-radius: 18px;
            border: 1px solid #2f3a34;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            color: #f7efd8;
            height: 100%;
        }
        .mini-note {
            color: #72695f;
            font-size: 0.95rem;
        }
        .big-number {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
            color: #f0b64d;
        }
        .small-heading {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: #8b7a66;
        }
        .point-box {
            background: #fffaf1;
            border: 1px solid #eddcb8;
            border-radius: 16px;
            padding: 0.9rem 1rem;
            margin-bottom: 0.8rem;
        }
        h1, h2, h3 {
            color: #221c14;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown(
    f"""
    <div class="hero-box">
        <div style="font-size:0.95rem; letter-spacing:0.08em; text-transform:uppercase; color:#ddc07a; margin-bottom:0.4rem;">
            SATAYDAY @ Dapur
        </div>
        <h1 style="color:#f7efd8; margin-bottom:0.35rem;">Proposal Profit Dashboard</h1>
        <p class="hero-sub" style="margin-bottom:0.4rem;">
            A clear visual case for why this is a <strong>low-risk, high-upside</strong> opportunity for Dapur.
        </p>
        <p style="margin-bottom:0; color:#f2ead8;">
            Core assumption used throughout: <strong>Dapur receives {DAPUR_SHARE_PCT}% of revenue</strong>, equal to <strong>{format_currency(DAPUR_PER_PORTION)} per £{PRICE_PER_PORTION:,.0f} portion</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# Top summary metrics
# -------------------------------------------------
metric_1, metric_2, metric_3, metric_4 = st.columns(4)
with metric_1:
    st.metric("Dapur per portion", format_currency(DAPUR_PER_PORTION))
with metric_2:
    st.metric("Best Saturday profit", format_currency(saturday_data["Dapur Profit"].max()))
with metric_3:
    st.metric("Strong Monday profit", format_currency(monday_data["Dapur Profit"].max()))
with metric_4:
    st.metric(
        "4-week upside (peak Sat + strong Mon)",
        format_currency((600 + 100) * 4),
    )

st.markdown("")

# -------------------------------------------------
# Why this works + zero-risk section
# -------------------------------------------------
col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Why this works for Dapur")
    st.markdown(
        """
        <div class="point-box"><strong>Existing demand:</strong> customers already ask whether Dapur sells satay.</div>
        <div class="point-box"><strong>Complementary offer:</strong> adds something authentic and high-appeal without overlapping the weekday menu.</div>
        <div class="point-box"><strong>Extra footfall:</strong> creates another reason for customers to visit and talk about Dapur.</div>
        <div class="point-box"><strong>Scalable concept:</strong> starts simply, with room to expand if successful.</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="dark-card">', unsafe_allow_html=True)
    st.subheader("Why it is low risk for Dapur")
    st.markdown(
        f"""
        <div class="big-number">{DAPUR_SHARE_PCT}%</div>
        <div style="margin-bottom:1rem;">Revenue share paid directly to Dapur</div>
        <div style="margin-bottom:0.6rem;">• No upfront cost</div>
        <div style="margin-bottom:0.6rem;">• No ingredient cost</div>
        <div style="margin-bottom:0.6rem;">• No additional staffing required</div>
        <div style="margin-bottom:0.6rem;">• Operations handled fully by us</div>
        <div style="margin-top:1rem; color:#ddc07a;">Every portion sold creates revenue for Dapur with minimal burden on the business.</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Saturday projections
# -------------------------------------------------
sat_left, sat_right = st.columns([1.05, 1])

with sat_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Saturday profit projections")
    st.caption("These show the upside if Saturday walk-in trading is also allowed.")

    saturday_display = saturday_data.copy()
    saturday_display["Total Revenue"] = saturday_display["Total Revenue"].apply(format_currency)
    saturday_display["Dapur Profit"] = saturday_display["Dapur Profit"].apply(format_currency)
    st.dataframe(saturday_display, width="stretch", hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with sat_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig_sat, ax_sat = plt.subplots(figsize=(8, 4.8))
    ax_sat.bar(saturday_data["Scenario"], saturday_data["Dapur Profit"])
    ax_sat.set_title("Saturday: Dapur profit by scenario", pad=15)
    ax_sat.set_ylabel("Profit (£)")
    ax_sat.set_xlabel("")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    st.pyplot(fig_sat, clear_figure=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Monday projections
# -------------------------------------------------
mon_left, mon_right = st.columns([1.05, 1])

with mon_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Monday profit projections")
    st.caption("This is the core proposal day and shows the base business case.")

    monday_display = monday_data.copy()
    monday_display["Total Revenue"] = monday_display["Total Revenue"].apply(format_currency)
    monday_display["Dapur Profit"] = monday_display["Dapur Profit"].apply(format_currency)
    st.dataframe(monday_display, width="stretch", hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with mon_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig_mon, ax_mon = plt.subplots(figsize=(8, 4.8))
    ax_mon.bar(monday_data["Scenario"], monday_data["Dapur Profit"])
    ax_mon.set_title("Monday: Dapur profit by scenario", pad=15)
    ax_mon.set_ylabel("Profit (£)")
    ax_mon.set_xlabel("")
    plt.tight_layout()
    st.pyplot(fig_mon, clear_figure=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Per portion and quick understanding section
# -------------------------------------------------
portion_col1, portion_col2, portion_col3, portion_col4 = st.columns(4)
with portion_col1:
    st.info(f"""**10 portions sold**
    Dapur earns **{format_currency(10 * DAPUR_PER_PORTION)}**""")

    st.info(f"""**25 portions sold**
    Dapur earns **{format_currency(25 * DAPUR_PER_PORTION)}**""")

    st.info(f"""**50 portions sold**
    Dapur earns **{format_currency(50 * DAPUR_PER_PORTION)}**""")

    st.info(f"""**100 portions sold**
    Dapur earns **{format_currency(100 * DAPUR_PER_PORTION)}**""")
    st.markdown("")

# -------------------------------------------------
# Weekly / monthly / annual view
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("What this could mean over time")
st.caption("This turns the idea from a one-day pop-up into a clear recurring revenue opportunity.")

weekly_options = pd.DataFrame(
    {
        "Scenario": [
            "Monday only – Conservative",
            "Monday only – Moderate",
            "Monday only – Strong",
            "Saturday + Monday – Moderate mix",
            "Saturday + Monday – Peak Saturday + Strong Monday",
        ],
        "Weekly Profit to Dapur": [30, 60, 100, 240 + 60, 600 + 100],
    }
)
weekly_options["Monthly Profit to Dapur"] = weekly_options["Weekly Profit to Dapur"] * 4
weekly_options["Annualised Profit to Dapur"] = weekly_options["Monthly Profit to Dapur"] * 12

weekly_display = weekly_options.copy()
weekly_display["Weekly Profit to Dapur"] = weekly_display["Weekly Profit to Dapur"].apply(format_currency)
weekly_display["Monthly Profit to Dapur"] = weekly_display["Monthly Profit to Dapur"].apply(format_currency)
weekly_display["Annualised Profit to Dapur"] = weekly_display["Annualised Profit to Dapur"].apply(format_currency)
st.dataframe(weekly_display, width="stretch", hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Combined scenario comparison
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Scenario comparison")
st.caption("A direct comparison of the proposal in its simplest form versus the expanded upside case.")

comparison_data = pd.DataFrame(
    {
        "Model": [
            "Monday only – Conservative",
            "Monday only – Strong",
            "Saturday only – Busy Day",
            "Saturday + Monday – Moderate mix",
            "Saturday + Monday – Peak mix",
        ],
        "Dapur Profit": [30, 100, 240, 300, 700],
    }
)

fig_compare, ax_compare = plt.subplots(figsize=(10, 5.2))
ax_compare.bar(comparison_data["Model"], comparison_data["Dapur Profit"])
ax_compare.set_title("How Dapur's earnings increase across different operating models", pad=15)
ax_compare.set_ylabel("Profit (£)")
ax_compare.set_xlabel("")
plt.xticks(rotation=18, ha="right")
plt.tight_layout()
st.pyplot(fig_compare, clear_figure=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Live calculator
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Live meeting calculator")
st.caption("Use this during the proposal meeting to instantly show Dapur's share under any sales scenario.")

calc_col1, calc_col2, calc_col3 = st.columns(3)
with calc_col1:
    portions = st.number_input("Number of portions/customers", min_value=0, value=60, step=5)
with calc_col2:
    price_per_portion = st.number_input("Selling price per portion (£)", min_value=0.0, value=8.0, step=0.5)
with calc_col3:
    dapur_share_pct = st.slider("Dapur share (%)", min_value=0, max_value=100, value=25)

total_revenue = portions * price_per_portion
dapur_share = total_revenue * (dapur_share_pct / 100)
month_projection = dapur_share * 4
year_projection = month_projection * 12

calc_m1, calc_m2, calc_m3, calc_m4 = st.columns(4)
with calc_m1:
    st.metric("Total revenue", format_currency(total_revenue))
with calc_m2:
    st.metric("Dapur earns", format_currency(dapur_share))
with calc_m3:
    st.metric("4-week equivalent", format_currency(month_projection))
with calc_m4:
    st.metric("Annual equivalent", format_currency(year_projection))

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# -------------------------------------------------
# Final takeaway
# -------------------------------------------------
st.markdown(
    """
    <div class="hero-box">
        <div style="font-size:0.95rem; letter-spacing:0.08em; text-transform:uppercase; color:#ddc07a; margin-bottom:0.4rem;">
            Key takeaway
        </div>
        <h3 style="color:#f7efd8; margin-bottom:0.45rem;">A simple, low-burden way for Dapur to create extra revenue</h3>
        <p style="margin-bottom:0; color:#f2ead8; font-size:1.05rem;">
            This concept gives Dapur a share of every sale, with no ingredient spend, no staffing increase, and no upfront outlay.
            Even at modest volumes, it creates additional profit. At stronger Saturday and Monday volumes, the upside becomes very meaningful.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)