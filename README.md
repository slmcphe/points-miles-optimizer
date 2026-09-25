# Flight Redemption Advisor

### A data-driven decision-support tool for optimizing points, miles, and cash when booking flights.

[**Try the Live Demo**](https://slmcphe-points-miles-optimizer-app-rdkdyw.streamlit.app/)

## Application Preview

![Streamlit screenshot blank.png]("Streamlit screenshot blank.png")

## Why I Built This

Travel rewards can create a decision-paralysis problem.

When booking a flight, travelers may need to compare cash prices, points or miles required, taxes and fees, airline credits, and the estimated value of their rewards. Doing these calculations manually across multiple programs can be time-consuming and make it difficult to determine whether a redemption is actually worthwhile.

I built **Flight Redemption Advisor** to turn that process into a simple, data-driven decision.

## The Product

The application allows travelers to enter their rewards balances and flight information, then calculates the potential value of each redemption in **cents per point (CPP)**.

The tool compares the calculated redemption value against an estimated rewards-program benchmark and provides an actionable recommendation:

* **Use Points** when the redemption meets or exceeds the estimated value.
* **Pay Cash** when the redemption falls below the estimated value.

The goal is to reduce manual calculations and help travelers make faster, more informed redemption decisions.

## How It Works

### 1. Enter Rewards Balances

Users can enter balances for:

* Chase Ultimate Rewards
* American Express Membership Rewards
* Capital One Miles
* Delta SkyMiles
* American Airlines AAdvantage Miles
* United MileagePlus Miles
* Spirit Free Spirit Miles

### 2. Enter Flight Information

Users provide:

* Cash ticket price
* Points or miles required
* Taxes and fees
* Applicable airline credits
* Potential transfer destination

### 3. Calculate Redemption Value

The application calculates the effective cost of the flight and converts the result into cents per point.

**CPP = Effective Flight Cost ÷ Points Required × 100**

### 4. Generate a Recommendation

The calculated CPP is compared with an estimated program valuation to determine whether the redemption provides sufficient value.

## Example

A traveler could compare a hypothetical:

**$500 cash fare**

versus:

**40,000 Delta SkyMiles + taxes and fees**

The application calculates the resulting CPP and determines whether the redemption meets the estimated value of the miles.

This transforms a multi-step calculation into a simple decision.

## Data and Methodology

The project uses estimated points-and-miles valuations informed by publicly available rewards data, including **The Points Guy** and **Roame**.

These valuations serve as benchmarks rather than guaranteed redemption values. Actual redemption value can vary based on:

* Award availability
* Route
* Travel dates
* Airline pricing
* Transfer ratios
* Taxes and fees
* Redemption type

## Technology

### Languages and Libraries

* Python
* Pandas
* Streamlit

### Development and Deployment

* GitHub
* Streamlit Community Cloud

## Project Architecture

The current MVP uses a rule-based valuation and recommendation approach:

**User Inputs → Effective Flight Cost → CPP Calculation → Benchmark Comparison → Recommendation**

The application is designed as a foundation that can be expanded with additional data and machine-learning capabilities.

## Future Product Opportunities

### Personalization

Recommendations based on a user's individual points balances, travel preferences, and redemption goals.

### Transfer Optimization

Automatically identify the most efficient credit-card-to-airline transfer pathway.

### Dynamic Valuations

Incorporate changing market valuations rather than relying solely on static benchmarks.

### Award Availability

Connect redemption recommendations to real-time award availability.

### Machine Learning

Use historical redemption data to predict redemption value and improve personalized recommendations.

### Automated Flight Comparison

Compare cash fares and award prices across multiple airlines and programs automatically.

## Product Impact

The project is designed around three measurable outcomes:

### Time Saved

Reduce the time required to manually calculate and compare redemption options.

### Less Manual Computation

Automate repetitive CPP and value calculations.

### Better-Informed Redemptions

Give travelers a consistent framework for evaluating whether points or cash provides greater value.

## Project Context

Developed as a passion project (Points & Miles Enthusiast / Credit Card Power User).

The project combines:

* Data analysis
* Quantitative valuation
* Python development
* Interactive application design
* Product thinking
* Decision-support modeling

Rather than simply analyzing rewards data, the project applies that analysis to a real-world consumer decision.

## About the Author

**Sophia McPherson**

Data Science & Analytics | Product & AI

[GitHub](https://github.com/slmcphe)
