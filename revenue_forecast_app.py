import streamlit as st

# ----------- Default funnel assumptions -----------
DEFAULT_LEAD_TO_MEETING = 0.05
DEFAULT_MEETING_TO_OPPORTUNITY = 0.50
DEFAULT_OPPORTUNITY_TO_CLOSED = 0.30
DEFAULT_AVERAGE_DEAL_SIZE = 75_000

# ----------- Forecasting function -----------
def forecast_revenue(leads: int, 
                     lead_to_meeting: float,
                     meeting_to_opportunity: float,
                     opportunity_to_closed: float,
                     average_deal_size: float) -> float:
    """Estimate revenue from number of leads and funnel conversion rates."""
    closed_deals = (leads *
                    lead_to_meeting *
                    meeting_to_opportunity *
                    opportunity_to_closed)
    return closed_deals * average_deal_size

# ----------- Streamlit App -----------
st.title("💰 Revenue Forecasting Tool")
st.write("Use the sliders below to test different sales scenarios.")

# Sliders & input widgets
leads = st.number_input("Number of leads", min_value=0, value=100, step=10)

lead_to_meeting = st.slider(
    "Lead to Meeting Rate (%)", 0.0, 100.0, DEFAULT_LEAD_TO_MEETING * 100
) / 100

meeting_to_opportunity = st.slider(
    "Meeting to Opportunity Rate (%)", 0.0, 100.0, DEFAULT_MEETING_TO_OPPORTUNITY * 100
) / 100

opportunity_to_closed = st.slider(
    "Opportunity to Closed-Won Rate (%)", 0.0, 100.0, DEFAULT_OPPORTUNITY_TO_CLOSED * 100
) / 100

average_deal_size = st.number_input(
    "Average Deal Size ($)", min_value=0, value=DEFAULT_AVERAGE_DEAL_SIZE, step=5000
)

# Calculate forecast
projected_revenue = forecast_revenue(
    leads,
    lead_to_meeting,
    meeting_to_opportunity,
    opportunity_to_closed,
    average_deal_size
)

# Show result
st.markdown("---")
st.metric("📈 Projected Revenue", f"${projected_revenue:,.0f}")


