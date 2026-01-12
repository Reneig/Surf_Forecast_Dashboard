# Surf Forecast Dashboard Documentation

## 1. Project Overview

This project was developed for a **Surf School located near Bordeaux**.
The primary objective is to collect, process, and visualize real-time sea conditions to help instructors identify the **best moments to practice surfing** during the week. The final output is an interactive dashboard deployed on RPubs that serves as a decision-support tool for the school.

## 2. Technical Architecture

The solution follows a hybrid architecture, combining **Python** for data engineering and **R** for visualization.

### A. Data Extraction (Python)

A custom Python library named `surf_scrap` was developed to automate web scraping from the school's preferred source.

* **Source:** The library extracts data from [Surf-Report.com](https://www.surf-report.com/meteo-surf/lacanau-s1043.html).

* **Captured Variables:** For each of the 7 days forecasted, the script captures:
    * The date and time.
    * The wave size (e.g., "0.8m - 1.3m").
    * The wind speed in km/h.
    * The wind direction via orientation arrows.

* **Storage:** The extracted data is cleaned, structured into a dataframe, and exported as a **CSV file**.

### B. Dashboard Development (R & Flexdashboard)

The dashboard is built using the `flexdashboard` package in R, which integrates the Python backend.

* **Python Integration:** The R session executes the Python script to refresh the dataset automatically.
* **Data Transformation:**
    * **Wave Mean:** To visualize wave trends, the dashboard computes the mean of the extracted wave ranges.
    * **KPI Logic:** Key Performance Indicators (KPIs) were built based on the client's "best conditions" (high waves and strong North winds).

## 3. Dashboard Features & KPIs
The dashboard provides a single-tab interface containing the following metrics:

* **Wave Size Evolution:** A graph displaying the mean wave height over the forecast timeline.
* **Wind Speed Analysis:** A graph showing wind intensity changes over time.
* **Detailed Forecast Table:** A comprehensive view including Day, Hour, Wave Size, and Direction.
* **Best Surf Moment Box:** A specialized KPI box highlighting the specific day and time with the most favorable conditions for the coming week.

## 4. Methodology for "Best Conditions"
The dashboard identifies the optimal surfing window based on the school's specific criteria for the Bordeaux area:
1. **High Waves:** The sea generates significant wave height.
2. **Strong Wind Speed:** Higher wind intensity is preferred for these specific school activities.
3. **Wind Direction:** Optimal conditions are met when the wind is coming from the **North**.

**Live Dashboard:** You can access the published interactive dashboard here: [https://rpubs.com/Gbodo20/1387098](https://rpubs.com/Gbodo20/1387098)

**Python library:** You can access to the python library here: [https://pypi.org/project/surf-scrap/](https://pypi.org/project/surf-scrap/)