#Global Tourism Data Analysis

##Project Overview

This project focuses on cleaning, validating, and analyzing global tourism data.

The goal is to transform raw tourism datasets into structured, analysis-ready data and use it to answer meaningful analytical questions about tourism trends, arrivals, expenditure, purpose of travel, and length of stay.

## Analytical Questions

The analysis will focus on answering the following questions:

1. Which countries received the highest number of tourists during 2013–2022?
2. What are the top 5 most visited countries, and what are the main purposes of visits to these countries?
3. Which geographical regions are the main sources of inbound tourists?
 4. Which countries recorded the highest average annual travel expenditure among countries with sufficient data     availability during 2013–2022?
5. Which countries recorded the longest average length of stay during 2013–2022?
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
- Cleaning and converting numerical values, including values containing thousands separators.- Handling missing values by converting them to `NaN` instead of deleting them.
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
|__analysis/
|   |__SQL analysis results 
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
|
|__sql/
|  ├── 01_top_visited_countries.sql
│  ├── 02_top_5_countries_purpose.sql
│  ├── 03_tourist_regions.sql
│  ├── 04_tourism_expenditure.sql
│  ├── 05_average_length_of_stay.sql
│  └── 06_stay_vs_expenditure.sql
│
└── README.md


## Tools & Technologies

## Tools & Technologies

- **Python** – Data processing and cleaning
- **Pandas** – Data transformation
- **PostgreSQL** – Data storage and SQL analysis
- **SQL** – Analytical queries
- **Git & GitHub** – Version control and project management
- **Power BI** – Data visualization and dashboarding

## Next Steps

- Build interactive dashboards using Power BI.
- Visualize the key findings from the SQL analysis.
- Identify and communicate the main tourism trends and insights.
- Document the final results and insights in the project README.