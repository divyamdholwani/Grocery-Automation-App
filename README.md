# Grocery-Automation-App


"This project has been made as a part of the mini-project of Innovation Hub"

Problem Statement-
Predict the rating of the product and the target gender audience.

Objective-
To help the sellers to know more about their product more by knowing the overall rating and gender audience to target.

Brief about the project-
1. The project has two main parts-
  i) The ML backend.
  ii) The streamlit front end. (model has been deployed here)
2. At the frontend we have taken several user inputs like 
  i) Member of IH (Yes/No)
  ii) Branch
  iii) City
  iv) Customer Type
  v) Product Line
  vi) Unit Price
3. If the user is a member of IH, we shall be using better algorithms to predict the results. While relatively less accurate result will be given if the user is not a member of IH. This may not be always true.
4. Based on other user inputs our algorithms at the back end will predict the results

5. At the backend we have used two types of algorithms- 
  i) Prediction- Linear Regression and SVM (SVR)
  ii) Classifictaion- KNN and SVM (SVC)
6. If user is member of IH, we have used SVR and SVC (0.536 accuracy). If user is not a member of IH we have used Linear Regressiona and KNN (0.49 accuracy).
7. Due to insufficient training data points, the ML models have not bee trained well.
8. All necessary preprocessing of data has been done 

# Run your program
1. Install all the files in your local device
2. In the Command Prompt, add the path where the files have been stored
3. Lastly run the following command in your command prompt- 
    streamlit run streamop.py
4. The frontend will automatically open in your browser.


