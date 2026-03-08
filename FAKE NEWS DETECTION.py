import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Sample dataset (replace with your data)
texts = [
    "The economy is growing fast",           # Real
    "Aliens have landed in New York",        # Fake
    "The stock market hits record highs",   # Real
    "Celebrity caught in scandal!",          # Fake
    "Scientists discover new species",       # Real
    "Government hides secret UFO files",     # Fake
]
labels = [0, 1, 0, 1, 0, 1]  # 0 = Real, 1 = Fake

# Parameters
vocab_size = 1000
embedding_dim = 16
max_length = 20
padding_type = 'post'
trunc_type = 'post'
oov_token = "<OOV>"
training_portion = 0.8

# Tokenize texts
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# Convert labels to numpy array
labels = np.array(labels)

# Split training and validation data
train_size = int(len(texts) * training_portion)
train_padded = padded[:train_size]
train_labels = labels[:train_size]
val_padded = padded[train_size:]
val_labels = labels[train_size:]

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Train model
model.fit(train_padded, train_labels, epochs=10, validation_data=(val_padded, val_labels))

# Example prediction
test_text = ["Secret documents reveal scandal"]
test_seq = tokenizer.texts_to_sequences(test_text)
test_pad = pad_sequences(test_seq, maxlen=max_length, padding=padding_type)
prediction = model.predict(test_pad)

print(f"Prediction (0=Real, 1=Fake): {prediction[0][0]:.4f}")
