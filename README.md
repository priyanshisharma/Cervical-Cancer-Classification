# Cervical Cancer Classification
This is the Capstone Project of my Machine Learning Engineer with Microsoft Azure Nanodegree Program by Udacity.

I used an external dataset i.e. [Cervical Cancer Risk Classification](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29) dataset in our Machine Learning Workspace, and trained the model using different tools available in the Microsoft Azure Workspace. I created two models, one using *Automated ML* module by Microsoft Azure and one Logistic Regression model whose hyperparameters are tuned using *Hyperdrive*. I compared their performance on the basis of their respective Weighted Average Precision Score wherein the score of the Voting Ensemble model created by AutoML was found to be 0.9150 and the Logistic Regression model as 0.104. Furthermore, I deploy the better performing model i.e. clearly the Voting Ensemble model as a web service using the Azure ML Framework. 

<img src="/images/capstone-diagram.png"/>

# Table of Contents
 * [Dataset](#ds)
    * [Overview](#do)
    * [Task](#dt)
    * [Access](#da)
 * [Automated ML](#aml)
 * [Hyperparameter Tuning](#ht)
 * [Model Deployment](#md)
 * [Screen Recording](#sr)
 
 
## Dataset<a name="ds"></a>

### Overview<a name="do"></a>
Cervical cancer is a type of cancer that occurs in the cells of the cervix — the lower part of the uterus that connects to the vagina. It isn't clear what causes cervical cancer, but it's certain that HPV plays a role. HPV is very common, and most people with the virus never develop cancer. This means other factors — such as your environment or your lifestyle choices — also determine whether you'll develop cervical cancer.

<img src="/images/cervical-cancer.jpeg"/>

We're using the [UCI's Machine Learning repository's Cervical cancer (Risk Factors) Data Set](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29). The dataset was collected at 'Hospital Universitario de Caracas' in Caracas, Venezuela. The dataset comprises demographic information, habits, and historic medical records of 858 patients. Several patients decided not to answer some of the questions because of privacy concerns (missing values).

**Citation: Kelwin Fernandes, Jaime S. Cardoso, and Jessica Fernandes. 'Transfer Learning with Partial Observability Applied to Cervical Cancer Screening.' Iberian Conference on Pattern Recognition and Image Analysis. Springer International Publishing, 2017.**

### Task<a name="dt"></a>
Our target variable here is **Biopsy**. Biopsy is a sample of tissue taken from the body in order to examine it more closely. A doctor should recommend a biopsy when an initial test suggests an area of tissue in the body isn't normal. Doctors may call an area of abnormal tissue a lesion, a tumor, or a mass.
Here this categorical variable contains the *Biopsy Test Result*.

### Access<a name="da"></a>
The dataset maybe accessed via the `.csv` file given [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv). This dataset has a lot of missing values due to the privacy concerns of participants which hindered proper usage. This was fixed with reference to the [Kaggle Notebook](https://www.kaggle.com/senolcomert/cervical-cancer-risk-classification#6.-Missing-Value) by [Senol Cmrt](https://www.kaggle.com/senolcomert).

This cleaning maybe observed in the `data-cleaning.ipynb` file in this notebook.

I further brought this data in my experiment, by creating a Tabular Dataset using `TabularDatasetFactory` and furthermore used it as a pandas Dataframe, using the dataset's `to_pandas_dataframe()` method. 

## Automated ML<a name="aml"></a>
I used the following setting for my automl experiment.

* Since we're working on a small dataset, about 30 mins should be enough to reach the best performing model, and that is why we set `experiment_timeout_minutes` as 30.
* Since our Compute has 4 nodes we're going for 4 `max_concurrent_iterations`.
* In order to minimise *overfitting* we're using 3 Cross Validation (`n_cross_validations`).
* Since we're working with medical data, *accuracy* is of utmost importance, hence we choose it as the `primary_metric`.

### Results

The best performing model is the **Voting Ensemble** model with a Weighted Average Precision Score of 0.9061. 

One may notice that the algorithms with the next best score, written as follows, has a good number of Random Trees followed by XGBoostClassifier. 

|Model |Weighted Average Precision Score|
|-|-|
|MaxAbsScaler LightGBM|0.9006|
|MinMaxScaler RandomForest|0.9004 |
|StandardScalerWrapper XGBoostClassifier|0.8960|
|MinMaxScaler ExtremeRandomTrees |0.8945|
|StandardScalerWrapper XGBoostClassifier|0.8927|


The interesting part is that these are infact the algorithms emsembled in the Voting Ensemble, with the following attributes

|**Field**|Value|
|-|-|
|**Ensembled Iterations**|0, 14, 15, 6, 26|
|**Ensembled Algorithms**|'LightGBM', 'RandomForest', 'XGBoostClassifier', 'ExtremeRandomTrees', 'XGBoostClassifier'|
|**Ensemble Weights**|0.3333333333333333, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666|
|**Best Individual Pipeline Score**|"0.9005922928114609"|

### Future Improvement
I think if we ran the automl run longer we may find some more insights similar to this which might as well help us improve our results.

### Screenshots from the Run
My run completed successfully, as displayed in the `RunDetails` widget, from my Jupyter Notebook below.
[automl-rundetails]("/images/automl-rundetails-widget.png")

The various models trained can be observed below, where `VotingEnsemble` has the best performance
[automl models trained]("/images/automl-exptdetails.png")

The parameters and further information about the best model maybe further received, as visible in the screenshot below.
[automl further info]("/images/automl-runid.png")

## Hyperparameter Tuning<a name="ht"></a>
Being a classification problem, I used **Logistic Regression** whose hyperparameters are tuned using the following configuration.

The hyperparameters to be tuned are:
* **Learning Rate** -  It controls how quickly the model is adapted to the problem. It has a small positive value, often in the range between 0.0 and 1.0.
* **Maximum Iterations** - It is the maximum number of iterations that Regression Algorithm can perform.

**Bandit Policy** <br/>
Bandit policy is based on slack factor/slack amount and evaluation interval. Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run. Unlike Truncation policy it doesn't calculate primary metric for all runs only to delete a percentage of them, but termminate it as soon as the primary metric doesn't satisfy slack amount, omitting unnecessary baggage. It also omits the need to calculate running Median, making it less computationally cumbersome unlike MedianStoppingPolicy.

I have chosen my parameters for the same as follows:

|Parameter|Value|Meaning|
|-|-|-|
|evaluation_interval|1|The frequency for applying the policy.|
|slack_factor|0.001|The ratio used to calculate the allowed distance from the best performing experiment run.|

**Random Parameter Sampling** <br/>
Random sampling supports discrete and continuous hyperparameters. In random sampling, hyperparameter values are randomly selected from the defined search space. It supports early termination of low-performance runs. Unlike other methods, this gives us a wide exploratory range, which is good to do when we don't have much idea about the parameters. It can also be used do an initial search with random sampling and then refine the search space to improve results.

Herein, we provide hyperdrive a search space to check for parameters, for learning rate I started with a very small search space of 0.02 to 0.05, where I got a very small value for my primary metric (which actually had to be maximised), and the maximum iterations were the least number provided. 
[Attempt 2 Results]("/images/hyperdrive-parameters.png")

So I increased `--C` to be in the range `0.09 - 0.15` and added 50 to the choices of maximum iterations, and received the following.

[Attempt 2 Results]("/images/hyperdrive-a2.png")

I see thet the regularisation metric tends to be on the greater side, and took a much greater range of `0.3,0.6` while also adding more choices for `max_iter` as it increased to 500 from 100 in the previous run. Here I observed `--C` close to 0.3 and 1200 ite4rations and improvement in the metric.

So I finally used `0.4-0.6` for the range for regularisation and choices of `max_iter` arounf 1200, namely `1000,1100,1200,1300,1400`. Since the result is similar, I'll retain this.

[Attempt 3 Results]("/images/hyperdrive-a3.png")

**Weighted Average Precision Score**<br/>
Since the data isn't quite balanced, I chose [Weighted Average Precision Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html) as my primary metric, from the scikit learn library.

### Results
The hyperparameters derived by Hyperdrive for the Logistic Regression Model is as follows:

|Hyperparameter|Value|
|-|-|
|Regularization Strength|0.4862058369948942|
|Max Iterations|1400|

This gave a Weighted Average Precision Score of 0.10382513661202186.

### Future Improvements
I observed that, I may get a higher accuracy for this model, but that is due to the bias in the data. Using Weighted Average Precision Score shows that Logistic Regression isn't actually well suited for this problem. In a future scenario I might want to use a different model for hyperparameter tuning.

### Screenshots from the Run
The Run was completed successfully as one may observe in the screenshot below, wherein I used the `RunDetails` widget to derive information about the same. Visualising the training process is helpful in getting details of the different runs and metrics of the experiment. The RunDetails widget is one important tool that facilitates this, right from the notebook.
[Hyperdrive rundetails]("/images/hyperdrive-rundetails.png")
This widget also helped me debug, when it didn't identify my primary metric as I happened to log it with a slightly different name in `train.py`.

Hereby I may observe information about the parameters generated by the best run along with its run id.
[hyperdrive parameters]("/images/hyperdrive-a3.png")

## Model Deployment<a name="md"></a>
After finding the best model, I hereby deploy it:

I start by downloading the model itself from the `best_run` generated by AutoML.
[Model Download](/images/bestrun-download.png")

Following this I retrieve other files required for deployment, that are configured already by AutoML in our `best_run` namely the Conda Environment (required to know the packages in order to run the webservice) and Inference Configuration (required to score the webservice deployed). We also configure an Azure Container Instance in order to deploy the model as a webservice.
[deployment files download]("/images/deployment-files-download.png")

With all these configurations ready, we may now actually deploy our model as a webservice, which is performes as follows.
[model-deploy]("/images/model-deploy.png")

After the state of the model changes to *Healthy* from *Transitioning*, we can actually retrieve important information about our webservice such as Swagger URI, Scoring URI etc. which is done as follows.
[Health Endpoint]("/images/healthy-endpoint.png")

The endpoint generated is a REST API, and takes in `json` data. Some example `json` data may be generated as follows:
[Input Data]("/images/input-data-pop.png")

Furthermore the endpoint can be queried as follows, using the Scoring URI and Primary key, as coded in the `endpoint.py` file:
[endpoint screenshot]("/images/input-data-pop.png)

We can also retrieve logs for our model as follows:
[Model Logs]("/images/model-logs.png")

Some more things that we can do with our service includes enabling application insights as done below, as well as deleting the service after use.
[Enable Insights and Delete]("/images/enable-insights-delete.png")

## Screen Recording<a name="sr"></a>
View the Screen Recording for my submission [here](https://youtu.be/SjtqRTwpYLw).

## Standout Suggestions

### Convert model to ONNX format

The Open Neural Network Exchange (ONNX) is an open-source artificial intelligence ecosystem. it allows its users to interchange models between various ML frameworks and tools. I have converted the moel to ONNX format and made predictions with the same.
[Get ONNX model]("/images/onnx1.png")
[Use ONNX Model]("/images/onnx2.png")

### Enabled Logging in my deployed Web App
I've enabled logging, by means of the `logs.py` file, which fetches the webservice from its name and the displays its logs. This has also been performed in the Jupyter Notebook.
[Logs]("/images/logs.png")