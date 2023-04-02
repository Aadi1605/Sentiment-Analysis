from textblob import TextBlob

# Define a function to perform sentiment analysis
def sentiment_analysis(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    # Get the sentiment polarity (range from -1 to 1)
    sentiment_polarity = blob.sentiment.polarity
    # Classify the sentiment as positive, negative or neutral
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    # Return the sentiment
    return sentiment

# Test the function
text = "I love this product! It's amazing."
sentiment = sentiment_analysis(text)
print(sentiment) # Output: Positive
