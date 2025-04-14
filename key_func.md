# Scikit-learn Functionality Overview

This document provides a comprehensive overview of the core functionalities of Scikit-learn (`sklearn`), including modules, their purpose, and where they fit in real-world machine learning tasks.

## Functional Modules in Scikit-learn

| Module                     | Functionality                                 | What It Does / When To Use It                                                | Example Use Case                                |
|---------------------------|-----------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------|
| `sklearn.linear_model`      | Linear & Logistic Regression                  | Predict numeric values or categories                                          | Predict house price, predict ad click            |
| `sklearn.tree`              | Decision Trees                                | Rule-based classification/regression                                          | Loan approval, disease diagnosis                 |
| `sklearn.ensemble`          | Random Forest, Boosting                       | Combine models to improve accuracy                                            | Fraud detection                                  |
| `sklearn.svm`               | Support Vector Machine                        | Binary/multi-class classifier, works well with small data                     | Spam detection, image classification             |
| `sklearn.naive_bayes`       | Naive Bayes Classifier                        | Fast probabilistic model for categorical/text data                            | Email spam detection, sentiment analysis         |
| `sklearn.neighbors`         | K-Nearest Neighbors                           | Classifies based on closest neighbors                                         | Recommender systems, handwriting recognition     |
| `sklearn.cluster`           | KMeans, DBSCAN, Clustering                    | Group unlabeled data automatically                                            | Customer segmentation, anomaly detection         |
| `sklearn.preprocessing`     | Scaling, Encoding, Normalization              | Prepares/cleans data before training                                          | Scale income, one-hot encode categories          |
| `sklearn.model_selection`   | Train/test split, Cross-validation            | Evaluate and tune model performance                                           | Avoid overfitting                                |
| `sklearn.metrics`           | Accuracy, Precision, ROC                      | Evaluate model quality                                                        | Confusion matrix, accuracy, precision            |
| `sklearn.decomposition`     | PCA, NMF                                      | Reduce dimensionality or extract features                                     | Image compression                                |
| `sklearn.pipeline`          | Preprocessing + Model                         | Automate and clean ML workflows                                               | Normalize, Train, Predict                        |
| `sklearn.datasets`          | Sample datasets                               | Access built-in datasets for testing/learning                                 | Iris, Digits datasets                            |
| `sklearn.feature_selection` | Select important features                     | Improve speed or remove noisy data                                            | Select top features                              |
| `sklearn.inspection`        | Explain model                                 | Visualize and interpret model predictions                                     | Feature importance, decision boundary            |
| `sklearn.calibration`       | Probability calibration                       | Make output probabilities more reliable                                       | Adjust predicted confidence                      |
| `sklearn.impute`            | Handle missing values                         | Fill NaNs using strategies like mean/median                                   | Missing income/age data                          |

## Quick Categories and Fit

| Category             | Common Modules                                               |
|----------------------|--------------------------------------------------------------|
| Supervised Learning  | `sklearn.linear_model`, `tree`, `ensemble`, `svm`, `neighbors`, `naive_bayes` |
| Unsupervised Learning| `sklearn.cluster`, `decomposition`                               |
| Data Preparation     | `sklearn.preprocessing`, `impute`, `feature_selection`            |
| Model Evaluation     | `sklearn.metrics`, `model_selection`, `calibration`, `inspection`    |
| Workflow Management  | `sklearn.pipeline`                                            |
| Practice Datasets    | `sklearn.datasets`                                            |

---

This README provides a quick overview of **Scikit-learn**'s capabilities for machine learning. You can use this as a reference to explore modules and decide which fits your task, be it classification, regression, clustering, or data preprocessing.

