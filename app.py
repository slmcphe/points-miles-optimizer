import streamlit as st
import pandas as pd


# --------------------------------
# Static CPP Estimates (cents/pt)
# --------------------------------
cpp_estimates = {
    'Chase UR': 1.25,
    'Amex MR': 1.10,
    'Capital One': 1.10,
    'Delta SkyMiles': 1.10,
    'AA Miles': 1.30,
    'United Miles': 1.25,
    'Spirit Miles': 0.75
}


# --------------------------------
# Streamlit Interface
# --------------------------------
st.title("✈️ Flight Redemption Advisor")
st.markdown(
    "Use this tool to decide whether to **redeem points or pay cash** for your flight."
)


# --------------------------------
# Input Section
# --------------------------------
st.header("1. Points and Miles Balances")

cc_points = {
    'Chase UR': st.number_input("Chase Ultimate Rewards", min_value=0, step=1000),
    'Amex MR': st.number_input("Amex Membership Rewards", min_value=0, step=1000),
    'Capital One': st.number_input("Capital One Miles", min_value=0, step=1000)
}

airline_miles = {
    'Delta SkyMiles': st.number_input("Delta SkyMiles", min_value=0, step=1000),
    'AA Miles': st.number_input("American Airlines AAdvantage Miles", min_value=0, step=1000),
    'United Miles': st.number_input("United MileagePlus Miles", min_value=0, step=1000),
    'Spirit Miles': st.number_input("Spirit Free Spirit Miles", min_value=0, step=1000)
}


st.header("2. Airline Gift Cards or Credits")

credits = {
    'Delta SkyMiles': st.number_input("Delta credit ($)", min_value=0.0, step=5.0),
    'AA Miles': st.number_input("AA credit ($)", min_value=0.0, step=5.0),
    'United Miles': st.number_input("United credit ($)", min_value=0.0, step=5.0),
    'Spirit Miles': st.number_input("Spirit credit ($)", min_value=0.0, step=5.0)
}


st.header("3. Flight Info – Airline Pricing")

cash_prices = {
    'Delta SkyMiles': st.number_input("Delta cash price ($)", min_value=0.0, step=5.0),
    'AA Miles': st.number_input("American Airlines cash price ($)", min_value=0.0, step=5.0),
    'United Miles': st.number_input("United cash price ($)", min_value=0.0, step=5.0),
    'Spirit Miles': st.number_input("Spirit cash price ($)", min_value=0.0, step=5.0)
}


st.header("3b. Flight Info – Points Redemption Cost")

points_needed = {
    'Delta SkyMiles': st.number_input("Delta SkyMiles needed for flight", min_value=0, step=1000),
    'AA Miles': st.number_input("American Airlines miles needed for flight", min_value=0, step=1000),
    'United Miles': st.number_input("United Miles needed for flight", min_value=0, step=1000),
    'Spirit Miles': st.number_input("Spirit miles needed for flight", min_value=0, step=1000)
}

taxes_and_fees = st.number_input(
    "Taxes/fees when redeeming with miles", min_value=0.0
)


st.header("4. Transfer Option")

transfer_option = st.selectbox(
    "Are you planning to transfer any credit card points to an airline?",
    ['None', 'Delta', 'AA', 'United', 'Spirit']
)

transfer_map = {
    'Delta': 'Delta SkyMiles',
    'AA': 'AA Miles',
    'United': 'United Miles',
    'Spirit': 'Spirit Miles',
    'None': None
}

transfer_to = transfer_map[transfer_option]


# --------------------------------
# CPP Calculations & Recommendation
# --------------------------------
if st.button("🔍 Calculate Recommendation"):
    st.subheader("📊 CPP (Cents Per Point) Analysis")

    all_balances = {**cc_points, **airline_miles}

    effective_prices = {
        program: max(cash_prices[program] - credits[program], 0)
        for program in credits
    }

    cpp_results = {}

    for program, points in all_balances.items():
        if points == 0:
            continue

        is_airline = program in airline_miles

        if program in effective_prices:
            effective_price = effective_prices[program]
        else:
            continue

        total_cost = effective_price + (taxes_and_fees if is_airline else 0)

        miles_required = points_needed.get(program, 0)

        if miles_required == 0:
            continue

        cpp = round((total_cost / miles_required) * 100, 2)
        cpp_results[program] = cpp

    # Handle transfers
    if transfer_to and any(cc_points.values()):
        if transfer_to in cpp_results:
            cpp_results[f'Transfer to {transfer_to}'] = cpp_results[transfer_to]

        for key in cc_points:
            cpp_results.pop(key, None)

    # Show results
    recommendations = []

    for program, cpp in cpp_results.items():
        baseline = cpp_estimates.get(
            program.replace("Transfer to ", ""), 1.0
        )
        status = "✅ Use Points" if cpp >= baseline else "💸 Pay Cash"

        st.write(
            f"**{program}**: {cpp}¢/pt "
            f"(est. value: {baseline}¢) → {status}"
        )

        recommendations.append((program, cpp, baseline))

    # Best overall option
    if recommendations:
        best_program, best_cpp, best_est = max(
            recommendations, key=lambda x: x[1]
        )

        if best_cpp >= best_est:
            st.success(
                f"🎯 Best Option: Use **{best_program}** "
                f"({best_cpp}¢/pt ≥ {best_est}¢)"
            )
        else:
            st.info(
                "🎯 Best Option: **Pay with Cash** — "
                "points don't offer better value."
            )
    else:
        st.warning(
            "No redemption options could be calculated. "
            "Please enter an eligible points balance and redemption cost."
        )
