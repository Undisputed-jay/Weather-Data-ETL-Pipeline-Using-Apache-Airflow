<title>Weather Data ETL Pipeline Using Apache Airflow</title>
<body>
    <h1>Project Description</h1>
    <p>
        This project implements a <strong>Weather Data ETL (Extract, Transform, Load) pipeline</strong> using <strong>Apache Airflow</strong>. 
        The pipeline is designed to fetch weather data from a public API, transform it into a structured format, and load it into a <strong>PostgreSQL database</strong> for further analysis. 
        The solution leverages Airflow's powerful task scheduling and orchestration capabilities to ensure the smooth flow of data between external APIs and a persistent data store.
    </p>
    
    <p>The project follows a standard ETL process:</p>
    <ul>
        <li><strong>Extract</strong>: The pipeline sends a request to a weather API using an HTTP hook, fetching current weather data based on specific geographic coordinates (latitude and longitude).</li>
        <li><strong>Transform</strong>: The pipeline processes the raw weather data, extracting relevant fields such as temperature, wind speed, wind direction, and weather code.</li>
        <li><strong>Load</strong>: The transformed data is then loaded into a PostgreSQL database, creating the <code>weather_data</code> table if it doesn't exist and inserting the current weather information.</li>
    </ul>

    <p>
        The pipeline is simple, efficient, and designed to be flexible for expansion or adaptation to different data sources or weather endpoints.
    </p>

    <h2>Features:</h2>
    <ul>
        <li>Airflow DAG for scheduling and orchestrating the ETL process.</li>
        <li>HTTP Hook for making requests to an external weather API.</li>
        <li>PostgreSQL Hook for database interaction and data storage.</li>
        <li>Well-structured and modular design, ensuring easy maintenance and scalability.</li>
        <li>Automatic table creation if it doesn't exist already.</li>
        <li>Designed with a focus on reliability and error handling in API data extraction.</li>
    </ul>

    <h2>Requirements:</h2>
    <ul>
        <li>Apache Airflow</li>
        <li>PostgreSQL Database</li>
        <li>Requests library (for handling HTTP requests)</li>
    </ul>

    <h2>Usage:</h2>
    <p>To use this pipeline, clone the repository and follow these steps:</p>
    <ul>
        <li>Set up your Airflow environment and install the required providers (<code>HttpHook</code>, <code>PostgresHook</code>).</li>
        <li>Update the necessary connection configurations for both the API (<code>API_CONN_ID</code>) and the PostgreSQL database (<code>POSTGRES_CONN_ID</code>) in Airflow.</li>
        <li>Add the geographic coordinates (<code>LATITUDE</code>, <code>LONGITUDE</code>) for which you want to retrieve weather data.</li>
        <li>Trigger the DAG to fetch, transform, and store weather data into your PostgreSQL instance.</li>
    </ul>
    <h2>Sample Table Schema:</h2>
<p>The weather data is stored in a table with the following schema:</p>

<pre>
    <code>
CREATE TABLE IF NOT EXISTS weather_data (
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    windspeed FLOAT,
    winddirection FLOAT,
    weathercode INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    </code>
</pre>
