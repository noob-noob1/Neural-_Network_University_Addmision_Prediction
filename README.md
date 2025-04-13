Neural Network Modularization
==============================
This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://neural-networkuniversityaddmisionprediction-hxhlungugd8k7ezo6z.streamlit.app/)

This is an implementation of modulirization for a neural network project

This app predicts whether a student will be admitted to a UCLA or not based on a plathora of different features

## Features

- User-friendly interface powered by Streamlit.
- Input form to enter details such as credit history, loan amount, income, and other relevant factors.
- Real-time prediction of loan eligibility based on the trained model.
- Accessible via Streamlit Community Cloud.

## Dataset
The application is trained on the **UCLA dataset**, a widely used dataset for evaluating creditworthiness. It includes features like:

- GRE_Score: (out of 340)
- TOEFL_Score: (out of 120)
- University_Rating: It indicates the    Bachelor University ranking (out of 5)
SOP: Statement of Purpose Strength (out of 5)
- LOR: Letter of Recommendation Strength (out of 5)
- CGPA: Student's Undergraduate GPA(out of 10)
- Research: Whether the student has Research Experience (either 0 or 1)
- Admit_Chance: (ranging from 0 to 1)

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn**: For model training and evaluation.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Matplotlib** and **Seaborn**: For exploratory data analysis and visualization 

## Model
The predictive model is trained using the UCLA dataset. It applies preprocessing steps like encoding categorical variables and scaling numerical features. The model used is a **MLP classifier**, which is trained using the training data and evaluated on the testing data. The model's performance is assessed using accuracy.

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/noob-noob1/Neural-_Network_University_Addmision_Prediction.git
   cd credit_eligibility_application

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run streamlit_app.py




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
