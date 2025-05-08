# COVID-19 Global Data Tracker

![COVID-19 Dashboard](https://img.shields.io/badge/COVID--19-Dashboard-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-yellow)

An interactive dashboard tracking global COVID-19 trends including cases, deaths, recoveries, and vaccinations across countries and time periods. Powered by real-time data from Our World in Data's comprehensive COVID-19 dataset.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Data Source](#-data-source)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dashboard Components](#-dashboard-components)
- [Notebook Analysis](#-notebook-analysis)
- [Key Insights](#-key-insights)
- [Technologies Used](#-technologies-used)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 🌐 Overview

The COVID-19 Global Data Tracker is a comprehensive data visualization project that provides insights into the global COVID-19 pandemic. It consists of two main components:

1. **Interactive Streamlit Dashboard**: A web application that visualizes COVID-19 data with interactive charts, maps, and metrics.
2. **Jupyter Notebook Analysis**: A detailed exploratory data analysis of COVID-19 trends with in-depth statistical analysis and visualizations.

This project aims to make complex pandemic data accessible and understandable through intuitive visualizations and interactive elements.

## ✨ Features

- **Global Overview**: Key metrics showing worldwide COVID-19 impact
- **Interactive World Map**: Choropleth visualization of cases, deaths, and vaccinations
- **Country Comparison**: Side-by-side analysis of selected countries
- **Time Series Analysis**: Track pandemic progression over time
- **Vaccination Progress**: Monitor global vaccination efforts
- **Responsive Design**: Optimized for desktop and mobile devices
- **Real-time Data**: Automatic updates from Our World in Data
- **Detailed Analysis**: Comprehensive statistical analysis in Jupyter notebook

## 📁 Project Structure

```
COVID-19-Dashboard/
│
├── covid19_dashboard.py       # Main Streamlit dashboard application
├── covid19_analysis.ipynb     # Jupyter notebook with detailed analysis
├── data/                      # Data directory
│   └── owid-covid-data.csv    # Our World in Data COVID-19 dataset (downloaded automatically)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 📊 Data Source

This project uses the [Our World in Data COVID-19 dataset](https://ourworldindata.org/coronavirus), which provides a comprehensive collection of the COVID-19 data maintained by researchers at the University of Oxford and Global Change Data Lab. The dataset includes:

- Confirmed cases
- Confirmed deaths
- Hospitalizations
- Testing data
- Vaccination data
- Various demographic indicators

The data is automatically downloaded and updated when running the dashboard.

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheODDYSEY/Covid-19-Dashboard.git
   cd Covid-19-Dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly streamlit jupyter requests
   ```

## 🚀 Usage

### Running the Streamlit Dashboard

```bash
streamlit run covid19_dashboard.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

### Using the Jupyter Notebook

```bash
jupyter notebook covid19_analysis.ipynb
```

Or open with VS Code, PyCharm, or any other Jupyter-compatible IDE.

## 📊 Dashboard Components

### Global Overview Section
- Total cases, deaths, death rate, and vaccination metrics
- Animated counters with visual indicators
- Responsive design for all device sizes

### Interactive World Map
- Choropleth map showing global distribution of selected metrics
- Hover functionality to view detailed country information
- Color scale representing metric intensity

### Country Comparison
- Bar charts comparing selected countries across metrics
- Multi-select functionality to customize country selection
- Sortable data visualization

### Time Series Analysis
- Line charts showing progression of metrics over time
- Multiple country overlay for comparative analysis
- Date range selector for focused time periods

### Vaccination Progress
- Vaccination rate comparison across countries
- Time series tracking of vaccination campaigns
- Percentage of population metrics

## 📓 Notebook Analysis

The Jupyter notebook (`covid19_analysis.ipynb`) provides a more in-depth analysis of the COVID-19 data, including:

1. **Data Collection & Preprocessing**
   - Handling missing values
   - Data type conversion
   - Feature engineering

2. **Exploratory Data Analysis**
   - Statistical summaries
   - Distribution analysis
   - Correlation studies

3. **Advanced Visualizations**
   - Heatmaps of case correlation
   - Scatter plots with regression lines
   - Box plots of regional distributions

4. **Statistical Analysis**
   - Growth rate calculations
   - Moving averages
   - Comparative statistical tests

5. **Insights & Reporting**
   - Key findings documentation
   - Pattern identification
   - Trend analysis

## 📈 Key Insights

1. **Global Case Distribution**: The United States, India, and Brazil have consistently reported the highest number of COVID-19 cases globally, indicating the severity of the pandemic in these regions.

2. **Death Rate Variations**: Despite having high case numbers, some countries have managed to maintain lower death rates, suggesting differences in healthcare capacity, testing strategies, and population demographics.

3. **Vaccination Progress**: Countries like the United Kingdom and the United States have achieved higher vaccination rates compared to others, demonstrating the disparity in vaccine distribution and administration globally.

4. **Waves of Infection**: The data reveals multiple waves of infection across different countries, with varying timing and intensity, highlighting the dynamic nature of the pandemic and the influence of public health measures.

5. **Correlation Between Measures**: There appears to be a correlation between early vaccination rollout and reduced death rates in subsequent waves, suggesting the effectiveness of vaccines in mitigating the severity of the pandemic.

## 💻 Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualizations
- **Matplotlib/Seaborn**: Statistical visualizations in notebook
- **NumPy**: Numerical computations
- **Jupyter**: Notebook environment for analysis
- **Requests**: HTTP library for data downloading

## 🔮 Future Improvements

- Add predictive modeling for case forecasting
- Implement more advanced statistical analysis
- Add regional and local-level data where available
- Create downloadable reports and insights
- Add user authentication for personalized dashboards
- Implement natural language insights generation

## 👤 Author

- [@theoddysey](https://github.com/TheODDYSEY)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Our World in Data](https://ourworldindata.org/) for providing the COVID-19 dataset
- The global scientific community for their tireless efforts in combating the pandemic
- [Streamlit](https://streamlit.io/) for the amazing framework that powers the dashboard
- [Plotly](https://plotly.com/) for the interactive visualization capabilities

---

<p align="center">
  Built with ❤️ using <a href="https://streamlit.io/">Streamlit</a> and <a href="https://plotly.com/">Plotly</a>
</p>

<p align="center">
  © 2024 All Rights Reserved
</p>
