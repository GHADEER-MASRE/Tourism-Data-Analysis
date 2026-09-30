#Global Tourism Data Analysis

##Project Overview

This project focuses on cleaning, validating, and analyzing global tourism data.

The goal is to transform raw tourism datasets into structured, analysis-ready data and use it to answer meaningful analytical questions about tourism trends, arrivals, expenditure, purpose of travel, and length of stay.

## Analytical Questions

The analysis will focus on answering the following questions:

1. Which countries received the highest number of tourists during 2013–2022?
2. What are the top 5 most visited countries, and what are the main purposes of visits to these countries?
3. Which geographical regions are the main sources of inbound tourists?
4. Which countries recorded the highest tourism expenditure?
5. Which countries recorded the longest average length of stay?
6. Is there a relationship between tourists' average length of stay and their expenditure?

## Datasets

The project uses 10 tourism datasets covering different aspects of global tourism:

- Domestic Tourism – Accommodation
- Domestic Tourism – Trips
- Inbound Tourism – Accommodation
- Inbound Tourism – Arrivals
- Inbound Tourism – Expenditure
- Inbound Tourism – Purpose
- Inbound Tourism – Regions
- Inbound Tourism – Transport
- Outbound Tourism – Departures
- Outbound Tourism – Expenditure

The datasets cover the period from **1995 to 2022**.

## Data Cleaning

The raw datasets were originally stored in a wide and hierarchical format, making them difficult to read and analyze.

Using **Python and Pandas**, the data was transformed into a structured, analysis-ready format.

The main cleaning steps included:

- Reshaping the data from **wide format to long format** using `melt()`.
- Converting year columns into a single `Year` column.
- Extracting and organizing **Country** information.
- Identifying the relevant **indicators and categories** for each dataset.
- Converting numerical values using `pd.to_numeric()`.
- Handling missing values by converting them to `NaN` instead of deleting them.
- Creating reusable functions for common cleaning operations.
- Saving the cleaned datasets separately from the raw data.


## Data Validation

After cleaning, the datasets were validated to ensure that the data was structured correctly and ready for analysis.

The validation process included checking:

- Missing values
- Data types
- Year ranges
- Duplicate rows
- Duplicate logical records

All cleaned datasets were checked for structural consistency before moving to the analysis phase.

## Project Structure

```text
Tourism-Data-Analysis/
│
├── data/
│   ├── raw/
│   │   └── Original tourism datasets
│   │
│   └── cleaned/
│       └── Cleaned and analysis-ready datasets
│
├── scripts/
│   ├── cleaning_functions.py
│   └── validate_cleaned_data.py
│
└── README.md


## Tools & Technologies

- **Python** – Data processing and analysis
- **Pandas** – Data cleaning and transformation
- **Git & GitHub** – Version control and project management

## Next Steps

- Analyze tourism trends and patterns.
- Answer the analytical questions using the cleaned datasets.
- Create visualizations to communicate the findings.
- Extract meaningful insights from the analysis.