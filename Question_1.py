#Task 1
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']


def keyword_highlighter(reviews):
    for review in reviews:
        upper_reviews = review #why do I need to make this a different variable?
        for words in keywords:
            upper_reviews = upper_reviews.replace(words, words.upper())
        print(upper_reviews) #why doesnt return upper_reviews work?


#Task 2
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']



positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def keyword_highlighter(reviews):
    for review in reviews:
        upper_reviews = review
        for words in keywords:
            upper_reviews = upper_reviews.replace(words, words.upper())
            

    positive_count = 0
    negative_count = 0

    if words in positive_words:
        positive_count += 1
    elif words in negative_words:
        negative_count += 1

        print(upper_reviews) #why doesnt return upper_reviews work?
        print(f"There were {positive_count} positive reviews and {negative_count} negative reviews")
    

print(keyword_highlighter(python_reviews))