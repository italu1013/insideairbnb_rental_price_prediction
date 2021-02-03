
### Data Download
```bash
bash ./data/downloader.sh

```
### Analysis and Result Notebook
to render javascript behavior on github, please refer to the following link:
https://nbviewer.jupyter.org/github/italu1013/insideairbnb_rental_price_prediction/blob/main/SD_airbnb_rental_EDA_and_rental_predict_modeling.ipynb


------
### Developing notes 
ideas:
* host/property image analysis
* comment sentiment analysis


training bert model on Colab (leveriing its GPU computation resources):
- notebook link: `https://colab.research.google.com/drive/1szG8-sbogv3V2fSlvQSmFDhALos9DQvi?usp=sharing`
- model file: `https://drive.google.com/file/d/1-CfdteZ4K6wtI2hMiLkx7a0flq7nX-2b/view?usp=sharing`
- inference results: `https://drive.google.com/file/d/1-NxMLkd5XhmjAPaIbwkmboYhsqz4B1Oh/view?usp=sharing`


- follow the instruction here to connect gpu on colab:
`https://colab.research.google.com/notebooks/gpu.ipynb#scrollTo=oM_8ELnJq_wd`


to improve:
* long tail categories merge
* labelencoder should save the mapping