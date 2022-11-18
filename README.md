# Project - TeAmDreAm

Joanne Affolter, Anne de Sacy, Amine Lamouchi, Antoine Munier

## Abstract 

Our idea is to analyze the relation between football world-cups and beer ratings to evaluate the impact of this huge event on beer consumers. <br>
More specifically we will search if world-cups affect beers or breweries' popularity, beer consumption and consumers opinion.

First of all, looking at the most rated beers and breweries we will see if there is a correlation between world-cups and ratings.

Then, we will analyze the ratings and reviews in a range of one month around the event. Our goal is to understand the variation in ratings and reviews between winning and losing countries.<br>
We will analyze the trends depending on the team's results. And use sentiment analysis to highlight positive and negative emotions that the result of a game can bring out in fans and therefore affect reviews.

Finally, the whole process will enable us to evaluate how to adapt the sales depending on the results.

## Research Questions

- Do the breweries sponsoring world cups earn a positive or negative impact from that marketing campaign ?
- Is there a correlation between rating and review date during the different world cups ?

- Can we observe a difference in consumption between the users of countries that win/lose a match ?
- Do the winning/losing nations drink the same beer when they win/lose ? Does their consumption increase or decrease ?
- Are the comments' emotional tone reflecting the result of a game ? 

- Which is the best beer to sell to each country if they win the world cups ?

## Proposed additional datasets

1. Beer analytics

This dataset gives us information about the popularity over time for each style of beer. <br>
It could be interesting to analyze that information to see if some particular style is popular during a world cup.<br>
Therefore we have a clue on which beers might have the better ratings.

2. OpenFootball WorldCup

In this dataset we have the information about all world cup games and results. <br>
It will give us the winning and losing countries for each game telling us which countries to look at.

## Methods

First of all we will pre-process the data to extract the interesting features.<br>
To start our preprocessing we first have explored the matched_data and the other two datasets to determine which one to work on.
Our analyze has shown that the matched_data did not contain enough data for us to work on it.<br>
Then we managed to read the ratings file from both websites (RateBeer and BeerAdvocate) and extract the ratings date.
We completed the beers data from each websites with the number of ratings on each beer and the dates of ratings.<br>

In continuation of our project we plan to use various methods :<br>
Our main objective is to analyze variation through time, therefore we will use time series methods.<br>
We will perform statistical tests on our data and results to ensure our conclusions.<br>
To analyze reviews we will use NLP methods and sentiment analysis. <br>
We can also use clustering to see if reviews with the same connotations were posted around the same time.

## Proposed timeline

### Week 1 : 21/11 - 28/11

| Task                                                                                                    | Team member(s)    | Week           |
|---------------------------------------------------------------------------------------------------------|-------------------|----------------|
| Pre processing the data                                                                                 | Joanne and Anne   | up to 18/11    |
| First analysis                                                                                          | Amine and Antoine | up to 18/11    |
| Global and temporal analysis                                                                            | All               | 19/11 to 04/12 |
| Process reviews, find NLP algorithms                                                                    | Amine             | 28/11 to 04/12 |
| Zoom on the period of the football world cups and finest analysis of beer reviews and consumption rates | All               | 05/12 to 18/12 |


