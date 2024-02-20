# Data-Infused Playlist Companion

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ishamahadalkar/Nashville_Housing">
    <img src="logo_playlist.png" height="350px" alt="Logo" >
  </a>
  
<!-- Section Name tag -->
<a name="#about-the-project"></a>
<h3 align="center">Analysis and Recommemder System based on your listening habits.</h3>

  <p align="center">
    The Data-Infused Playlist Companion project endeavors to construct a music recommender system using Spotify datasets, aiming to enhance music discovery and connection based on individual listening habits. The project explores the profound impact of music on personal identity and relationships, utilizing data analysis techniques to uncover patterns and preferences within music consumption.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#data-sources">Data Sources</a>
      <ul>
          <li><a href="#preprocessing">Preprocessing</a></li>
      </ul>
    </li>
    <li><a href="#approach">Approach</a></li>
    <li><a href="#code-structure">Code Structure</a></li>
    <li><a href="#lessons-learned">Lessons Learned</a></li>
    <li><a href="#future-work">Future Work</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- Section Name tag -->
<a name="#built-with"></a>

### Built With

* [![Python][python-badge]][python-url]
* [![Pandas][pandas-badge]][pandas-url]
* [![Matplotlib][matplotlib-badge]][matplotlib-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get started with the project, follow these steps:

<!-- Section Name tag -->
<a name="#getting-started"></a>

### Prerequisites

<!-- Section Name tag -->
<a name="#prerequisites"></a>

- Installation of Python for algorithm development and data analysis tasks.
- Familiarity with Matplotlib for generating static visualizations.

### Installation

<!-- Section Name tag -->
<a name="#installation"></a>

1. Clone the repo
   ```sh
   git clone https://github.com/ishamahadalkar/Playlist_Companion
   ```
 2. Python: Install Python from the official website and set up the required libraries for data analysis and visualization.
 3. Matplotlib: Install Matplotlib using pip or conda package managers.
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DATA SOURCES -->
## Data Sources

<!-- Section Name tag -->
<a name="#data-sources"></a>

The project utilizes two primary datasets sourced from Kaggle:

1. "Spotify Top Chart Songs 2022": Provides insights into weekly top chart songs collected from Spotify's global charts.
2. "Spotify 2000's MegaSet Data": A larger dataset comprising 54,000 songs from diverse regions for in-depth analysis.

### Preprocessing

<!-- Section Name tag -->
<a name="#preprocessing"></a>

Initial data preprocessing involves:

- Removal of duplicate entries.
- Elimination of rows with missing or incorrect values.
- Filtering out songs with a popularity index below 70 (out of 100).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- APPROACH -->
## Approach

<!-- Section Name tag -->
<a name="#approach"></a>

The project adopts a multifaceted approach, involving:

1. Algorithm Development: Python program for computing similarity scores and forming clusters using K Means Clustering.
2. Data Visualization: Utilization of Matplotlib for generating static radar charts and scatterplots to visualize music data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CODE STRUCTURE -->
## Code Structure

<!-- Section Name tag -->
<a name="#code-structure"></a>

The project's code structure involves:

- cluster.py: Python scripts for algorithm development and data analysis.
- CSV and Excel files that have the data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Lessons Learned -->
## Lessons Learned

<!-- Section Name tag -->
<a name="#lessons-learned"></a>

- Navigating Large Datasets with Python, Pandas, and NumPy: Delving into sizable datasets taught us invaluable skills in handling vast amounts of data efficiently. Through the powerful libraries of Python, namely Pandas and NumPy, we learned techniques to manipulate, analyze, and extract insights from extensive datasets, fostering a deeper understanding of data processing and management.

- Exploring Clustering Algorithms: Our exploration into clustering algorithms provided a deeper understanding of unsupervised learning techniques, enabling us to identify patterns and structures within data. By experimenting with algorithms such as K Means Clustering, we gained insights into grouping similar data points, facilitating more nuanced analysis and interpretation of complex datasets.

- Utilizing Radar Charts for Visualizations: Incorporating radar charts into our visualizations enhanced our ability to represent multidimensional data effectively. By visualizing multiple attributes simultaneously, we were able to grasp the relationships and variations within datasets more intuitively, enabling clearer insights and communication of findings.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE WORK -->
## Future Work

<!-- Section Name tag -->
<a name="#future-work"></a>

1. Interactive Application Development: Enhance user engagement through the development of an interactive application using Processing and D3.
2. Real-time Data Integration: Integrate the Spotify API for real-time data retrieval, enhancing the accuracy of music recommendations.
3. Database Management: Implement SQL for efficient database management, supporting the recommender system's functionality.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

<!-- Section Name tag -->
<a name="#license"></a>

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<!-- Section Name tag -->
<a name="#contact"></a>

Your Name - [@LinkedIn]([linked-url]) - mahadalkar.isha@gmail.com

Project Link: [https://github.com/ishamahadalkar/Academic_Prediction](https://github.com/ishamahadalkar/Academic_Prediction)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<!-- Section Name tag -->
<a name="#acknowledgments"></a>

We would like to acknowledge Kaggle for providing the datasets used in this project, as well as the developers of Python, Matplotlib, Processing, and D3 for their invaluable contributions to the field of data analysis and visualization.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[repository-name]: https://github.com/ishamahadalkar/Academic_Prediction
[contributors-shield]: https://img.shields.io/github/contributors/ishamahadalkar/Academic_Prediction.svg?style=for-the-badge
[contributors-url]: https://github.com/ishamahadalkar/Academic_Prediction/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ishamahadalkar/Academic_Prediction.svg?style=for-the-badge
[forks-url]: https://github.com/ishamahadalkar/Academic_Prediction/network/members
[stars-shield]: https://img.shields.io/github/stars/ishamahadalkar/Academic_Prediction.svg?style=for-the-badge
[stars-url]: https://github.com/ishamahadalkar/Academic_Prediction/stargazers
[issues-shield]: https://img.shields.io/github/issues/ishamahadalkar/Academic_Prediction.svg?style=for-the-badge
[issues-url]: https://github.com/ishamahadalkar/Academic_Prediction/issues
[license-shield]: https://img.shields.io/github/license/ishamahadalkar/Academic_Prediction.svg?style=for-the-badge
[license-url]: https://github.com/ishamahadalkar/Academic_Prediction/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/isha-mahadalkar

[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[scikit-learn-badge]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
[pandas-badge]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[numpy-badge]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[matplotlib-badge]: https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white
[seaborn-badge]: https://img.shields.io/badge/Seaborn-008ABC?style=for-the-badge&logo=seaborn&logoColor=white

[python-url]: https://www.python.org/
[scikit-learn-url]: https://scikit-learn.org/
[pandas-url]: https://pandas.pydata.org/
[numpy-url]: https://numpy.org/
[matplotlib-url]: https://matplotlib.org/
[seaborn-url]: https://seaborn.pydata.org/


