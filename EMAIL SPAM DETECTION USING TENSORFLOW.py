import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import pandas as pd

# Sample dataset: replace this with your email data
data = {
    'text': [
        "Win money now!!!",
        "Hi, how are you doing?",
        "Congratulations, you've won a free ticket!",
        "Let's meet for lunch tomorrow.",
        "URGENT! Your account has been compromised.",
        "Can you send me the report?",
        "Get cheap meds online!",
        "Are you coming to the party?"
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 for spam, 0 for ham
}

df = pd.DataFrame(data)

# Tokenize text
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
padded = pad_sequences(sequences, padding='post')

# Split data
X_train, X_test, y_train, y_test = train_test_split(padded, df['label'], test_size=0.2, random_state=42)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=1000, output_dim=16, input_length=padded.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train
model.fit(X_train, y_train, epochs=10, verbose=2)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy:.2f}")

# Predict example
sample_text = ["Congratulations, you have won a free prize!"]
seq = tokenizer.texts_to_sequences(sample_text)
padded_seq = pad_sequences(seq, maxlen=padded.shape[1], padding='post')
prediction = model.predict(padded_seq)
print("Spam" if prediction[0][0] > 0.5 else "Not Spam")
