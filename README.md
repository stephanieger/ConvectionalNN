# ConvectionalNN
MSiA490 Deep Learning Project

## Overview

This project is based off of the ideas discussed in the blog post [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). In this post, the abilityfor RNNs trained on a certain type of text is able to pick up the syntax of the text inputs, be it Shakespearean prose or LaTeX source file, and generate novel text that mimics the structure of the training data.

For this class project, we trained an LSTM based model on recipes that we pulled from the Yummly API. We cleaned the data and used all recipes with ``cookie'' in the title to try and generate novel cookie recipes from the training corpus.

## Steps
1. Get dataset from Yummly API with get_ingredients.py. You will need your own API Key and ID. 
2. Process data for model usage with process_ingredients.py and ingredients_to_txt.py
3. Train model with lstm_text_generation.py 
4. Predict new cookie recipes using lstm_text_predict.py

## Results
We generated a chocolate chip protein powder cookie recipe from this dataset and baked them for the class final presentation.
