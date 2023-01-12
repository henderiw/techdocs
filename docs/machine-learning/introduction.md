#

google colab -> everything is preinstalled

## google colab

[google colab](https://drive.google.com/drive/folders/1OFNnrHRZPZ3unWdErjLHod8Ibv2FfG1d)
- tensorflow
- xgboost

## install r

[r](https://cran.r-project.org)
[rstudio](https://posit.co/download/rstudio-desktop/)

## general info

[general resources for ml](https://sdsclub.com/machine-learning-a-z-tips-and-resources/)

## ML process

step1: data preprocessing
- import the data
- clean the data
- split into training and test sets
  - seperating out: 20% test set, 80% train
  - test set is used to test the model (created the model with test data the model never saw)

step2: modelling
- build the model
- train the model
- make predictions

step3: evaluation
- calculate performance
- make a verdict


Feature scaling:
-> applied to a column
-> never applied to a row
-> 2 techniques
  - normalization: X' = (X - Xmin)/(Xmax-Xmin) -> new data set
    - substract the min value on each data set and devide with a value (max-min)
    - [0,1]
  - standardization: iso min substract the average and divide by the std deviation
    - X' = (X-Xavg)/(std dev)
    - [-3,3]