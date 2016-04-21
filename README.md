Student Alcohol Consumption Prediction

Dataset was downloaded from http://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION

In the input, workday and weekend alcohol consumption is given in range of 1 - very low to 5 - very high.
Its value for the week is normalized as (workday_alcohol_consumption*5 + weekend_alcohol_consumption*2)/7
If the value is greater than 3.0, then alcohol consumption is considered too high.

I used Decision Tree Classifier & Support Vector Machine to predict whether alcohol consumption is high or not.
With DT Classifier, I had an accuracy of 88% and with SVM 91%.
