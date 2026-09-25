import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Flight Redemption Advisor",
    layout="wide"
)

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
st.title("Flight Redemption Advisor")
st.markdown(
    "Use this tool to decide whether to redeem points or pay cash for your flight."
)


# --------------------------------
# Input Section
# --------------------------------

st.header("1. Points and Miles Balances")

st.subheader("Credit Card Points")

col1, col2, col3 = st.columns(3)

with col1:
    chase_points = st.number_input(
        "Chase Ultimate Rewards",
        min_value=0,
        step=1000
    )

with col2:
    amex_points = st.number_input(
        "Amex Membership Rewards",
        min_value=0,
        step=1000
    )

with col3:
    capital_one_points = st.number_input(
        "Capital One Miles",
        min_value=0,
        step=1000
    )

cc_points = {
    "Chase UR": chase_points,
    "Amex MR": amex_points,
    "Capital One": capital_one_points
}


st.subheader("Airline Miles")

col1, col2, col3, col4 = st.columns(4)

with col1:
    delta_miles = st.number_input(
        "Delta SkyMiles",
        min_value=0,
        step=1000
    )

with col2:
    aa_miles = st.number_input(
        "American Airlines AAdvantage Miles",
        min_value=0,
        step=1000
    )

with col3:
    united_miles = st.number_input(
        "United MileagePlus Miles",
        min_value=0,
        step=1000
    )

with col4:
    spirit_miles = st.number_input(
        "Spirit Free Spirit Miles",
        min_value=0,
        step=1000
    )

airline_miles = {
    "Delta SkyMiles": delta_miles,
    "AA Miles": aa_miles,
    "United Miles": united_miles,
    "Spirit Miles": spirit_miles
}


st.header("2. Airline Credits")

col1, col2, col3, col4 = st.columns(4)

with col1:
    delta_credit = st.number_input(
        "Delta credit ($)",
        min_value=0.0,
        step=5.0
    )

with col2:
    aa_credit = st.number_input(
        "American Airlines credit ($)",
        min_value=0.0,
        step=5.0
    )

with col3:
    united_credit = st.number_input(
        "United credit ($)",
        min_value=0.0,
        step=5.0
    )

with col4:
    spirit_credit = st.number_input(
        "Spirit credit ($)",
        min_value=0.0,
        step=5.0
    )

credits = {
    "Delta SkyMiles": delta_credit,
    "AA Miles": aa_credit,
    "United Miles": united_credit,
    "Spirit Miles": spirit_credit
}


st.header("3. Flight Pricing")

col1, col2, col3, col4 = st.columns(4)

with col1:
    delta_cash = st.number_input(
        "Delta cash price ($)",
        min_value=0.0,
        step=5.0
    )

with col2:
    aa_cash = st.number_input(
        "American Airlines cash price ($)",
        min_value=0.0,
        step=5.0
    )

with col3:
    united_cash = st.number_input(
        "United cash price ($)",
        min_value=0.0,
        step=5.0
    )

with col4:
    spirit_cash = st.number_input(
        "Spirit cash price ($)",
        min_value=0.0,
        step=5.0
    )

cash_prices = {
    "Delta SkyMiles": delta_cash,
    "AA Miles": aa_cash,
    "United Miles": united_cash,
    "Spirit Miles": spirit_cash
}


st.header("4. Points Redemption Cost")

col1, col2, col3, col4 = st.columns(4)

with col1:
    delta_needed = st.number_input(
        "Delta SkyMiles needed",
        min_value=0,
        step=1000
    )

with col2:
    aa_needed = st.number_input(
        "American Airlines miles needed",
        min_value=0,
        step=1000
    )

with col3:
    united_needed = st.number_input(
        "United Miles needed",
        min_value=0,
        step=1000
    )

with col4:
    spirit_needed = st.number_input(
        "Spirit miles needed",
        min_value=0,
        step=1000
    )

points_needed = {
    "Delta SkyMiles": delta_needed,
    "AA Miles": aa_needed,
    "United Miles": united_needed,
    "Spirit Miles": spirit_needed
}


taxes_and_fees = st.number_input(
    "Taxes and fees when redeeming with miles ($)",
    min_value=0.0,
    step=1.0
)


st.header("5. Transfer Option")

transfer_option = st.selectbox(
    "Are you planning to transfer any credit card points to an airline?",
    ["None", "Delta", "AA", "United", "Spirit"]
)

transfer_map = {
    "Delta": "Delta SkyMiles",
    "AA": "AA Miles",
    "United": "United Miles",
    "Spirit": "Spirit Miles",
    "None": None
}

transfer_to = transfer_map[transfer_option]

# --------------------------------
# CPP Calculations & Recommendation
# --------------------------------
if st.button("Calculate Recommendation"):
    st.subheader("CPP (Cents Per Point) Analysis")

    total_cc_points = sum(cc_points.values())

    effective_prices = {
        program: max(cash_prices[program] - credits[program], 0)
        for program in credits
    }

    recommendations = []

    for program in effective_prices:
        miles_available = airline_miles[program]
        miles_required = points_needed[program]

        # Cannot calculate a redemption without a redemption cost
        if miles_required == 0:
            continue

        effective_price = effective_prices[program]
        total_cost = effective_price + taxes_and_fees

        cpp = round((total_cost / miles_required) * 100, 2)

        baseline = cpp_estimates.get(program, 1.0)

        # Determine whether the user can currently use this redemption
        has_enough_miles = miles_available >= miles_required
        transfer_selected = (
            transfer_to == program and total_cc_points > 0
        )

        # Display the CPP calculation
        st.write(
            f"**{program}**: {cpp}¢/pt "
            f"(est. value: {baseline}¢)"
        )

        # Determine status
        if has_enough_miles:
            if cpp >= baseline:
                status = "Use Points"
            else:
                status = "Pay Cash"

            st.write(f"→ {status}")

            recommendations.append(
                (program, cpp, baseline)
            )

        elif transfer_selected:
            if cpp >= baseline:
                status = "Use Points / Transfer Points"
            else:
                status = "Pay Cash"

            st.write(f"→ {status}")

            recommendations.append(
                (f"Transfer to {program}", cpp, baseline)
            )

        elif miles_available > 0:
            st.write(
                "→ Insufficient miles for this redemption"
            )

        else:
            st.write(
                "→ No miles available — Pay Cash"
            )

    # --------------------------------
    # Best Overall Option
    # --------------------------------
    if recommendations:
        best_program, best_cpp, best_est = max(
            recommendations,
            key=lambda x: x[1]
        )

        if best_cpp >= best_est:
            st.success(
                f"Best Option: Use **{best_program}** "
                f"({best_cpp}¢/pt ≥ {best_est}¢)"
            )
        else:
            st.info(
                "Best Option: **Pay with Cash** — "
                "the available redemptions do not provide "
                "better value than the benchmark."
            )

    else:
        st.info(
            "Best Option: **Pay with Cash** — "
            "no eligible points or miles are currently "
            "available for the redemption options entered."
        )
