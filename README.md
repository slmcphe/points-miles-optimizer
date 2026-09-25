# ✈️ Flight Redemption Advisor

A Streamlit web app that helps travelers decide whether to use airline points and miles or pay cash for a flight.

## Overview

Redeeming points and miles can involve comparing cash prices, award prices, taxes and fees, available balances, and the estimated value of different loyalty currencies.

This project provides a simple decision-support tool that calculates the value of a points redemption and compares it with a predefined estimated value for each rewards program.

## Features

* Enter credit card points and airline mileage balances
* Enter airline cash prices
* Enter the number of miles required for an award flight
* Account for taxes and fees when redeeming miles
* Enter available airline credits
* Compare redemption value against estimated points-and-miles valuations
* Receive a recommendation to redeem points/miles or pay cash

## Rewards Programs

The calculator currently includes:

* Chase Ultimate Rewards
* American Express Membership Rewards
* Capital One Miles
* Delta SkyMiles
* American Airlines AAdvantage
* United MileagePlus
* Spirit Free Spirit Miles

## Technology

* Python
* Streamlit
* Pandas

## How to Run Locally

Clone the repository and navigate to the project directory:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd points-miles-redemption-optimizer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## Example Testing

One test scenario used a $500 Delta flight with 25,000 SkyMiles required and $11.20 in taxes and fees. The calculator determined that the redemption provided approximately 2.04¢ per SkyMile and recommended using points.

A second scenario used a $300 Delta flight with 40,000 SkyMiles required and $11.20 in taxes and fees. The calculator determined that the redemption provided approximately 0.78¢ per SkyMile and recommended paying cash.

## Future Enhancements

Potential future improvements include personalized redemption recommendations, dynamic points valuations, additional airlines and loyalty programs, transfer-partner optimization, and machine-learning-based recommendations.

## Project Context

Developed as part of the University of Michigan School of Information's SI 699 Big Data Analytics Mastery project.
