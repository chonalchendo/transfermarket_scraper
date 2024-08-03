# Medium Data Project

The purpose of this project is to explore and publish "full-stack data science" content.

Full-stack data science is a broad term used to encapsulate aspects of the data science lifecycle. The data science life cycle involves:
1. Project scoping - define business metrics to optimise 
2. Data Engineering - data collection, processing, validation and storage
3. Exploratory data analysis (EDA) - Gain insight from data
4. Statistical and machine learning (ML) - train model to optimise the business metric
5. Deploy model - deploy to serve end-user
6. Model monitoring and continual learning - update model based on evolving data
7. Model evaluation - evaluate the model against requirements developed at stage 1

The above depicts a simplified view of the components needed to develop modern ML systems, and the skills required to make each stage possible. 

My goal is to explore each stage by documenting best practices, the best tools to use, and to make it as interesting as possible!


## Project Scope

As mentioned above, this is a learning project, but that doesn't mean we shouldn't scope of requirements for the project and what we want to achieve.

To make it interesting I've focused this project on football market data. Quite often player transfer fees can be viewed as being priced incorrectly, especially in the Premier League. Therefore, it would be interesting to build an ML model that predicts player market valuations based on historical performance metrics, league, and wages to name a few.


## Data Engineering

The majority of the work done here will follow the Extract, Transform and Load (ETL) process.
- Extract - collect data from various sources
- Transform - process the data to make sense of it so downstream analytics can be performed
- Load - save the processed data to a location easily accessible for downstream analytics

Considerations for data engineering:
- Available data sources
- Storage location for data
- Orchestrate ETL process for automation

### Web Scraping (Data Collection)

This is the extract phase of the data engineering process. 

We'll use web scraping to extract market data from Transfermarkt.com. We will need detailed stats from other sites such as Fbref to conduct our analysis, as Transfermarkt does not provide this. 

Tools used:
- HTTPX
- Beautiful Soup

I've included for you the code and Medium walkthrough below.

[NOTEBOOK](https://github.com/chonalchendo/transfermarket_scraper/blob/main/notebooks/medium_scraper_code.ipynb)

[MEDIUM ARTICLE](https://medium.com/@conalhenderson/how-to-build-a-custom-web-scraper-to-extract-premier-league-player-market-data-3b8e5378cca2)

### Data Processing

This is the transformation stage.

The main considerations for this step are cleaning the data by standardising formats, and dealing with data types to increase storage efficiency. We also want to introduce data validation logic to set boundaries for what we expect our data to look like. For example, we can validate that player valuations are greater than or equal to zero, as negative values are invalid.

Tools used:
- Pandas (data processing)
- Pandera (data validation) 

I've included for you the code and Medium walkthrough for the data processing below.

[NOTEBOOK](https://github.com/chonalchendo/transfermarket_scraper/blob/main/notebooks/medium_processing_code.ipynb)

[MEDIUM ARTICLE](https://medium.com/@conalhenderson/master-pandas-to-build-modular-and-reusable-data-pipelines-1d12b003a423)

The data validation code and walkthrough will be published in due course.

## Future Work

As this project develops, I will upload articles to Medium discussing the steps I've taken and the code written to achieve each step
