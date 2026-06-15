## What Drives User Conversion in Digital Platforms?

## Project Overview

This capstone project investigates how user engagement, weather conditions, and market characteristics influence conversion behavior in digital platforms.

Using Google Analytics 4 event data enriched with weather information and country-level indicators, the analysis explores whether engagement alone is sufficient to drive conversions and how external factors affect user intent.

## Business Questions
* Is engagement sufficient to drive conversion?
* How do external factors influence user intent?
* Does user behavior vary across different markets?

## Dataset

Sources
* Google Analytics 4 (GA4) event data
* Weather API data
* Country-level economic and digital connectivity indicators

## Limitations

* Weather conditions are associated with user behavior but do not imply causation.
* Analysis is based on observed sessions and conversions.
* Some countries contain extreme values that can influence comparisons and clustering results.

## Analytical Approach

* Session-Level Analysis
* User engagement and conversion behavior
* Weather impact on conversion
* New vs. returning users
* Temperature and environmental conditions
* Market Segmentation

Countries were grouped using clustering techniques based on:

* Economic indicators
* Digital connectivity
* Market maturity
* Statistical Testing

Hypothesis testing was used to validate whether observed differences were statistically significant.

## Key Findings

```text
1. Conversion Plateaus with Engagement
Early engagement strongly increases conversion probability.
Additional engagement provides diminishing returns.
More engagement does not necessarily mean more conversions.

2. Weather Influences Conversion Behavior
Conversion rates increase significantly during cold and extreme rain conditions.
Environmental context appears to influence purchase intent.
Differences were statistically significant.

3. Temperature Matters
Moderate temperatures generate the highest conversion rates.
Hot conditions show the lowest conversion performance.
User behavior changes under different environmental conditions.

4. Returning Users Convert More Consistently
Returning users outperform new users across most weather conditions.
New users are more sensitive to environmental changes.
User familiarity moderates the impact of weather.

5. Market Maturity Drives Performance
Developed markets achieve higher conversion rates and greater efficiency.
Higher conversion is not explained by engagement alone.
Environmental factors affect market segments differently.
```

## Tools & Technologies

* SQL
* Python
* Pandas
* BigQuery
* Google Analytics 4
* Weather API
* Tableau
* Statistical Testing

## Skills Demonstrated

* Data Cleaning & Transformation
* Exploratory Data Analysis (EDA)
* Data Visualization
* Statistical Testing
* Customer Behavior Analysis
* Market Segmentation
* Clustering
* Business Intelligence
* Storytelling with Data

## Project Structure

```text
capstone-project/
├── data/           # Raw and processed datasets
├── docs/           # Project documentation and presentation
├── images/         # Dashboard screenshots and visual assets
├── notebooks/      # Exploratory analysis notebooks
├── python/         # Python scripts and data processing
├── sql/            # SQL queries
├── src/            # Reusable project code
├── tableau/        # Tableau workbook
│   └── capstone_project.twb
├── .env
├── .gitignore
└── README.md
```

## Conclusion

The analysis shows that user engagement alone is not enough to explain conversion behavior.

External factors such as weather conditions, user type, and market maturity significantly influence conversion outcomes, highlighting the importance of combining behavioral and contextual data when making business decisions.

## Author

Gabriela Kilpp
```text
LinkedIn: https://www.linkedin.com/in/gabriela-kilpp
GitHub: https://github.com/gkilpp
```