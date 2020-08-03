from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def reindeer_wc(text):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__)

    # read the mask image
    reindeer_mask = np.array(Image.open(path.join(d, "reindeer.png")))

    stopwords = set(STOPWORDS)
    with open("wc_ignore.txt", "r", encoding="utf-8") as f:
        for w in f.read().split('\n'):
            stopwords.add(w)

    wc = WordCloud(background_color="black", max_words=3000, mask=reindeer_mask,
                   stopwords=stopwords)
    
    # create coloring from image
    im_colors = ImageColorGenerator(reindeer_mask)
    

    # generate word cloud
    wc.generate(text)
    wc.recolor(color_func=im_colors)

    # store to file
    return wc.to_file(path.join(d, "final_wc.png"))