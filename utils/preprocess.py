import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from uuid import uuid4

import re

def preprocess_text(text):
    if not isinstance(text, str):
        # raise TypeError("Expected a string or bytes-like object")
        return ""
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.lower()
    text = text.strip()
    return text

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values (example: fill with mean)
    # data.fillna(data.mean(), inplace=True)
    
    # Encode categorical variables (example: one-hot encoding)
    print(data.columns)
    # data = pd.get_dummies(data)

    #remove characters other than alphabets and numbers
    data['title'] = data['title'].str.replace(r'[^a-zA-Z0-9]', ' ')
    data['description'] = data['description'].str.replace(r'[^a-zA-Z0-9]', ' ')

    
    # Preprocess text data
    data['title'] = data['title'].apply(preprocess_text)  # Replace 'text_column' with your actual text column name
    data['description'] = data['description'].apply(preprocess_text)  # Replace 'text_column' with your actual text column name
    
    # # Vectorize text data
    # vectorizer = TfidfVectorizer()

    # X_text = vectorizer.fit_transform(data['title'] + ' ' + data['description'])  
    # return X_text, data
    return data

# Example usage
file_path = '/home/jaggu/misc/RAG/project/data/amazon-products.csv'  # Replace with your actual file path
data = load_and_preprocess_data(file_path)

# add additonl column uuid
data['uuid'] = [str(uuid4()) for _ in range(len(data))]

print(data.shape)
print(data)

data.to_csv('/home/jaggu/misc/RAG/project/data/amazon-products-preprocessed.csv', index=False)