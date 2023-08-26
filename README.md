# Multilabel-News-Classifier

A text classification model from data collection, model training, and deployment that can classify News articles. <br/>
The model can classify 22 different types of News articles <br/>The keys of `models\label_types_encoded.json` shows the News labels

###  Visit the [website Here !!](https://multilab-news-classifier.onrender.com)

 ## Data Collection

Data was collected from Website of [Dhaka-Tribune](https://www.dhakatribune.com/) and `31,125` News articles were scraped <br/>The data collection was completed in 2 steps:

 - **Step-1:- News URL Scraping:** The URLs of news were scraped with `Scripts\Scrape_URL.pyy` and the URLs are stored along with News titles in `Data\News_urls.csv`
 - **Steo2:- News article Scraping:** Using the URLs, News articles and News Category are scraped with `Scripts\data_scrapper.py` and they are stored in `Data\Dataset.csv`


## Data Preprocessing

Initially, there were 18 different Sub-categories and 4 Categories in the dataset. After some analysis, All the categories and sub-categories were merged as multiple-label category. Apart from that, Data was cleaned as URLs were dropped and nulls values were dropped as well and the final data size was `31,125` which was initially `31,889`.

## Model Training

For model selection, a `distilrobera-base` model from HuggingFace Transformers was finetuned that uses Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/SanjidHossain/Multilabel-News-Classifier/blob/main/Notebooks/Blurr_Onnx.ipynb)

## Model Compression and ONNX Inference

The trained model has a memory of 322+MB. For better usage, the model was compressed using ONNX quantization and brought under 82MB.

## Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/sanjid/News_Classifier)

<img src = "https://github.com/SanjidHossain/Multilabel-News-Classifier/blob/main/Data/Image%20sources/app_gradio.png" width="800" height="400">

## Web Deployment
A Flask App has been built and published on `render`. The web app can take any form of News or article and show the Category or type of the article as output. Check `flask ` branch. 
**Please visit the [Website](https://multilab-news-classifier.onrender.com)**

<img src = "Data/Image sources/Web_app.png" width="800" height="400">


