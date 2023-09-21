

# Swiggy Restaurant Recommendation Model
## Introduction
The "Swiggy Restaurant Recommendation Model" project simplifies the decision making process by utilizing data science and machine learning. This project provides personalized restaurant recommendations to users based on their cuisine preferences and location. It involves web scraping, data cleaning, machine learning modeling, and the development of an interactive web application for an enhanced dining experience.

## 🍽️ Problem Aimed to Solve

In a world where dining preferences and choices are abundant, it can be challenging for individuals to decide where to eat. This project aims to address this problem by developing a Restaurant Recommendation Model. The goal is to provide users with personalized restaurant recommendations based on their cuisine preferences and location. To achieve this, the project involves collecting restaurant data from the Swiggy website, cleaning and preprocessing the data, building a machine learning model for price prediction, and creating an interactive web application for user-friendly recommendations.

## 📋 Project Overview

The project can be divided into several key components:

### 🌐 Data Extraction

- Utilizing web scraping techniques with Selenium to collect comprehensive restaurant data from the Swiggy website. Information includes restaurant names, cuisines, locations, user reviews, and menu prices.
![model_1](https://github.com/Saikiran0432/Swiggy_Restaurent_Recomendation_Model/assets/144260007/9daf1b3e-311c-421d-ab2d-ce9c78952f19)

This code snippet demonstrates the process of web scraping with Selenium to extract essential restaurant data from the Swiggy website. Specifically, it focuses on extracting restaurant names and locations.
The code accomplishes the following:
1. Initializes a WebDriver using Selenium to open the Swiggy website.
2. Utilizes the "find_elements" method with "By.CLASS_NAME" to locate and extract restaurant names and locations.
3. Prints the extracted restaurant names and locations to the console for demonstration purposes.


### 🧹 Data Preprocessing

- Handling noisy data, null values, and duplicates to ensure data quality.
- Conducting outlier analysis to identify and address data points that could affect predictions.

### 📊 Insights and Visualizations

- Exploring and analyzing the collected data to gain insights into restaurant trends, popular cuisines, and price ranges.
- Creating visualizations and dashboards to present these insights to users.
![Ml_2](https://github.com/Saikiran0432/Restaurent_Recomendation_Model/assets/144260007/7d450dbe-6363-4eb4-a1fd-2676ed9147d2)

### 🤖 Machine Learning Modeling

- Building a Random Forest Regressor model to predict restaurant prices based on various factors, including cuisine, location, and user reviews.
- Converting categorical columns into numerical values using Label Encoding for model training.
![ML_1](https://github.com/Saikiran0432/Restaurent_Recomendation_Model/assets/144260007/6976110a-6cd2-405e-bf20-5c06a7047fda)

### 🌐 Web Application

- Developing an interactive web application using Flask that allows users to input their preferences and receive personalized restaurant recommendations.
- Implementing user-friendly features for an enhanced dining experience.
![WhatsApp Image 2023-08-11 at 8 23 00 PM](https://github.com/Saikiran0432/Restaurent_Recomendation_Model/assets/144260007/44493f7f-a8c5-4029-906e-4352e23cc428)

### 🚧 Challenges and Learnings

- Addressing challenges in web scraping, data preprocessing, and model development.
- Learning experiences in data handling and privacy considerations.

### 🚀 Future Scope

- Exploring opportunities for real-time updates in menu prices and user preferences.
- Enhancing the recommendation model with advanced machine learning algorithms.
- Improving the transparency and interpretability of restaurant recommendations.

## 📈 Insights and Visualizations

Exploratory Data Analysis (EDA) and visualizations play a significant role in understanding restaurant data. Some key insights include:

- Ice creams and desserts emerge as the most popular cuisines among users, followed by North Indian and Chinese.
- The analysis also reveals that North Indian cuisine tends to be the most expensive, while fast food and South Indian are generally more budget-friendly.
- ![chart_2](https://github.com/Saikiran0432/Restaurent_Recomendation_Model/assets/144260007/0e101a9a-9965-4a9d-8f0f-3fb07f7898ca)
- Kormangla has high area wise Restaruent distribution than other cities
- ![kormangla](https://github.com/Saikiran0432/Swiggy_Restaurent_Recomendation_Model/assets/144260007/414b595d-b9c8-4cfc-85e3-2f4c87933d1d)


## 📝 Conclusion

In summary, the Restaurant Recommendation Model project addresses the challenge of deciding where to dine by providing personalized recommendations. It involves data extraction, preprocessing, and machine learning modeling to predict restaurant prices. The interactive web application enhances user experience, and visualizations provide valuable insights into restaurant trends. While the project has limitations, it demonstrates the potential of data-driven dining decisions.

---





