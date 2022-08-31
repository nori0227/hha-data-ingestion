import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files

# Section 1:
# 1. from Kaggle, downloaded two datasets and combined into one xls file
# 2. put the file in the data subfolder
# 3. defined the xls spreadsheet with the variable xls
xls = xlrd.open_workbook(
    '/Users/nuri/Documents/GitHub/hha-data-ingestion/Data/Dataset.xls', on_demand=True)
# 4. to see what tabs are in the spreadsheet, create the below command
xls.sheet_names()
# 5. from this, find out there are two tabs: 'StudentsPerformance' and 'Score'
# 6. define each tab with a variable using the below commands
tab1 = pd.read_excel(
    '/Users/nuri/Documents/GitHub/hha-data-ingestion/data/Dataset.xls', sheet_name='StudentsPerformance')
tab2 = pd.read_excel(
    '/Users/nuri/Documents/GitHub/hha-data-ingestion/data/dataset.xls', sheet_name='Score')
