#Task 1
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']


def keyword_highlighter(reviews):
    for review in reviews:
        upper_reviews = review
        for words in keywords:
            upper_reviews = upper_reviews.replace(words, words.upper())
        print(upper_reviews) #why doesnt return upper_reviews work?