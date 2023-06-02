# CSE163-Project
Title and Authors: 
Understanding Covid-19’s effect on bicycle route usage in Seattle (Fremont, Crown Hill, Belltown, Laurelhurst) 

Annika Halvorson, Ani Ramadurai, Henry Ramstad

https://covid-19-bicycle-route-usage-analysis.onrender.com

Research Question:
The research questions posed by this group fall into two categories: general data analytics, and Covid specific analysis. For general data analytics questions, we are primarily interested in how each sensor's data compares to its fellow sensors regardless of the covid pandemic. This analysis will take a holistic view of each sensor's data over a long period and provide an analysis of why certain sensors may be more popular. The second general question involves asking questions about trends in the data pre, during, and post covid. This second portion involves things like overall trends of bike path use as well as examining if certain months are more popular than others. The second portion of the questioning looks at how Covid has affected the data. For the sake of our analysis, the pandemic began on January 1st, 2020, and ended on January 1st, 2022. This is an oversimplified view of the situation which must be taken to define strict cut-offs between what is and isn't considered part of the pandemic period. The questions posed with these assumptions as how frequency changed for all sensors overall during these periods and how individual sensors may have changed. The direction of this line of questioning is to examine what happened to Seattle bike path usage as a whole and how certain regions gained or lost popularity.
Among the four sensors which one has the most traffic (regardless of the pandemic)?
What are the general trends of the data (trending up, certain months higher) ?
How did the pandemic change the frequency of use overall?
How did the pandemic change individual sensor data?

Motivation: 
Our research questions were motivated by an interest in understanding how the Covid-19 pandemic might have had an impact on the popularity of biking culture in Seattle. We wanted to look at the difference in the traffic trends from the bike counters to understand the health trends that might have been occurring and changing in Seattle during this period. Knowing the health trends in Seattle affects our understanding of how the Covid-19 pandemic impacted health trends all over the country, by focusing on one major metropolitan area. Our research questions focus on looking at the biking trends in Seattle both as a whole, regardless of the pandemic, as well as pandemic-specific information to compare which sensors might have been more popular at a given time. These questions allow us to perform an analysis as to what the impacts of the pandemic might have been, and also how they might have impacted certain areas of Seattle more than others.

Challenge Goals:
The focus of our group's challenge goals is to design visualizations that are beyond the scope of this class. In particular, we want to create GIS-based heatmaps for the different sensors so that users can get a sense of which parts of Seattle are more popular for biking and how these trends have changed over the course of the Pandemic. To harness the combined datasets properly we will need to employ a new library like Plotly, specifically their Mapbox Density Heatmap in Python or Mapbox Choropleth Maps in Python. One of the primary motivations for using Plotly is its ability to be implemented into websites via Dash. Our primary deliverable for this project will be a web-based visualization platform that will allow various charts and graphs to be viewed and manipulated. These goals will stretch our group's understanding of Python by requiring us to learn Plotly’s syntax as well as how to leverage Dash into a webpage. The current plan is to use GitHub pages to provide an interactive and connectable experience without requiring server-side maintenance or domain purchase.

Data Setting:
The dataset we will be using is composed of four different bicycle counter datasets collected by the Seattle Department of Transportation. These datasets include hourly counts of bicyclists crossing various bike trails in the Fremont, Crown Hill, Belltown, and Laurelhurst neighborhoods of Seattle, WA from 2018 to 2022. All data was collected using sensors that were placed on the bike trails. This dataset is open to the public and can be found on the Seattle Government’s Data Portal.

Since we are referring to multiple datasets that cover multiple neighborhoods, it is likely that the bicycle usage patterns vary across each neighborhood due to the differences in infrastructure, demographics, along with other factors. On top of that, factors including weather and the time of day may have different impacts on bicycle usage in these different neighborhoods. However, most importantly, the main factor that may complicate our analysis is the potential impact of COVID-19 on bicycle usage patterns.

To download the datasets, follow these steps:
Go to the Seattle Government’s Data Portal at: https://data.seattle.gov
In the search bar, search for “bicycle counter”
Selected the four datasets titled “Fremont Bridge Bicycle Counter”, “Burke Gilman Trail north of NE 70th St Bicycle and Pedestrian Counter”, “Elliott Bay Trail in Myrtle Edwards Park Bicycle and Pedestrian Counter”, and “NW 58th St Greenway at 22nd Ave NW Bicycle Counter”
Click on the “Export” button and select the format you want to download the dataset in (CSV, JSON, or RDF)
The dataset will be downloaded to your computer.

Method: 
Among the four sensors, which one has the most traffic? (regardless of the pandemic)
Look at which of the four sensors had the most people using it during the 5 year period.
What are the general trends of the data? (trending up, certain months higher)
Look at a line of best fit for the data of the 4 combined sensors to get a sense of the general trend of bike path usage in Seattle, focusing on steepness and accounting for year to year changes.
Look at the bike count by month and compare each, see if any have any specific results (higher or lower)
How did the pandemic change the frequency of use overall?
Analyze how the frequency of the entire bike network changed from the pre-pandemic period to during and after. Highlight how certain parts of the data have large peaks or values and explain why they could exist.
How did the pandemic change individual sensor data?
Calculate the monthly usage trends of data at individual sensors and compare the individual analysis to each other. Look at how one sensor was used more, focusing on individual moments in a sensor's data and relating it contextually to pandemic situations (vaccine roll out, mask mandates, stimulus checks). 

Plan and Development Environment:
Clean and join the data (add GIS location columns and filter) [3-5 hours]
Test combined df for errors [1-2 hours]
Generate plot elements [5-7 hours]
Write web page HTML/CSS [2-3 hours]
Implement plot elements using Dash onto the website [10 hours]

For development purposes, the group plans to meet mid-afternoon on Sundays to discuss development issues or work on larger deliverables. Communication for the work will be done through group SMS, allowing a quick response. 

The environment for development will be VSCode attached with Anaconda using the CSE160 environment. The coding sharing will be managed using a GitHub repository in which all three members will be committing changes to track work.

https://www.seattle.gov/transportation/projects-and-programs/programs/bike-program/bike-counters 
Fremont bridge data 2012 - feb 2023 (47.648116, -122.349834)
https://data.seattle.gov/Transportation/Fremont-Bridge-Bicycle-Counter/65db-xm6k

E 70th burke data (2014 - sept 2022) (47.681344, -122.265128)
https://data.seattle.gov/Transportation/Burke-Gilman-Trail-north-of-NE-70th-St-Bicycle-and/2z5v-ecg8

Belltown myrtle edwards park (2014 - sept 2022) (47.616238, -122.356984)
https://data.seattle.gov/Transportation/Elliott-Bay-Trail-in-Myrtle-Edwards-Park-Bicycle-a/4qej-qvrz

NW 58th St Greenway at 22nd Ave NW (2014 - jul 2022) (47.671213, -122.384746)
https://data.seattle.gov/Transportation/NW-58th-St-Greenway-at-22nd-Ave-NW-Bicycle-Counter/47yq-6ugv


Years of note 2018, 2019, 2020, 2021, 2022
