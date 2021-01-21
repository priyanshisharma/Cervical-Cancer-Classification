# Cervical Cancer Classification
This is the Capstone Project of my Machine Learning Engineer with Microsoft Azure Nanodegree Program by Udacity.

I used an external dataset i.e. (Cervical Cancer Risk Classification)[https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29] dataset in our Machine Learning Workspace, and trained the model using different tools available in the Microsoft Azure Workspace. I created two models, one using *Automated ML* module by Microsoft Azure and one Logistic Regression model whose hyperparameters are tuned using *Hyperdrive*. I compared their performance on the basis of their respective Weighted Average Precision Score wherein the score of the Voting Ensemble model created by AutoML was found to be 0.9150 and the Logistic Regression model as 0.098. Furthermore, I deploy the better performing model i.e. clearly the Voting Ensemble model as a web service using the Azure ML Framework. 

<img src="/images/capstone-diagram.png"/>

## Dataset

### Overview
Cervical cancer is a type of cancer that occurs in the cells of the cervix — the lower part of the uterus that connects to the vagina. It isn't clear what causes cervical cancer, but it's certain that HPV plays a role. HPV is very common, and most people with the virus never develop cancer. This means other factors — such as your environment or your lifestyle choices — also determine whether you'll develop cervical cancer.

<img src="/images/cervical-cancer.jpeg"/>

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

The best performing model is the **Voting Ensemble** model with a Weighted Average Precision Score of 0.9150. 

One may notice that the algorithms with the next best score, written as follows, has a good number of Extreme Random Trees followed by XGBoostClassifier. 

|Model |Weighted Average Precision Score|
|-|-|
|StandardScalerWrapper ExtremeRandomTrees|0.9112 |
|MinMaxScaler ExtremeRandomTrees|0.8958|
|MinMaxScaler ExtremeRandomTrees|0.8944|
|MaxAbsScaler XGBoostClassifier|0.8723 |


The interesting part is that these are infact the algorithms emsembled in the Voting Ensemble, with the following attributes

|**Field**|Value|
|-|-|
|**Ensembled Iterations**|11, 13, 14, 15, 8, 4, 5, 6, 9, 0|
|**Ensembled Algorithms**|'ExtremeRandomTrees', 'ExtremeRandomTrees', 'RandomForest', 'XGBoostClassifier', 'ExtremeRandomTrees', 'ExtremeRandomTrees', 'RandomForest', 'ExtremeRandomTrees', 'RandomForest', 'LightGBM'|
|**Ensemble Weights**|0.13333333333333333, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.13333333333333333, 0.13333333333333333, 0.13333333333333333, 0.13333333333333333, 0.06666666666666667, 0.06666666666666667|
|**Best Individual Pipeline Score**|"0.9112431387013187"|

I think if we ran the automl run longer we may find some more insights similar to this which might as well help us improve our results.

My run completed successfully, as displayed in the `RunDetails` widget, from my Jupyter Notebook below.
<img src="/images/Screen Shot 2021-01-21 at 9.37.38 PM.png"/>

The various models trained can be observed below, where `VotingEnsemble` has the best performance
<img src="/images/Screen Shot 2021-01-21 at 3.39.24 PM.png"/>

The parameters and further information about the best model maybe further received, as visible in the screenshot below.
<img src="/images/Screen Shot 2021-01-21 at 3.39.45 PM.png"/>

## Hyperparameter Tuning
Being a classification problem, I used **Logistic Regression** whose hyperparameters are tuned using the following configuration.

**Bandit Policy** <br/>
Bandit policy is based on slack factor/slack amount and evaluation interval. Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run. Unlike Truncation policy it doesn't calculate primary metric for all runs only to delete a percentage of them, but termminate it as soon as the primary metric doesn't satisfy slack amount, omitting unnecessary baggage. It also omits the need to calculate running Median, making it less computationally cumbersome unlike MedianStoppingPolicy.

**Random Parameter Sampling** <br/>
Random sampling supports discrete and continuous hyperparameters. In random sampling, hyperparameter values are randomly selected from the defined search space. It supports early termination of low-performance runs. Unlike other methods, this gives us a wide exploratory range, which is good to do when we don't have much idea about the parameters. It can also be used do an initial search with random sampling and then refine the search space to improve results.

**Weighted Average Precision Score**<br/>
Since the data isn't quite balanced, I chose [Weighted Average Precision Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) as my primary metric, from the scikit learn library.

### Results
The hyperparameters derived by Hyperdrive for the Logistic Regression Model is as follows:

|Hyperparameter|Value|
|-|-|
|Regularization Strength|0.030805695984711334|
|Max Iterations|900|

This gave a Weighted Average Precision Score of 0.09836065573770492.

The Run was completed successfully as one may observe in the screenshot below, wherein I used the `RunDetails` widget to derive information about the same.
<img src="/images/Screen Shot 2021-01-21 at 3.40.21 PM.png"/>
This widget also helped me debug, when it didn't identify my primary metric as I happened to log it with a slightly different name in `train.py`.

Hereby I may observe information about the parameters generated by the best run.
<img src="/images/Screen Shot 2021-01-21 at 3.41.30 PM.png"/>

I observed that, I may get a higher accuracy for this model, but that is due to the bias in the data. Using Weighted Average Precision Score shows that Logistic Regression isn't actually well suited for this problem. In a future scenario I might want to use a different model for hyperparameter tuning.

## Model Deployment
After finding the best model, I hereby deploy it:

I start by downloading the model itself from the `best_run` generated by AutoML.
<img src="/images/Screen Shot 2021-01-22 at 12.25.42 AM.png"/>

Following this I retrieve other files required for deployment, that are configured already by AutoML in our `best_run` namely the Conda Environment (required to know the packages in order to run the webservice) and Inference Configuration (required to score the webservice deployed). We also configure an Azure Container Instance in order to deploy the model as a webservice.
<img src="/images/Screen Shot 2021-01-22 at 12.26.16 AM.png"/>

With all these configurations ready, we may now actually deploy our model as a webservice, which is performes as follows.
<img src="/images/Screen Shot 2021-01-22 at 12.33.29 AM.png"/>

After the state of the model changes to *Healthy* from *Transitioning*, we can actually retrieve important information about our webservice such as Swagger URI, Scoring URI etc. which is done as follows.
<img src="/images/Screen Shot 2021-01-22 at 12.34.10 AM.png"/>

The endpoint generated is a REST API, and takes in `json` data. Some example `json` data may be generated as follows:
<img src="/images/Screen Shot 2021-01-22 at 12.38.57 AM.png"/>

Furthermore the endpoint can be queried as follows:
<img src="/images/Screen Shot 2021-01-22 at 12.40.35 AM.png"/>

We can also retrieve logs for our model as follows:
<img src="/images/Screen Shot 2021-01-22 at 12.43.32 AM.png"/>

Some more things that we can do with our service includes enabling application insights as done below, as well as deleting the service after use.
<img src="/images/Screen Shot 2021-01-22 at 12.45.02 AM.png"/>

## Screen Recording
View the Screen Recording for my submission (here)[https://youtu.be/Tw43_28cHUk].