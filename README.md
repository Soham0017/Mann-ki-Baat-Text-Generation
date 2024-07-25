# Mann Ki Baat Text Generator

This project creates a text generation model based on the "Mann Ki Baat" speeches delivered by the Prime Minister of India. Using data scraped from [www.pmindia.gov.in](https://www.pmindia.gov.in/), the model generates coherent and contextually relevant text.The goal of this project is to leverage text data from the "Mann Ki Baat" series to build a model capable of generating text that mimics the style and themes of these speeches. The process involves several key steps:

1. **Data Collection**:
   - The data is scraped from the [PM India website](https://www.pmindia.gov.in/), focusing on various episodes of the "Mann Ki Baat" speeches, using BeautifulSoup.
   - The collected text is then cleaned and preprocessed to remove any inconsistencies and prepare it for model training.

2. **Model Building**:
   - A text generation model is constructed using TensorFlow and Keras, specifically utilizing Long Short-Term Memory (LSTM) networks.
   - The model is trained on the preprocessed text data to learn patterns, themes, and styles of the speeches.

3. **Text Generation**:
   - Once trained, the model is used to generate new text sequences. Users can input a seed phrase, and the model will produce text that continues from that phrase, maintaining coherence and relevance to the original style.

## Features

- **Data Preprocessing**: Involves text extraction, cleaning, and tokenization to ensure the data is in a suitable format for training.
- **LSTM-Based Model**: Employs Long Short-Term Memory (LSTM) networks to capture and generate text sequences with long-range dependencies.
- **Interactive Text Generation**: Generates new text sequences based on user-provided seed phrases, enabling dynamic and contextually appropriate text creation.
