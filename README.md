# COVID-19 Global Data Tracker

A comprehensive data analysis and visualization project that tracks global COVID-19 trends, including cases, deaths, recoveries, and vaccinations across countries and time periods.

## Project Overview

This project analyzes real-world COVID-19 data to generate insights and visualize trends using Python data tools. It includes:

1. A Jupyter Notebook (`covid19_analysis.ipynb`) for comprehensive data analysis
2. A Streamlit dashboard (`covid19_dashboard.py`) for interactive visualization

## Features

- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries/regions
- Visualize trends with charts and maps
- Communicate findings with narrative insights

## Data Source

The project uses the COVID-19 dataset from [Our World in Data](https://ourworldindata.org/coronavirus), which provides comprehensive data on cases, deaths, testing, hospitalizations, and vaccinations.

## Getting Started

### Prerequisites

- Python 3.7+
- Required packages: pandas, numpy, matplotlib, seaborn, plotly, streamlit, jupyter

### Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
   ```

### Running the Jupyter Notebook

1. Navigate to the project directory
2. Launch Jupyter Notebook:
   ```
   jupyter notebook covid19_analysis.ipynb
   ```

### Running the Streamlit Dashboard

1. Navigate to the project directory
2. Launch the Streamlit app:
   ```
   streamlit run covid19_dashboard.py
   ```

## Project Structure

- `covid19_analysis.ipynb`: Jupyter notebook containing the data analysis
- `covid19_dashboard.py`: Streamlit app for interactive visualization
- `data/`: Directory for storing the COVID-19 dataset

## Analysis Components

1. **Data Collection**: Obtaining reliable COVID-19 data from Our World in Data
2. **Data Exploration**: Examining the dataset structure and basic statistics
3. **Data Cleaning**: Preparing data for analysis by handling missing values and converting data types
4. **Exploratory Data Analysis**: Generating descriptive statistics and exploring trends
5. **Vaccination Analysis**: Analyzing vaccination rollouts across countries
6. **Choropleth Maps**: Visualizing global COVID-19 cases and vaccination rates
7. **Insights & Reporting**: Summarizing key findings and patterns

## Key Insights

1. **Global Case Distribution**: The United States, India, and Brazil have consistently reported the highest number of COVID-19 cases globally.
2. **Death Rate Variations**: Despite having high case numbers, some countries have managed to maintain lower death rates.
3. **Vaccination Progress**: Countries like the United Kingdom and the United States have achieved higher vaccination rates compared to others.
4. **Waves of Infection**: The data reveals multiple waves of infection across different countries, with varying timing and intensity.
5. **Correlation Between Measures**: There appears to be a correlation between early vaccination rollout and reduced death rates in subsequent waves.

## Author

- @theoddysey

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [Our World in Data](https://ourworldindata.org/) for providing the COVID-19 dataset
- The global scientific community for their tireless efforts in combating the pandemic
