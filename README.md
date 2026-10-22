## AI-Based Road Accident Severity Prediction

## Project Overview

AI-Based Road Accident Severity Prediction is a Deep Learning project that predicts road accident severity using accident-related, weather, road, and time information.

The project uses the US Accidents dataset and an Artificial Neural Network (ANN) built with PyTorch. A Streamlit web application provides a simple and interactive interface for users to enter accident details and view the predicted severity.

## Live Demo

Streamlit App: [https://jasla123-accident-severity-deep-learning-app-zxccsc.streamlit.app/]

## Objectives

- Predict road accident severity using accident-related features.
- Explore the relationship between road conditions, weather, and accident severity.
- Apply Deep Learning techniques to a real-world dataset.
- Deploy the trained model as an interactive web application.

## Dataset

- Dataset: US Accidents Dataset
- Original dataset size: Approximately 7.7 million records
- Severity classes: 1, 2, 3, and 4
- Training sample: 200,000 records, with 50,000 records selected for each severity class.

Severity represents the accident severity category in the dataset.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- PyTorch
- Streamlit
- Joblib
- Matplotlib and Seaborn

## Project Workflow

1. Data Collection: Used the US Accidents dataset.
2. Data Preprocessing: Handled missing values and prepared numerical and categorical features.
3. Feature Engineering: Extracted hour, month, and day of the week from the accident start time.
4. Feature Scaling and Encoding: Applied StandardScaler to numerical features and OneHotEncoder to categorical features.
5. Model Building: Developed an Artificial Neural Network (ANN) using PyTorch.
6. Model Evaluation: Evaluated the model using accuracy, precision, recall, F1-score, and a confusion matrix.
7. Deployment: Integrated the saved model and preprocessing objects into a Streamlit application.

## Deep Learning Model

The project uses an Artificial Neural Network with the following architecture:

- Input layer: 153 processed features
- Hidden layer 1: 128 neurons
- Hidden layer 2: 64 neurons
- Hidden layer 3: 32 neurons
- Output layer: 4 neurons

Activation function: ReLU
Loss function: Cross-Entropy Loss
Optimizer: Adam
Framework: PyTorch

Dropout layers are used to help reduce overfitting.

## Streamlit Application

The web application allows users to enter available accident details, including:

- Accident location coordinates
- Distance
- Weather conditions
- Temperature, humidity, and wind information
- Road features, such as junctions and traffic signals
- Accident time-related information

After clicking Predict Severity, the application displays the predicted severity class and class probability estimates.

## Model Performance

The model achieved approximately 46.38% test accuracy on the test set.

The model's performance varies across severity classes. Further improvements are needed before it can be considered reliable for real-world use.

## Project Files

- "app.py" — Streamlit application
- "requirements.txt" — Required Python packages
- "accident_severity_model.pth" — Saved PyTorch model
- "preprocessor.joblib" — Saved preprocessing pipeline
- "feature_columns.joblib" — Saved feature column information
- "*.ipynb" — Jupyter Notebook containing the project workflow

Note: File names and folders may vary depending on the repository structure.

## How to Run Locally

1. Clone the repository:
   
   git clone <your-github-repository-url>

2. Navigate to the project folder:
   
   cd <your-project-folder>

3. Install the required packages:
   
   pip install -r requirements.txt

4. Run the Streamlit application:
   
   streamlit run app.py

## Future Improvements

- Improve prediction performance across all severity classes.
- Explore class imbalance handling and model optimization techniques.
- Evaluate additional machine learning and deep learning models.
- Validate the model on suitable real-world data.
- Improve the user interface and input validation.

## Limitations

This project is developed for educational and research purposes. Predictions are estimates based on the trained model and dataset. The application should not be used as the sole basis for emergency response or real-world road safety decisions.

