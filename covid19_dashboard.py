import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import os
import requests

# Set page configuration
st.set_page_config(
    page_title="COVID-19 Global Data Tracker",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for the entire dashboard
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    /* Global animations */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes countUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    @keyframes glow {
        0% { text-shadow: 0 0 5px rgba(66, 133, 244, 0.5); }
        50% { text-shadow: 0 0 20px rgba(66, 133, 244, 0.8); }
        100% { text-shadow: 0 0 5px rgba(66, 133, 244, 0.5); }
    }

    /* Dashboard title styling */
    .main-title {
        background: linear-gradient(90deg, #1a2a6c, #b21f1f, #fdbb2d);
        background-size: 600% 600%;
        animation: gradientBG 10s ease infinite;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .main-title h1 {
        color: white;
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 10px;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .main-title h3 {
        color: rgba(255,255,255,0.9);
        font-size: 20px;
        font-weight: 500;
        margin-bottom: 15px;
        font-family: 'Roboto', sans-serif;
    }

    .main-title p {
        color: rgba(255,255,255,0.8);
        font-size: 18px;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.5;
        font-family: 'Roboto', sans-serif;
    }

    .floating-icon {
        display: inline-block;
        animation: float 3s ease-in-out infinite;
        margin: 0 10px;
        font-size: 36px;
    }

    /* Info cards styling */
    .info-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        animation: fadeIn 0.8s ease-out forwards;
    }

    .info-section h2 {
        color: white;
        font-size: 28px;
        margin-bottom: 20px;
        text-align: center;
        font-weight: 600;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .info-section h2 i {
        margin-right: 10px;
        animation: pulse 2s infinite;
    }

    .info-card {
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .info-icon {
        font-size: 32px;
        margin-bottom: 15px;
        display: inline-block;
        animation: pulse 2s infinite;
    }

    .info-label {
        font-size: 16px;
        color: #555;
        font-weight: 500;
        margin-bottom: 10px;
    }

    .info-value {
        font-size: 28px;
        font-weight: 700;
        margin: 10px 0;
        animation: countUp 1s ease-out forwards;
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .countries-card .info-icon { color: #4285F4; }
    .date-card .info-icon { color: #EA4335; }
    .records-card .info-icon { color: #34A853; }
</style>
""", unsafe_allow_html=True)

# Enhanced title and description with animations
st.markdown("""
<div class="main-title">
    <h1>
        <span class="floating-icon">🦠</span>
        COVID-19 GLOBAL DATA TRACKER
        <span class="floating-icon">🌡️</span>
    </h1>
    <h3>Developed by <a href="https://github.com/TheODDYSEY" target="_blank" style="color: #fdbb2d; text-decoration: none; font-weight: bold;">@TheODDYSEY</a></h3>
    <p>
        An interactive dashboard tracking global COVID-19 trends including cases, deaths, recoveries, and vaccinations across countries and time periods.
        Powered by real-time data from Our World in Data's comprehensive COVID-19 dataset.
    </p>
</div>
""", unsafe_allow_html=True)

# Function to load data
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data():
    try:
        # Create data directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        # URL for the Our World in Data COVID-19 dataset
        url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        file_path = 'data/owid-covid-data.csv'

        # Download the dataset if it doesn't exist
        if not os.path.exists(file_path):
            with st.spinner("Downloading COVID-19 dataset..."):
                try:
                    response = requests.get(url, timeout=30)
                    response.raise_for_status()  # Raise an exception for HTTP errors
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    st.success("Download complete!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error downloading the dataset: {str(e)}")
                    # If download fails and file doesn't exist, create a sample dataframe
                    if not os.path.exists(file_path):
                        st.warning("Using sample data instead.")
                        return create_sample_data()

        # Load the dataset
        try:
            df = pd.read_csv(file_path)

            # Check if the dataset has the expected columns
            required_columns = ['date', 'location', 'total_cases', 'total_deaths']
            missing_columns = [col for col in required_columns if col not in df.columns]

            if missing_columns:
                st.warning(f"Dataset is missing required columns: {', '.join(missing_columns)}. Using sample data instead.")
                return create_sample_data()

            # Convert date column to datetime
            df['date'] = pd.to_datetime(df['date'])

            # Calculate death rate
            if 'total_cases' in df.columns and 'total_deaths' in df.columns:
                df['death_rate'] = (df['total_deaths'] / df['total_cases'] * 100).round(2)
                df['death_rate'] = df['death_rate'].replace([np.inf, -np.inf], np.nan).fillna(0)
            else:
                df['death_rate'] = 0

            return df

        except Exception as e:
            st.error(f"Error loading the dataset: {str(e)}")
            return create_sample_data()

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return create_sample_data()

# Function to create sample data if loading fails
def create_sample_data():
    # Create a sample dataframe with minimal data for demonstration
    # Use real country codes for the map to work properly
    country_data = [
        {'name': 'United States', 'iso_code': 'USA'},
        {'name': 'India', 'iso_code': 'IND'},
        {'name': 'Brazil', 'iso_code': 'BRA'},
        {'name': 'United Kingdom', 'iso_code': 'GBR'},
        {'name': 'Russia', 'iso_code': 'RUS'},
        {'name': 'Germany', 'iso_code': 'DEU'},
        {'name': 'France', 'iso_code': 'FRA'},
        {'name': 'Italy', 'iso_code': 'ITA'},
        {'name': 'Spain', 'iso_code': 'ESP'},
        {'name': 'China', 'iso_code': 'CHN'}
    ]

    countries = [c['name'] for c in country_data]
    iso_codes = {c['name']: c['iso_code'] for c in country_data}

    dates = pd.date_range(start='2020-01-01', end='2023-01-01', freq='M')

    # Create empty dataframe
    sample_data = []

    # Generate sample data for each country and date
    for country in countries:
        for i, date in enumerate(dates):
            # Generate increasing values over time with some randomness
            country_index = countries.index(country) + 1
            base_cases = i * 10000 * country_index
            base_deaths = i * 500 * country_index

            # Add some randomness (±10%)
            import random
            random_factor = 0.9 + random.random() * 0.2  # Between 0.9 and 1.1

            total_cases = int(base_cases * random_factor)
            total_deaths = int(base_deaths * random_factor)
            new_cases = int(5000 * country_index * random_factor) if i > 0 else 0
            new_deaths = int(250 * country_index * random_factor) if i > 0 else 0

            # Calculate vaccination data (starting from month 12)
            vax_start_month = 12
            people_vaccinated = int(i * 5000 * country_index * random_factor) if i > vax_start_month else 0
            vax_percent = min(((i - vax_start_month) * 5 * country_index * random_factor / 5), 100) if i > vax_start_month else 0

            # Calculate death rate
            death_rate = (total_deaths / total_cases * 100) if total_cases > 0 else 0

            sample_data.append({
                'date': date,
                'location': country,
                'iso_code': iso_codes[country],
                'total_cases': total_cases,
                'new_cases': new_cases,
                'total_deaths': total_deaths,
                'new_deaths': new_deaths,
                'people_vaccinated': people_vaccinated,
                'people_vaccinated_per_hundred': vax_percent,
                'people_fully_vaccinated': int(people_vaccinated * 0.8),  # 80% of vaccinated are fully vaccinated
                'people_fully_vaccinated_per_hundred': vax_percent * 0.8 if vax_percent > 0 else 0,
                'death_rate': death_rate
            })

    df = pd.DataFrame(sample_data)
    st.warning("Using sample data for demonstration. The actual COVID-19 dataset could not be loaded.")
    return df

# Load the data
try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to load data: {str(e)}")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")

# Date range filter
min_date = df['date'].min().date()
max_date = df['date'].max().date()
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Convert back to datetime for filtering
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Country selection
all_countries = sorted(df['location'].unique())
default_countries = ['United States', 'India', 'Brazil', 'United Kingdom', 'Russia', 'France', 'Germany', 'South Africa', 'Kenya', 'China']
default_countries = [c for c in default_countries if c in all_countries]  # Ensure defaults exist in the data

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    all_countries,
    default=default_countries
)

# Metric selection
available_metrics = {
    'Total Cases': 'total_cases',
    'New Cases': 'new_cases',
    'Total Deaths': 'total_deaths',
    'New Deaths': 'new_deaths',
    'Death Rate (%)': 'death_rate',
    'Total Vaccinations': 'total_vaccinations',
    'People Vaccinated': 'people_vaccinated',
    'People Fully Vaccinated': 'people_fully_vaccinated',
    'People Vaccinated (%)': 'people_vaccinated_per_hundred',
    'People Fully Vaccinated (%)': 'people_fully_vaccinated_per_hundred'
}

selected_metrics = st.sidebar.multiselect(
    "Select Metrics to Display",
    list(available_metrics.keys()),
    default=['Total Cases', 'Total Deaths', 'Death Rate (%)', 'People Vaccinated (%)']
)

# Filter data based on selections
filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
if selected_countries:
    filtered_df = filtered_df[filtered_df['location'].isin(selected_countries)]

# Create three columns for the metrics
col1, col2, col3 = st.columns(3)

# Add some additional CSS for the cards
st.markdown("""
<style>
    .data-card {
        height: 100%;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .data-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .data-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        transition: all 0.3s ease;
    }

    .data-card:hover::before {
        width: 10px;
    }

    .countries-card::before { background-color: #4285F4; }
    .date-card::before { background-color: #EA4335; }
    .records-card::before { background-color: #34A853; }

    .card-icon {
        font-size: 32px;
        margin-bottom: 10px;
        display: inline-block;
        animation: pulse 2s infinite;
    }

    .countries-card .card-icon { color: #4285F4; }
    .date-card .card-icon { color: #EA4335; }
    .records-card .card-icon { color: #34A853; }

    .card-label {
        font-size: 16px;
        color: #555;
        font-weight: 500;
        margin-bottom: 10px;
    }

    .card-value {
        font-size: 28px;
        font-weight: 700;
        margin: 10px 0;
        animation: countUp 1s ease-out forwards;
    }

    .countries-card .card-value { color: #4285F4; }
    .date-card .card-value { color: #EA4335; }
    .records-card .card-value { color: #34A853; }

    .card-desc {
        font-size: 14px;
        color: #666;
        margin-top: 10px;
    }

    @keyframes countUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

with col1:
    st.markdown(f"""
    <div class="data-card countries-card">
        <div class="card-icon">🌎</div>
        <div class="card-label">TOTAL COUNTRIES</div>
        <div class="card-value">{df['location'].nunique()}</div>
        <div class="card-desc">Nations tracked in dataset</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="data-card date-card">
        <div class="card-icon">📅</div>
        <div class="card-label">DATE RANGE</div>
        <div class="card-value" style="font-size: 22px;">{min_date} to {max_date}</div>
        <div class="card-desc">Time period covered</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="data-card records-card">
        <div class="card-icon">📈</div>
        <div class="card-label">TOTAL RECORDS</div>
        <div class="card-value">{len(df):,}</div>
        <div class="card-desc">Data points analyzed</div>
    </div>
    """, unsafe_allow_html=True)

# Get the latest global data (needed for both map and overview)
latest_global = df.sort_values('date').groupby('location').tail(1)

# Filter out 'World' and 'International' entries and select only numeric columns for summing
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations', 'people_vaccinated']
filtered_global = latest_global[~latest_global['location'].isin(['World', 'International'])]

# Calculate global totals for numeric columns
global_totals = {}
for col in numeric_cols:
    if col in filtered_global.columns:
        global_totals[col] = filtered_global[col].sum(skipna=True)
    else:
        global_totals[col] = None

# Global overview with enhanced styling and animations
st.markdown("""

<style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes countUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 15px 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 10px;
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease-out forwards;
        border-left: 5px solid;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .metric-icon {
        font-size: 28px;
        margin-bottom: 8px;
        display: inline-block;
    }

    .metric-value {
        font-size: calc(18px + 1.5vw);
        font-weight: 700;
        margin: 8px 0;
        animation: countUp 1s ease-out forwards;
        word-break: break-word;
        line-height: 1.2;
    }

    .metric-label {
        font-size: calc(12px + 0.3vw);
        color: #555;
        font-weight: 500;
        margin-bottom: 5px;
    }

    .metric-desc {
        font-size: calc(10px + 0.2vw);
        color: #666;
        line-height: 1.3;
        margin-top: 5px;
    }

    .cases-card { border-color: #FF9800; animation-delay: 0.1s; }
    .cases-card .metric-icon { color: #FF9800; }
    .cases-card .metric-value { color: #FF9800; }

    .deaths-card { border-color: #F44336; animation-delay: 0.3s; }
    .deaths-card .metric-icon { color: #F44336; }
    .deaths-card .metric-value { color: #F44336; }

    .rate-card { border-color: #673AB7; animation-delay: 0.5s; }
    .rate-card .metric-icon { color: #673AB7; }
    .rate-card .metric-value { color: #673AB7; }

    .vax-card { border-color: #4CAF50; animation-delay: 0.7s; }
    .vax-card .metric-icon { color: #4CAF50; }
    .vax-card .metric-value { color: #4CAF50; }

    /* Media queries for better responsiveness */
    @media (max-width: 768px) {
        .metric-value {
            font-size: calc(16px + 1vw);
        }

        .metric-icon {
            font-size: 24px;
        }

        .metric-label {
            font-size: 14px;
        }

        .metric-desc {
            font-size: 12px;
        }

        .metric-card {
            padding: 10px 5px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Create custom metric cards with animations - use responsive layout
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if global_totals['total_cases'] is not None:
        st.markdown(f"""
        <div class="metric-card cases-card">
            <div class="metric-icon">🦠</div>
            <div class="metric-label">TOTAL CASES</div>
            <div class="metric-value">{global_totals['total_cases']:,.0f}</div>
            <div class="metric-desc">Confirmed infections worldwide</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="metric-card cases-card">
            <div class="metric-icon">🦠</div>
            <div class="metric-label">TOTAL CASES</div>
            <div class="metric-value">Data not available</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if global_totals['total_deaths'] is not None:
        st.markdown(f"""
        <div class="metric-card deaths-card">
            <div class="metric-icon">💔</div>
            <div class="metric-label">TOTAL DEATHS</div>
            <div class="metric-value">{global_totals['total_deaths']:,.0f}</div>
            <div class="metric-desc">Lives lost to COVID-19</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="metric-card deaths-card">
            <div class="metric-icon">💔</div>
            <div class="metric-label">TOTAL DEATHS</div>
            <div class="metric-value">Data not available</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
    if global_totals['total_cases'] is not None and global_totals['total_deaths'] is not None and global_totals['total_cases'] > 0:
        death_rate = (global_totals['total_deaths'] / global_totals['total_cases'] * 100).round(2)
        st.markdown(f"""
        <div class="metric-card rate-card">
            <div class="metric-icon">📊</div>
            <div class="metric-label">DEATH RATE</div>
            <div class="metric-value">{death_rate}%</div>
            <div class="metric-desc">Case fatality ratio</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="metric-card rate-card">
            <div class="metric-icon">📊</div>
            <div class="metric-label">DEATH RATE</div>
            <div class="metric-value">Data not available</div>
        </div>
        """, unsafe_allow_html=True)

with col4:
    if global_totals['people_vaccinated'] is not None:
        st.markdown(f"""
        <div class="metric-card vax-card">
            <div class="metric-icon">💉</div>
            <div class="metric-label">VACCINATED</div>
            <div class="metric-value">{global_totals['people_vaccinated']:,.0f}</div>
            <div class="metric-desc">People with at least one dose</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="metric-card vax-card">
            <div class="metric-icon">💉</div>
            <div class="metric-label">VACCINATED</div>
            <div class="metric-value">Data not available</div>
        </div>
        """, unsafe_allow_html=True)

# Add a separator with animation
st.markdown("""
<div style="margin: 30px 0; text-align: center; overflow: hidden;">
    <div style="display: inline-block; position: relative; animation: fadeIn 1s ease-out forwards; animation-delay: 0.9s; opacity: 0;">
        <hr style="width: 100px; display: inline-block; border: none; height: 2px; background: linear-gradient(90deg, transparent, rgba(30, 60, 114, 0.5), transparent);">
        <span style="margin: 0 15px; color: #555; position: relative; top: -3px;">UPDATED DATA</span>
        <hr style="width: 100px; display: inline-block; border: none; height: 2px; background: linear-gradient(90deg, transparent, rgba(30, 60, 114, 0.5), transparent);">
    </div>
</div>
""", unsafe_allow_html=True)

# World map visualization
st.header("Global COVID-19 Map")
st.markdown("""
This interactive map shows the global distribution of COVID-19 metrics.
Select a metric from the dropdown below to visualize its distribution across countries.
Hover over countries to see detailed information.
""")

# Select metric for the map
map_metric = st.selectbox(
    "Select Metric for World Map",
    list(available_metrics.keys()),
    index=0
)

map_metric_col = available_metrics[map_metric]

# Create a choropleth map
if map_metric_col in latest_global.columns:
    try:
        # Make sure iso_code column exists
        if 'iso_code' not in latest_global.columns:
            st.warning("ISO country codes are missing in the dataset, which are required for the world map visualization.")
        else:
            # Check if there are any valid iso_code values
            has_valid_iso = latest_global['iso_code'].notna().any()

            if not has_valid_iso:
                st.warning("No valid ISO country codes found in the dataset.")
            else:
                # Determine which columns to include in the hover data
                hover_columns = [map_metric_col]
                for col in ['total_cases', 'total_deaths', 'death_rate']:
                    if col in latest_global.columns:
                        hover_columns.append(col)

                # Create a copy of the dataframe with only the necessary columns
                # First, create a list of columns that exist in the dataframe
                available_cols = ['iso_code', 'location']
                for col in [map_metric_col] + hover_columns:
                    if col not in available_cols and col in latest_global.columns:
                        available_cols.append(col)

                # Create the map data with only available columns
                map_data = latest_global[available_cols].copy()

                # Remove rows with missing iso_code or the selected metric
                map_data = map_data.dropna(subset=['iso_code', map_metric_col])

                if map_data.empty:
                    st.warning(f"No data available for {map_metric} with valid ISO codes.")
                else:
                    # Create the choropleth map
                    fig = px.choropleth(
                        map_data,
                        locations="iso_code",
                        color=map_metric_col,
                        hover_name="location",
                        hover_data=hover_columns,
                        color_continuous_scale="Viridis",
                        title=f"Global {map_metric} Distribution"
                    )
                    # Make the map larger for better visibility
                    fig.update_layout(height=700, margin={"r":0,"t":30,"l":0,"b":0})
                    st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating the map visualization: {str(e)}")
        # Print more detailed error information for debugging
        import traceback
        st.error(f"Detailed error: {traceback.format_exc()}")
else:
    st.warning(f"Data for {map_metric} is not available for the world map visualization.")

# Country comparison
if selected_countries:
    st.header("Country Comparison")

    try:
        # Get the latest data for selected countries
        latest_selected = latest_global[latest_global['location'].isin(selected_countries)]

        if not latest_selected.empty:
            # Sort by total cases if available, otherwise use the first column
            if 'total_cases' in latest_selected.columns:
                latest_selected = latest_selected.sort_values('total_cases', ascending=False)

            # Create a bar chart for selected metrics
            for metric_name in selected_metrics:
                metric_col = available_metrics[metric_name]
                if metric_col in latest_selected.columns and latest_selected[metric_col].notna().any():
                    try:
                        fig = px.bar(
                            latest_selected,
                            x='location',
                            y=metric_col,
                            title=f"{metric_name} by Country (Latest Data)",
                            color='location',
                            labels={metric_col: metric_name, 'location': 'Country'}
                        )
                        fig.update_layout(xaxis_tickangle=-45)
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"Error creating bar chart for {metric_name}: {str(e)}")
                else:
                    st.warning(f"Data for {metric_name} is not available for some or all selected countries.")

            # Time series analysis
            st.header("Time Series Analysis")

            # Create time series plots for selected metrics
            for metric_name in selected_metrics:
                metric_col = available_metrics[metric_name]
                if metric_col in filtered_df.columns and filtered_df[metric_col].notna().any():
                    try:
                        # Filter data for selected countries and remove rows with NaN values for the metric
                        time_series_df = filtered_df[filtered_df['location'].isin(selected_countries)].dropna(subset=[metric_col])

                        if not time_series_df.empty:
                            fig = px.line(
                                time_series_df,
                                x='date',
                                y=metric_col,
                                color='location',
                                title=f"{metric_name} Over Time",
                                labels={metric_col: metric_name, 'date': 'Date', 'location': 'Country'}
                            )
                            fig.update_layout(xaxis_tickangle=-45)
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.warning(f"No time series data available for {metric_name} for the selected countries.")
                    except Exception as e:
                        st.error(f"Error creating time series chart for {metric_name}: {str(e)}")
                else:
                    st.warning(f"Time series data for {metric_name} is not available for some or all selected countries.")
        else:
            st.warning("No data available for the selected countries.")
    except Exception as e:
        st.error(f"Error in country comparison: {str(e)}")



# Vaccination progress
st.header("Vaccination Progress")

try:
    # Check if vaccination data column exists
    if 'people_vaccinated_per_hundred' in filtered_df.columns:
        # Filter countries with vaccination data
        vax_df = filtered_df.dropna(subset=['people_vaccinated_per_hundred'])
        vax_countries = vax_df['location'].unique()

        if len(vax_countries) > 0:
            # Get the latest vaccination data
            latest_vax = vax_df.sort_values('date').groupby('location').tail(1)
            latest_vax = latest_vax.sort_values('people_vaccinated_per_hundred', ascending=False)

            # Create a bar chart for vaccination rates
            try:
                fig = px.bar(
                    latest_vax,
                    x='location',
                    y='people_vaccinated_per_hundred',
                    title="Vaccination Rate by Country (% of Population)",
                    color='location',
                    labels={'people_vaccinated_per_hundred': 'People Vaccinated (%)', 'location': 'Country'}
                )
                fig.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating vaccination rate chart: {str(e)}")

            # Create a time series plot for vaccination progress
            if selected_countries:
                try:
                    vax_time_df = vax_df[vax_df['location'].isin(selected_countries)]
                    if not vax_time_df.empty:
                        fig = px.line(
                            vax_time_df,
                            x='date',
                            y='people_vaccinated_per_hundred',
                            color='location',
                            title="Vaccination Progress Over Time (% of Population)",
                            labels={'people_vaccinated_per_hundred': 'People Vaccinated (%)', 'date': 'Date', 'location': 'Country'}
                        )
                        fig.update_layout(xaxis_tickangle=-45)
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.warning("No vaccination data available for the selected countries.")
                except Exception as e:
                    st.error(f"Error creating vaccination progress chart: {str(e)}")
        else:
            st.warning("Vaccination data is not available for the selected countries or time period.")
    else:
        st.warning("Vaccination data (people_vaccinated_per_hundred) is not available in the dataset.")
except Exception as e:
    st.error(f"Error processing vaccination data: {str(e)}")

# Insights and conclusions
st.header("Key Insights")
st.markdown("""
### Key Insights from the COVID-19 Data Analysis

1. **Global Case Distribution**: The United States, India, and Brazil have consistently reported the highest number of COVID-19 cases globally, indicating the severity of the pandemic in these regions.

2. **Death Rate Variations**: Despite having high case numbers, some countries have managed to maintain lower death rates, suggesting differences in healthcare capacity, testing strategies, and population demographics.

3. **Vaccination Progress**: Countries like the United Kingdom and the United States have achieved higher vaccination rates compared to others, demonstrating the disparity in vaccine distribution and administration globally.

4. **Waves of Infection**: The data reveals multiple waves of infection across different countries, with varying timing and intensity, highlighting the dynamic nature of the pandemic and the influence of public health measures.

5. **Correlation Between Measures**: There appears to be a correlation between early vaccination rollout and reduced death rates in subsequent waves, suggesting the effectiveness of vaccines in mitigating the severity of the pandemic.
""")

