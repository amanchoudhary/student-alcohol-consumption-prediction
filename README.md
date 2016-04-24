Student Alcohol Consumption Prediction

Dataset was downloaded from http://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION

In the input, workday and weekend alcohol consumption is given in range of 1 - very low to 5 - very high.
Its value for the week is normalized as (workday_alcohol_consumption*5 + weekend_alcohol_consumption*2)/7
If the value is greater than 3.0, then alcohol consumption is considered too high.
Features used:
1. School
2. Sex
3. Age
4. Parents status
5. Mother education
6. Father education
7. Guardion
8. Weekly study time
9. Past failure
10. Extra curricular
11. Higher education
12. Romantic relationship
13. Going out
14. Health status
15. School absence
16. Final grades
I used Decision Tree Classifier & Support Vector Machine to predict whether alcohol consumption is high or not.
With DT Classifier, I had an accuracy of 88% and with SVM 91%.

Neural network is also implemented having accuracy of 92%.
You can choose the method in config.py file.


If you want to learn about neural network solution: This might be the best way to start with.
http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/