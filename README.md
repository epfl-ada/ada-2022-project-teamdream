# Project - TeAmDreAm

Joanne Affolter, Anne de Sacy, Amine Lamouchi, Antoine Munier

## Abstract 
<br>
Our objective is to give an overall analysis of the beer market.
To do so we imagine being a data analysis company.
In that context we were contacted by a businessman that wanted to open a brewery.
<br><br>
As the majority of ratings are coming from the US on both RateBeer and BeerAdvocate, we were interested in studying that country in particular.
Moreover, recently the local-oriented breweries have gained popularity in the US.
These are the reasons why we decided that our client wants to start a local brewery in the US.
<br><br>
Then our idea is to have an overall analysis of the whole country to determine which state is the most suited to install a new brewery.
Especially we analyzed the concurrent local breweries according to the number of ratings.
We were then able to suggest a state where our client could start a flourishing business.
<br><br>
With that particular state we performed a more in-depth analysis of the local customers preferences.
As our client already has an idea to create a new beer we tested the popularity of it compared to the actual beers in the market.
We were then able to advise him on some improvements and characteristics to focus on for developing other beers.
Looking at the preferred styles in the state we also gave him additional recommendations.
<br><br>

## Research Questions
<br>
Part 1 - Overview of the beer reviews websites<br>
- Where do consumers mainly come from ?<br>
- How does the consumers behaviour evolved through time ?<br>
- Does the 2012/2015 hype of discovering new beers had an impact on breweries ?
<br><br>
Part 2 - Competitive state analysis<br>
- Where is the best place to open a brewery ?<br>
- Which are the states with a large market share to reach ?<br>
- Where are the local beer lovers ? Where are the real beer fans who make a lot of ratings ?<br>
- Which breweries are our client's competitors?
<br><br>
Part 3 - Strategic advice for market positioning in Virginia<br>
- Will our client beer be a unique product in Virginia ? Are there beers similar to mine ?<br>
- What are the most succesful beers/breweries in Virginia ? What is the aspect in which these beers excel (taste, palate) ?<br> 
- What aspects of the beer profile are most important (e.g. : is taste more important than palate) ?
<br><br>

## Proposed additional datasets
<br>

1. **Beer analytics**
[BeerAnalytics](https://www.beer-analytics.com/styles/ipa/specialty-ipa/)<br>
This dataset gives us information about the popularity over time for each style of beer. <br>


## Methods

**Part 1 - Overview of the beer reviews websites**<br>
**Aim:** Have a first global analysis of the websites<br>
In this part we first managed to extract useful information from the huge ratings files by splitting the files.<br>
Then we explore a little the data obtained. 
We have seen that the number of ratings posted by US users is much higher than from other countries. 
For this reason we decided to focus our analysis on that country.<br>
Then we looked at the evolution of the beer industry over the years on both websites.
<br><br>

**Part 2 - Competitive state analysis**<br>
**Aim:** Determine which state is the best open a brewery and who are our client's competitors<br>
We looked at various criterias to determine that state. 
First, if there is a large market share to reached and a large number of users on the websites.
Then, if there are consumers who like local beers.
Finally, if there are beer enthusiasts who make a large number of ratings on the review sites and who can be reached by our client's products.
<br>
Afterwards, having filtered out a few state where our client might succeed we look through the breweries that would then compete against our client.
By analysing the biggest breweries and the most local-oriented ones 
we identified the state were there would be less competition and therefore were our client would have more chance of succeeding.
<br>

**Part 3 - Strategic advice for market positioning in Virginia**<br>
**Aim:** Advice our client on the products to sell in his brewery<br>
In this part we need to represent beers in a space that has a notion of distance. 
If we can represent each beer as a vector, then we can run clustering algorithms like K-Means to find beers that are similar to each other. 
Or we can run K-Nearest Neighbours to find the beers that are most similar to ours.
<br>
On the same note, we can draw the word-cloud of the textual reviews associated to the beer, it will give the most commonly mentioned words.
For each beer we can run linear regression and compare the coefficients associated to each aspect. 
We start by learning a function of which the biggest coefficient gives us the most decisive aspect of the beer rating.
<br>
Measuring the success of a beer is simple, we just look at the proportion of high ratings.
<br>
Following that representation we were able to advice our client on which beer styles to sell and with which characteristics to focus on.


## File structure

We put all our analysis in the notebook `FinalNotebook.ipynb`.<br>
We extracted some data from the provided files and created databases that can be used.
<br>
For overview of the ratings with extracted columns 
``beer_id``, ``date``, ``rating``, ``appearance``, 
``aroma``, ``palate``, ``taste``, ``overall`` :
- data/BeerAdvocate/ratings_overview_ba.csv
- data/RateBeer/ratings_overview_rb.csv
