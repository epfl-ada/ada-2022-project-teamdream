# Project - TeAmDreAm

Joanne Affolter, Anne de Sacy, Amine Lamouchi, Antoine Munier

## Abstract 

Our idea is to analyze the relation between major sporting events (football world-cups, superbowl, etc.) and beer ratings to evaluate the impact of these huge events on beer consumers and breweries' sales. <br>
More specifically we will search if those sporting events affect beers or breweries' popularity, beer consumption and consumers opinion.

First of all, we will look at the most rated beers and most popular breweries to determine if there exists any temporal correlation between some major sporting events and the popularity of the studied beers/breweries.
*For instance, can we observe a peak every 4 years in the consumption of beers from a certain brewery?*

Then, we will analyze the ratings and reviews in a range of one month around the events which have caught our attention in the first part of the project. Our goal is to understand the variation in ratings and reviews between winning and losing countries.<br>
We will analyze the trends depending on the team's results. We will also look for the effect of these events in the textual reviews by leveraging sentiment analysis.

Finally, the whole process will enable us to evaluate how to adapt the sales of breweries depending on the results.

## Research Questions

- Is there a temporal correlation between the ratings dates and major sporting events ?
- Can we observe a difference in consumption between the users of countries that win/lose a match ?
- Do the winning/losing nations drink the same beer when they win/lose ? Does their consumption increase or decrease ?
- Can textual reviews provide an additional metric for beer popularity in relation to sporting events ?
- Do the breweries sponsoring sporting events earn a positive or negative impact from that marketing campaign ?
- Can we tell which beer to sell to each country depending on the results of given sporting event ?

## Proposed additional datasets

1. **Beer analytics**
[BeerAnalytics](https://www.beer-analytics.com/styles/ipa/specialty-ipa/)<br>
This dataset gives us information about the popularity over time for each style of beer. <br>
It could be interesting to analyze that information to see if some particular style is popular during a major sporting event.<br>


2. **History of SuperBowl**
[History of SuperBowl](https://data.world/sports/history-of-the-super-bowl/workspace/file?filename=Super_Bowl.csv)<br>
In this dataset we can find information about all the past SuperBowls. <br>
It also provides information about results of state teams in the US. This is particularly important to study the reviews from the US since it is the only country whose reviews are recorded per state (the number of said reviews is also very significant)

3. **NBA Playoffs**<br>
This dataset contains information about the NBA Playoffs winner and games.
We can use this data as a source of sporting events

## Methods

Our project is divided into 3 parts :<br> 
**1. Data pre-processing**<br>
**Aim:** Determine which breweries are the most suitable to be sponsors of major sporting events.<br>
During this part, we pre-process the data to extract the features needed for the project.<br>
We first have explored the matched dataset and the other two datasets to determine which one to work on.
Our analyze has shown that the matched dataset did not contain enough data for us to work on it. We will therefore work on the datasets from each website individually.<br>
Then we managed to read the ratings file from both websites (RateBeer and BeerAdvocate) and extract the ratings date.
We merged these dates to the beers dataset from each website. We also added the location of each brewery.<br>
One important part of our pre-processing was to filter the data in order to work only with the most popular beers (i.e. with the highest number of ratings) and therefore with the breweries who could be sponsors of such events.

**2. Temporal analysis of the popularity of biggest breweries and the impact of major sporting events on their sales**<br>
**Aim:** Find a temporal link between the consumption of  beers of the breweries selected in the pre-processing part  and major sporting events 
<br>
We will look at the evolution over time of the number of ratings and search for some peaks in the data during particular events (Football World Cups, Euro, Super Bowl).
We will group the data in different ways and analyze its temporal evolution to understand how beers' popularity and these events are correlated. 
*Does a particular **style** stand out during this period? Are the number of comments on a certain **brewery**'s beers increasing? Is it a sponsor of that event? What about the beer consumption in the **country** hosting such events?*<br>
Our main objective is to analyze variation through time, therefore we will use time series methods. We will also perform statistical tests on our data to ensure our conclusions.<br>
We started to analyze the evolution of the top 10 beers and breweries to get a general idea and determine if our project was feasible. We are satisfied with these first results because we do observe peaks in the number of comments on the beers studied during the World Cup period in 2014.


**3. Textual Data Analysis**
**Aim:** Study whether textual reviews can be used to measure beer popularity<br>
Our goal for this part is to analyze the textual reviews and see if we can derive insights from them. In particular, we aim at predicting whether a given review has a positive or negative sentiment. We think that by considering the sentiment associated to a review, we can study the popularity of certain beers better than just by looking at the numerical ratings. The intuition behind this is that a textual review is a richer source of information than a rating between 0 and 5. We hope that by leveraging sentiment analysis, we can encapsulate this additional information and use it as an additional measure for beer popularity. We therefore present a first implementation of a pipeline that:


        - Extracts textual reviews from the dataset
        - Annotates the reviews (positive/negative for later training) using the ratings 
        - Represents each review in an embedding space
        - Trains a classifier on the review embeddings
        - Uses the classifier to predict the sentiment of a given review
        - Provides a ranking of beer popularity based on sentiment analysis

In particular, we will look at the top 10 countries with highest review output and try to find their (semantically) most popular beer. As mentioned above, we have yet no reason to believe that this ranking is more "useful" than a rating-based ranking, we just want to study to what extent these two are different for now. 



## File structure
In order to make our proposal clearer, we have decided to separate our first analyses into three notebooks, one for each part. 
- `pre_processing.ipynb`: part 1 
- `temporal_analysis.ipynb`: part 2
- `textual_reviews_analysis.ipynb`: part 3

The datasets that we will use are stored into the zip file `final`
In that file we put the result of our pre-processed data (part 1).

## Website URL 
[Beer Reviews](https://cerulean-pavlova-66ae22.netlify.app)
## Proposed timeline

| Task                                                                        | Team member(s)    | Week           |
|-----------------------------------------------------------------------------|-------------------|----------------|
| Data pre-processing.                                                        | Joanne, Anne      | up to 18/11    |
| Exploratory analysis and checking feasibility of part 2.                    | Antoine, Joanne   | up to 18/11    |
| Processing textual reviews and checking feasability of part 3.              | Amine             | up to 18/11    |
| Integrate additional datasets                                               | All               | 28/11 to 04/12 |
| Develop temporal and textual analysis                                       | All               | 05/12 to 18/12 |
| Formulate data story into website                                            Joanne            | 14/12 to 25/12 |
