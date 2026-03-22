Team Members:

Nihal Karkera – 01SU23AI057
Worked on designing and implementing the Autoencoder deep learning model using TensorFlow/Keras. Responsible for training the model on normal transaction data, calculating reconstruction error for anomaly detection, selecting the threshold value for fraud classification, and integrating the trained model with the Flask web application for real-time prediction.

Sanjay Moolya – 01SU23AI051
Handled dataset preprocessing and feature preparation. Performed normalization using StandardScaler and prepared the dataset for anomaly detection by selecting only legitimate transactions (Class = 0) for training the Autoencoder model.

Prajwal Uday Musali – 01SU23AI068
Implemented backend logic for prediction using Flask. Developed reconstruction error calculation and designed the fraud detection decision mechanism based on threshold comparison. Also worked on generating risk scores and categorizing transactions into Low, Medium, and High risk levels.

Rahul – 01SU23AI064
Developed the frontend interface for the system using HTML and Flask templates. Designed the transaction input form and created result display sections showing prediction status such as Safe Transaction or Fraud Detected along with risk levels for user understanding.

Ritvik S – 01SU23AI072
Worked on dashboard visualization and system testing. Implemented transaction monitoring features to display fraud detection results and risk distributions. Performed multiple test-case evaluations to verify prediction accuracy and ensure proper system functionality.


This project presents a deep learning–based approach for detecting fraudulent credit card transactions using an Autoencoder neural network. The system is designed to identify unusual transaction patterns by learning the behavior of normal transactions and detecting deviations from that behavior.

Credit card fraud detection is an important problem in financial security systems. Traditional fraud detection methods depend on rule-based approaches, which are less effective when dealing with new or unknown fraud patterns. To overcome this limitation, this project uses an unsupervised deep learning technique called anomaly detection, where the model automatically identifies suspicious transactions without requiring labeled fraud examples during training.

In this system, the Autoencoder model is trained only on legitimate transaction data. The model learns the normal transaction behavior and tries to reconstruct the input data at the output layer. When a new transaction is given as input, the model attempts to reconstruct it. If the reconstruction error is small, the transaction is considered normal. If the reconstruction error is high, the transaction is considered fraudulent.

The reconstruction error is calculated using the difference between the original input and the reconstructed output. This error value is compared with a predefined threshold. If the error exceeds the threshold value, the system classifies the transaction as Fraud Detected; otherwise, it classifies it as a Safe Transaction.

The system also calculates a risk score percentage, which helps in identifying the severity level of the transaction. Based on this score, transactions are categorized into:

Low Risk
Medium Risk
High Risk

The project is implemented using Python, TensorFlow/Keras, Scikit-learn, and Flask. The dataset used for training is the credit card transaction dataset, which contains anonymized transaction features. Data preprocessing techniques such as normalization using StandardScaler are applied before training the model.

A user-friendly web interface is developed using Flask and HTML templates where users can enter transaction details such as transaction amount and time. The system processes the input and displays the prediction result along with the fraud risk score and risk level.

Additionally, a dashboard module is implemented to monitor transaction history and visualize fraud detection results. This helps in understanding the performance of the system and analyzing transaction behavior effectively.

This project demonstrates how deep learning–based anomaly detection techniques can be applied to real-world financial security problems and provides an efficient solution for identifying fraudulent transactions in banking systems.
