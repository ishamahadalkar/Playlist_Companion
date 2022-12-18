# Isha Mahadalkar (imahadal@purdue.edu) 

# Writing a program that computes the similarity scores between one selected song and all the other songs
# to find the songs that are the most similar using its attributes. 
# Also creating a cluster of similar songs with a fixed value of K

# Input: Songs Data - songs-data.csv

# Output: 1. List of songs similar to a selected song.
# 2. Cluster of similar songs using K Means CLustering. 

import pandas as pd
import numpy as np
import random as rand
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Reading in the Songs data

df = pd.read_csv('songs-data.csv')


# Finding the cosine similarity of one song with all the other songs
attributes = df.loc[:,'Danceability':]
attributes = attributes.apply(pd.to_numeric)

# Similarity Matrix
similarity = cosine_similarity(attributes)

# Sorting the selected song list and returning the index positions uisng descending similarity scores
# Currently selecting 'Dynamite' by BTS which has an Index of 1841

print("\nCurrently analyzing 'Dynamite' by BTS\n")

np_array = np.array(similarity[1841])
sorted_index_pos = [index for index, num in sorted(enumerate(np_array), key=lambda x: x[-1], reverse=True)]

# Finding the 7 most similar songs to the selected song
similar_songs_index = sorted_index_pos[:8]
similar_songs = df.loc[df['Index'].isin(similar_songs_index)]

# Showing the selected song and the 6 songs most similar to this song
print("Most Similar Songs")
print(similar_songs)

# Currently selecting 'Money Trees' by Kendrick Lamar ft. Jay Rock which has an Index of 4205

print("\nCurrently analyzing 'Money Trees' by Kendrick Lamar ft. Jay Rock\n")

np_array = np.array(similarity[4205])
sorted_index_pos = [index for index, num in sorted(enumerate(np_array), key=lambda x: x[-1], reverse=True)]

# Finding the 6 most similar songs to the selected song
similar_songs_index = sorted_index_pos[:9]
similar_songs = df.loc[df['Index'].isin(similar_songs_index)]

# Showing the selected song and the 6 songs most similar to this song
print("Most Similar Songs")
print(similar_songs)

# Currently selecting 'Dancing Queen' by ABBA which has an Index of 1488

print("\nCurrently analyzing 'Dancing Queen' by ABBA\n")

np_array = np.array(similarity[1488])
sorted_index_pos = [index for index, num in sorted(enumerate(np_array), key=lambda x: x[-1], reverse=True)]

# Finding the 6 most similar songs to the selected song
similar_songs_index = sorted_index_pos[:7]
similar_songs = df.loc[df['Index'].isin(similar_songs_index)]

# Showing the selected song and the 6 songs most similar to this song
print("Most Similar Songs")
print(similar_songs)

# K Means Clustering
# Initialize the class object
kmeans = KMeans(n_clusters= 3, random_state=0)

# Predict the labels of the clusters using the song attributes and return the array of cluster labels 
# each data point belongs to 
df['cluster'] = kmeans.fit_predict(attributes)
 
# Get centroids
centroids = kmeans.cluster_centers_
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]
# Add to df
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})
# define and map colors
colors = ['#DF2020', '#81DF20', '#2095DF']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})
 
# Results:
fig, ax = plt.subplots(1, figsize=(8,8))

# Remove this line below if you want to plot all the songs
# df = df.loc[df['Index'].isin(similar_songs_index)]


# Songs by Popularity
plt.scatter(df.Year, df.Popularity, c=df.c, alpha = 0.6, s=10)
# Create a list of legend elements
# Markers
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Cluster {}'.format(i+1), 
               markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]
# Plot legend
plt.legend(handles=legend_elements, loc='upper right')
# title and labels
plt.title('Popular Songs by Year\n', loc='left', fontsize=22)
plt.xlabel('Year')
plt.ylabel('Popularity')

plt.show()

# Songs as Clusters 
plt.scatter(df.Danceability, df.Popularity, c=df.c, alpha = 0.6, s=10)
# create a list of legend elemntes
## markers / records
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Cluster {}'.format(i+1), 
               markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]
# plot legend
plt.legend(handles=legend_elements, loc='upper right')
# title and labels
plt.title('Popular Songs by Danceability\n', loc='left', fontsize=22)
plt.xlabel('Danceability')
plt.ylabel('Popularity')

plt.show()

