# Flight Redemption Advisor

### Data-Driven Optimization of Reward Redemption Strategies and Valuation Models

**Flight Redemption Advisor** is an interactive Streamlit application designed to help travelers decide whether to **redeem credit card points/airline miles or pay cash** for a flight.

The tool calculates the **cents-per-point (CPP)** value of a potential redemption and compares it against estimated point valuations to provide a straightforward recommendation.

## Live Demo

**Try the app:**
https://slmcphe-points-miles-optimizer-app-rdkdyw.streamlit.app/

---

## The Problem

Using points and miles effectively can be difficult because travelers must compare:

* Cash ticket prices
* Points or miles required
* Taxes and fees
* Existing airline credits
* Credit card point balances
* Estimated point values

Manually calculating these factors can be time-consuming and can lead to decision paralysis when multiple redemption options are available.

## The Solution

Flight Redemption Advisor brings these calculations into one interactive tool.

Users enter their available points and miles, flight pricing, redemption costs, taxes/fees, and applicable credits. The application then:

1. Calculates the effective cash price of the flight.
2. Calculates the redemption value in cents per point.
3. Compares the redemption value against an estimated benchmark.
4. Indicates whether using points or paying cash provides the stronger value.
5. Identifies the highest-value redemption option among the available choices.

## Key Features

### Points & Miles Balances

Users can enter balances for:

* Chase Ultimate Rewards
* Amex Membership Rewards
* Capital One Miles
* Delta SkyMiles
* American Airlines AAdvantage Miles
* United MileagePlus Miles
* Spirit Free Spirit Miles

### Flight Pricing

Users can enter:

* Cash ticket price
* Points/miles required
* Taxes and fees
* Airline credits

### CPP Analysis

The application calculates:

**Cents Per Point (CPP) = Effective Flight Cost ÷ Points Required × 100**

The calculated CPP is compared against an estimated value for each rewards program.

### Recommendation Engine

The application provides an easy-to-understand recommendation:

* **Use Points** when the calculated redemption value meets or exceeds the estimated benchmark.
* **Pay Cash** when the calculated redemption value falls below the estimated benchmark.

---

## Example

Suppose a Delta flight costs **$500 cash** or **40,000 SkyMiles + $6 in taxes and fees**.

The application calculates the redemption value and compares it with the estimated Delta SkyMiles valuation.

The result can then be used to determine whether redeeming miles provides sufficient value relative to paying cash.

---

## Technology

* **Python**
* **Streamlit** — interactive web application
* **Pandas** — data manipulation and calculations
* **GitHub** — version control and project hosting
* **Streamlit Community Cloud** — application deployment

---

## Data & Valuation Sources

The project was informed by publicly available points-and-miles valuation data, including:

* **The Points Guy (TPG)** — points and miles valuations
* **Roame** — rewards program valuation data

Valuations are used as benchmarks rather than guaranteed redemption values. Actual redemption value can vary depending on route, availability, airline pricing, transfer ratios, taxes, fees, and other factors.

---

## Future Enhancements

Potential future versions could include:

* Personalized redemption recommendations
* Additional airlines and hotel programs
* Transfer-partner optimization
* Dynamic points valuations
* Award availability integration
* Historical redemption-value tracking
* Machine-learning-based recommendation models
* Automatic flight-price and award-price comparisons
* User profiles for storing rewards balances
* Visualization of redemption value across programs

---

## Project Context

This project was developed as a passion project.

The project combines data analysis, valuation modeling, and product thinking to address a real-world decision-making problem in the travel rewards space.

### Project Goal

The broader goal is to demonstrate how data-driven tools can reduce the time and complexity involved in evaluating rewards redemption decisions.

---

## Author

**Sophia McPherson**

Data Science & Analytics | Product & AI

GitHub: https://github.com/slmcphe
