# ItRadar

**ItRadar** is a search engine designed to scrape IT blogs and retrieve the most relevant links based on user queries. It leverages advanced ranking algorithms and indexing techniques to provide precise and efficient search results.

```
  ____________    ________    ________ ___________          _____         ____________       _____        ___________      
 /            \  /        \  /        \\          \       /      |_       \           \    /      |_      \          \     
|\___/\  \\___/||\         \/         /|\    /\    \     /         \       \           \  /         \      \    /\    \    
 \|____\  \___|/| \            /\____/ | |   \_\    |   |     /\    \       |    /\     ||     /\    \      |   \_\    |   
       |  |     |  \______/\   \     | | |      ___/    |    |  |    \      |   |  |    ||    |  |    \     |      ___/    
  __  /   / __   \ |      | \   \____|/  |      \  ____ |     \/      \     |    \/     ||     \/      \    |      \  ____ 
 /  \/   /_/  |   \|______|  \   \      /     /\ \/    \|\      /\     \   /           /||\      /\     \  /     /\ \/    \
|____________/|            \  \___\    /_____/ |\______|| \_____\ \_____\ /___________/ || \_____\ \_____\/_____/ |\______|
|           | /             \ |   |    |     | | |     || |     | |     ||           | / | |     | |     ||     | | |     |
|___________|/               \|___|    |_____|/ \|_____| \|_____|\|_____||___________|/   \|_____|\|_____||_____|/ \|_____|
```

This project is built for educational purposes, allowing you to explore the inner workings of web scraping, information retrieval, and search engine ranking methods.

## Features

- **Web Scraping**: Automatically scrapes IT-related blogs and stores the content locally.
- **Inverted Indexing**: Efficiently indexes scraped content to enable fast query retrieval.
- **BM25 Ranking Algorithm**: Uses the BM25 algorithm to rank search results based on relevance.
- **Flask Web Interface**: Provides a simple, user-friendly interface for querying and displaying results.

## How It Works

1. **Scraping**: ItRadar scrapes IT blogs to extract the article titles, URLs, and content. The scraped data is stored in JSON files.
2. **Indexing**: The scraped content is processed using an inverted index, which allows efficient querying by mapping keywords to documents.
3. **Querying**: When a user inputs a query, ItRadar calculates the relevance of each document using the BM25 algorithm and returns the most relevant results.
4. **Ranking**: The search results are ranked based on their BM25 scores and displayed with their corresponding URLs, titles, and snippets of content.

## Technical Details

- **Scrapy**: Used for web scraping.
- **Inverted Index**: A data structure that maps keywords to the documents in which they appear.
- **BM25**: A ranking function used to measure the relevance of documents to a given query.
- **Flask**: Provides a simple web interface for user interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Balcus/ItRadar.git
   ```
   
2. Go to the project's folder :
   ```bash
   cd .\ItRadar\
   ```
   
3. Install requirements :
   ```bash
   pip install -r requirements.txt
   ```
   
   If you have multiple versions of Python installed and want to ensure you're using pip for a specific version (like Python 3), you might want to use:
   ```bash
   pip3 install -r requirements.txt
   ```

   Or, if you need to specify the full path to pip for a particular Python installation:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
   
4. **OPTIONAL** :  A few websites have already been scraped and the data can be found in the json_folder. However, please note that these articles may not include the latest content.
   If you want to ensure you have the most up-to-date information, consider re-scraping these sites.
   To get started, first navigate to the `crawlers` folder :
   
   ```bash
   cd .\crawlers\
   ```
   After that you will need to once more navigate to the `crawlers` folder :
   
   ```bash
   cd .\crawlers\
   ```
   Inside it should look something like this:
   
   ```bash
     Mode                 LastWriteTime         Length Name
      ----                 -------------         ------ ----
    d-----         9/26/2024   3:49 PM                spiders
    d-----         9/26/2024   3:49 PM                __pycache__
    -a----         9/26/2024   3:49 PM            276 items.py
    -a----         9/26/2024   3:49 PM           3755 middlewares.py
    -a----         9/26/2024   3:49 PM            375 pipelines.py
    -a----         9/26/2024   3:49 PM           3816 settings.py
    -a----         9/26/2024   3:49 PM              0 __init__.py

   ```
   Go to the `spider` folder:
   ```bash
   cd .\spiders\
   ```
   And now you can run any of the spider by using the following command:
   ```bash
   scrapy crawl [name_of_the_spider] -O [name_of_json_file].json
   ```
   The names of the spiders can be found inside the `blog_spider.py` file or in the following list:
   
   - `danluuspider` for https://danluu.com/
   - `jvnsspider` for https://jvns.ca/
   - `2alityspider` for https://2ality.com/index.html
   - `cleancoderspider` for https://blog.cleancoder.com/
   - `pragmaticengineerspider` for https://blog.pragmaticengineer.com/
   - `techradarspider` for https://www.techradar.com/
   - `arsspider` for https://arstechnica.com/gadgets/
   - `a_list_apart_spider` for https://alistapart.com/articles/
   - `hsspider` for https://highscalability.com/
   - `css` for https://css-tricks.com/category/articles/
  
   The name of ths json files should also match the ones from the `json_folder'

   After scraping the websites and storing the data in JSON files, you can move these new files into the `json_folder`, replacing the existing files with the updated content.
   This ensures that you have the latest articles available for your search engine.

   After this move back until you find the app folder:
   ```bash
   cd ..
   ```
   (should do this for 3 times)

5. Get inside the app folder:
   ```bash
   cd .\app\
   ```

6. Run the app:
   ```bash
   python app.py
   ```
   or for python3 :
   ```bash
   python3 app.py
   ```

7. Open your browser and go to:
     ```
     http://localhost:5000
     ```

8. Have fun with the app !

## Contact

For any questions or feedback, please reach out via:

- Email: bbalcus04@gmail.com
- GitHub Issues: [Issues](https://github.com/Balcus/CTextEditor/issues)

Thank you for using Git-Stats!
  
   
