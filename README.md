# Bike/Scooter price predictive model

This project aims to build a price predictive model for bikes and scooters based on various features present in the dataset. The dataset used for this project was downloaded from Kaggle. The model is built using several libraries such as Pandas, NumPy, Seaborn, Matplotlib, and Scikit-learn. The deployment of the model is done using Flask, HTML, and CSS, and the model is hosted using Render web hosting service.

## Dataset

The dataset used for this project was obtained from Kaggle. It contains information about bikes and scooters, including features like brand, model, mileage, engine capacity, bike/scooter type, top speed and acceleration speed and other relevant attributes. The dataset is preprocessed and cleaned before training the predictive model.

## Libraries Used

- Pandas: Used for data manipulation and preprocessing.
- NumPy: Used for numerical computations and operations.
- Seaborn: Used for data visualization and creating informative plots.
- Matplotlib: Used for creating various types of plots and charts.
- Scikit-learn: Used for building the price predictive model using machine learning algorithms.

## Model Building

The price predictive model is built using machine learning techniques. The dataset is split into training and testing sets, and various algorithms are explored to find the best model for predicting the price of bikes and scooters. The model is trained using the training set and evaluated using the testing set to assess its performance.

## Deployment

The model is deployed using Flask, a Python web framework, along with HTML and CSS for creating the user interface. Flask provides the necessary functionality to serve the model predictions through a web application. Render web hosting service is used to host the model, making it accessible over the internet.

## Project Structure

- data/: Contains the dataset files.
- model_development.ipynb/: Contains the trained predictive model.
- static/: Contains static files such as CSS stylesheets.
- templates/: Contains HTML templates for the web application.
- app.py: The Flask application file that handles the routing and model serving.
- model.pkl: Pickle file of the trained model
- requirements.txt: Lists the required Python packages and versions.

## Conclusion

This project demonstrates the process of building a price predictive model for bikes and scooters using machine learning techniques. By leveraging the dataset downloaded from Kaggle and utilizing libraries like Pandas, NumPy, Seaborn, Matplotlib, and Scikit-learn, the model provides price predictions based on various features. The Flask web application, along with HTML and CSS, allows users to interact with the model and obtain price predictions. The model is deployed and hosted using Render web hosting service, making it accessible over the internet.



