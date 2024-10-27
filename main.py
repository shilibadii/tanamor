import pandas as pd
import numpy as np
import spacy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Load the dataset from a compressed CSV file
data = pd.read_csv('train.csv')

# Initialize the spaCy NLP model
nlp = spacy.load('en_core_web_sm')

# Preprocess the text data: convert to lowercase and filter out non-alphabetic characters
data['comment_text'] = data['comment_text'].apply(lambda x: nlp(x.lower()))
data['comment_text'] = data['comment_text'].apply(lambda x: ' '.join([token.text for token in x if token.is_alpha]))

# Compute sentiment polarity of comments and add as a new feature
data['polarity'] = data['comment_text'].apply(lambda x: x._.polarity if hasattr(x._, 'polarity') else 0)

# Set the maximum number of features and initialize the tokenizer
max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['comment_text'].values)

# Convert text to sequences and pad them to ensure uniform length
X = tokenizer.texts_to_sequences(data['comment_text'].values)
X = pad_sequences(X)

# Append sentiment polarity to the feature set
X = np.concatenate((X, data['polarity'].values.reshape(-1, 1)), axis=1)

# Define the neural network architecture
embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_features, embed_dim, input_length=X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(6, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Split the dataset into training and testing sets
Y = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# Train the model and print the accuracy
batch_size = 32
history = model.fit(X_train, Y_train, epochs=5, batch_size=batch_size, verbose=2)
print("Training Accuracy: {:.2f}%".format(history.history['accuracy'][-1] * 100))

# Save the model
model.save('toxic.h5')

# Define a function to test new comments for toxicity
def test_comment(comment):
    # Process the comment using NLP tools
    processed_comment = nlp(comment.lower())
    processed_text = ' '.join([token.text for token in processed_comment if token.is_alpha])
    polarity = processed_comment._.polarity if hasattr(processed_comment._, 'polarity') else 0
    
    # Convert text to padded sequence, incorporating polarity
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=X.shape[1])
    padded_sequence = np.concatenate((padded_sequence, np.array([[polarity]])), axis=1)
    
    # Predict and return the model's output
    prediction = model.predict(padded_sequence)
    return prediction
