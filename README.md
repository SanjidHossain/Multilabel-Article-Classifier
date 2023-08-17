# Multilabel-News-Classifier

A text classification model from data collection, model training, and deployment that can classify News articles. <br/>
The model can classify 22 different types of News articles <br/>The keys of `models\label_types_encoded.json` shows the News labels

 ## Data Collection

Data was collected from Website of [Dhaka-Tribune](https://www.dhakatribune.com/) and `31,125` book details were scraped <br/>The data collection completed in 2 steps:

 - **Step-1:- News URL Scraping:** The urls of news were were scraped with `Scripts\Scrape_URL.pyy` and the urls are stored along with News tittles in `Data\News_urls.csv`
 - **Steo2:- News article Scraping:** Using the urls, News articles and News Category are scraped with `Scripts\data_scrapper.py` and they are stored in `Data\Dataset.csv`


## Data Preprocessing

Initially there were 18 different Sub-cetgories and 4 Categories in the dataset. After some analysis, All the catgeories and su-categories were merged as multil-label catgory. Apart from that, Data was cleaned as URL were dropped and nulls values were dropped as well and final data size was `31,125`

## Model Training

For model selection, a `distilrobera-base` model from HuggingFace Transformers was finetuned that uses Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/SanjidHossain/Multilabel-News-Classifier/blob/main/Notebooks/Blurr_Onnx.ipynb)

## Model Compression and ONNX Inference

The trained model has a memory of 322+MB . For better usage, the model was compressed using ONNX quantization and brought under 82MB.