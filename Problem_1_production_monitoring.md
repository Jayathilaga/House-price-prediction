**Production monitoring steps - MLOPS**

- Monitoring data quality and Data Drift:
     1. As of now we know the training data data types for each column, we have to make sure that we get the same data type for each column
     2. Adding new feature to the model for better prediction.
     3. We can check data drift using evidently report and see how many columns are drifted.
     4. TO support the above claim we can check with KS goodness of fit test to see if the test data comes from an existing distribution of train data, in case we have a huge shift according to business we can take decision.
 
 
 - Monitoring Model drift:
     1. If we know the ground truth of new data ( the train data ), we can see how well our model performs and if there is a drastic shift we can take a call to change the parameters.
     2. We can have a challenge model that runs parallelly, if the existing model prediction falls behind longs can help us to create and retrain the model


Logs to be monitored :

RMSE,R- square for regression, KS stats, time taken to run the model, data quality

Business shifts:(A change in relation ship between dependent and independent variable )
- change in basis points in the banks
- recession 
- Covid  and so on .


Feedbacks of all the above are required to monitor the model.