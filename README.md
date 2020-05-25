# SpotifyAPI

We attempted to answer the question "what are the characteristics of a hit song on spotify" 

We used the spotify API to analyse "attributes for songs" 

https://developer.spotify.com/documentation/web-api/

Spotify has created data for various song characteristics some of which are outlined below. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/SpotifyCharacteristics.png)

We collected song attributes based on billboard top one hundred playlists, the current top one hundred and randomly chosen songs. 

We collated data from top 100 billboard charts for years 1975 to 1984 and also from 2000 to 2009. 

We also collected unemployment figures for the years 1975 to  1984 and 2000 to 2009 from the BLS 

https://www.bls.gov/developers/

We looked at the correlation between various characteristics of the present top 100. 

This graph represents average characteristics for different attributes compared between a random sample of 200 songs and the top 100 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Bar%20Plot_Top100%20and%20CG.png)

We noted that accept for "acousticness" and "instrumentalness" the values are remarkeably similar. 
We assumed that because spotify weights popular songs in any search that our "random sample" was not particularly random and probably still contained popular songs and those owned by labels. 

Information, source and code for the random sampling is given here: 

https://github.com/what-makes-a-hit/spotifyAPI/tree/master/randomSpotifySearces

Some of the limitations of the random sampling are discussed further in the links given above. 

Below is a heat map which correlates the different characteristics with each other. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/goodpearsonheatmap.png)

The highest correlation is between danceability and loudness. 

It is the only characteristic correlation which is "strong" ( ie greater than |.07| )

Below is a table of test results correlating the top 100 with 200 randomly chosen songs. 
For each group characteristic values were averaged. 
Using a paired t-test p values were calculated to compare the significance of the difference in mean between groups. 
Statistically significant differences are in bold. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/testresults.PNG)

Danceability, energy, loudness, liveness displayed statistically significant positive correlations. 
Acousticnness displayed a statistically significant negative correlation. 

Here is a plot of Danceability versus Acousticness for the control group. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Danceb%20vs%20Acous_CG.png)

Here is energy vs loudness for the top 100 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Energy%20vs%20Loudness_Top100.png)

We looked at unemployment hoping to find a correlation with something like "valence" ( happiness ) or ( danceability )
Here is a plot of unemployment or the years analysed. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Figure_10.png)

Here is a plot of valence for the periods. 
![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Figure_2.png)

It is hard to see any correlation with unemployment but it does seem that songs are "sadder" in the more recent period. 
I guess millenials are grumpy ! 

This is a graph of loudness. It shows a very obvious trend towards songs getting louder. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Figure_8.png)

This is because over time a competition ensues to get a song louder to "make it a hit" 
We noted that loudness was also positively correlated with a hit song. 

This graph seemed to suggest that perhaps "danceability" is increasing with time. 
Perhaps young people prefer dance music these days. 

![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Figure_3.png)

Finally we present the tempo of average tempo of a "hit song" for multiple years. 
![alt text](https://github.com/what-makes-a-hit/spotifyAPI/blob/master/images/Figure_7.png)


It is surprisingly close to 120 bpm which equates to most peoples ability to jump up and down ( dance ) 

In conclusion based on the data we decided that Danceability, energy, loudness, liveness and Acousticnness are the most important factor in a hit song. The result was limited by the fact that we couldn't find a proper random sample. We also expected that the distribution of data across all groups and the entire spotify data are not normally distributed. The data not being normal would have influenced the value of the t test performed. In the future we hope that it may be possible to create a random sample of the data. 

To view all the images/plot created in this survey click here: 
https://github.com/what-makes-a-hit/spotifyAPI/tree/master/images

The "presentation" folder contains most of the code written to query the spotify API.

"The Sample Guys" team 3/21/2020



