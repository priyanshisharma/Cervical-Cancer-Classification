# Cervical-Cancer-Classification
This is the Capstone Project of my Machine Learning Engineer with Microsoft Azure Nanodegree Program by Udacity.

I use an external dataset in our Machine Learning Workspace, and train the model using different tools available in the Microsoft Azure Workspace. I created two models, one using Automated ML module by Microsoft Azure and one Linear Regression model whose hyperparameters are tuned using HyperDrive. I find out the accuracy by the *** model created by AutoML to be *** and the Linear Regression model as *** . Furthermore, I deploy the better performing model as a web service using the Azure ML Framework.

<img href="/images/capstone-diagram.png"/>

## Dataset

### Overview
Cervical cancer is a type of cancer that occurs in the cells of the cervix — the lower part of the uterus that connects to the vagina. It isn't clear what causes cervical cancer, but it's certain that HPV plays a role. HPV is very common, and most people with the virus never develop cancer. This means other factors — such as your environment or your lifestyle choices — also determine whether you'll develop cervical cancer.

<img href="/images/cervical-cancer.jpeg"/>

We're using the [UCI's Machine Learning repository's Cervical cancer (Risk Factors) Data Set](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29). The dataset was collected at 'Hospital Universitario de Caracas' in Caracas, Venezuela. The dataset comprises demographic information, habits, and historic medical records of 858 patients. Several patients decided not to answer some of the questions because of privacy concerns (missing values).

**Citation: Kelwin Fernandes, Jaime S. Cardoso, and Jessica Fernandes. 'Transfer Learning with Partial Observability Applied to Cervical Cancer Screening.' Iberian Conference on Pattern Recognition and Image Analysis. Springer International Publishing, 2017.**

### Task
Our target variable here is **Biopsy**. Biopsy is a sample of tissue taken from the body in order to examine it more closely. A doctor should recommend a biopsy when an initial test suggests an area of tissue in the body isn't normal. Doctors may call an area of abnormal tissue a lesion, a tumor, or a mass.
Here this categorical variable contains the *Biopsy Test Result*.

### Access
The dataset maybe accessed via the `.csv` file given [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv). This dataset has a lot of missing values due to the privacy concerns of participants which hindered proper usage. This was fixed with reference to the [Kaggle Notebook](https://www.kaggle.com/senolcomert/cervical-cancer-risk-classification#6.-Missing-Value) by [Senol Cmrt](https://www.kaggle.com/senolcomert).

This cleaning maybe observed in the `data-cleaning.ipynb` file in this notebook.

## Automated ML
I used the following setting for my automl experiment.

* Since we're working on a small dataset, about 30 mins should be enough to reach the best performing model, and that is why we set `experiment_timeout_minutes` as 30.
* Since our Compute has 4 nodes we're going for 4 `max_concurrent_iterations`.
* In order to minimise *overfitting* we're using 3 Cross Validation (`n_cross_validations`).
* Since we're working with medical data, *accuracy* is of utmost importance, hence we choose it as the `primary_metric`.

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?



*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
Being a classification problem, I used **Logistic Regression** (read `train.py` for greater insight) whose hyperparameters are tuned using the following configuration.

**Bandit Policy** <br/>
Bandit policy is based on slack factor/slack amount and evaluation interval. Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run. Unlike Truncation policy it doesn't calculate primary metric for all runs only to delete a percentage of them, but termminate it as soon as the primary metric doesn't satisfy slack amount, omitting unnecessary baggage. It also omits the need to calculate running Median, making it less computationally cumbersome unlike MedianStoppingPolicy.

**Random Parameter Sampling** <br/>
Random sampling supports discrete and continuous hyperparameters. In random sampling, hyperparameter values are randomly selected from the defined search space. It supports early termination of low-performance runs. Unlike other methods, this gives us a wide exploratory range, which is good to do when we don't have much idea about the parameters. It can also be used do an initial search with random sampling and then refine the search space to improve results.

**Accuracy** is the proximity of measurement results to the true value. Being medical data, being correct is important, being even slightly misguided can have disastrous consequences. I have hereby chosen *Accuracy* as my primary metric.

### Results

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.