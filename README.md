## Presentation
Hello! I'm Augustin Renard, a Data Scientist/Data Engineer from Montreal, soon based in Edinburgh. With a BBA in Information Technology from HEC Montreal, I'm passionate about harnessing data and cutting-edge technologies to drive impactful insights.

At Bell Canada, I revolutionized ETL processes using Docker, reducing processing time from 150 hours to 7 minutes. My skills span Python, Docker, Airflow, SQL, and frontend technologies like HTML, CSS, and Vue.js. I'm adept at analytics tools like Pandas, Numpy and Excel.

In roles like Full Stack Web Developer at Services iNSiTU inc and Webmaster Intern at Station Mont Tremblant, I honed my data analysis skills. Projects like Bitcoin price prediction and emotion detection in wine reviews demonstrate my ability to extract meaningful insights from data.

I've also developed machine learning models for projects such as Bitcoin price prediction using XGBoost, ARIMA, and FB Prophet. In the realm of computer vision, I've implemented a Wireless Hand Volume Controller using OpenCV and Mediapipe, showcasing my expertise in this exciting field.

I hold certifications from HarvardX, AWS, and Udemy, covering key areas like TinyML, DevOps and implementing Machine Learning solution on daily problems. As a Teaching Assistant at HEC Montreal, I've supported students in their data science journey.

Fluent in French and English, I thrive in multicultural settings and excel in collaborative, data-driven environments. I'm eager to bring my analytical mindset and technical expertise in machine learning and computer vision to a Data Scientist role.

## Education

### [Msc Software Systems](https://www.hw.ac.uk/study/postgraduate/information-technology-software-systems.htm)
#### Grade: on-going
#### Course Outline:
- Database and Informations Systems
- Advanced Software Engineering
- Computer Network Security
- Intelligent Robotics
- Computer Games Programming
- Software Engineering Foundations
- Advanced Human Computer Interaction

### [HarvardX (EdX) - CS109x: Introduction to Data Science with Python](https://www.harvardonline.harvard.edu/course/introduction-data-science-python)
#### Grade: 100% - A
#### Course Outline:
- Linear Regression
- Multiple and Polynomial Regression
- Model Selection and Cross-Validation
- Bias, Variance, and Hyperparameters
- Classification and Logistic Regression
- Multi-logstic Regression and Missingness
- Bootstrap, Confidence Intervals, and Hypothesis Testing
- Capstone Project

### [HEC Montreal - Bachelor Business Administration / IT Specialisation](https://www.hec.ca/etudiants/mon-programme/baa/specialisations/specialisation-analyse-affaires-technologie-information.html)
#### Grade: 3.0
#### Program Outline:
- Python Introduction
- Web Development Introduction
- DataBase management
- Java Introduction
- Analytics and Statistics for business analysis
- Machine learning
- UI/UX
- Team work and management

## Projects

### [Project - Computer Vision Interactive Map -  OPENCV](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/interactive_map)
#### Overview
![map](https://github.com/Augmaster/Augmaster.github.io/assets/90472022/bea00a89-1029-44b8-9dae-c2bd9f1c4c0b)

The Interactive Computer Vision Map project is an inventive application merging computer vision with geographical data to create an engaging map interface. Through a webcam, users can interact with the map in real-time using hand gestures, facilitating intuitive exploration of various regions without conventional input devices. Leveraging OpenCV and cvzone libraries, the application accurately detects and interprets hand movements, enabling dynamic manipulation of map elements.

![map_interactive](https://github.com/Augmaster/Augmaster.github.io/assets/90472022/b9e471d1-be40-4565-9b0b-302a65c0bf86)


In addition to interactive map features, the project integrates external data sources and APIs to enrich the user experience. By selecting countries on the map through hand gestures, users trigger requests to a Language Model via MetaAI, retrieving comprehensive information about the chosen regions. This educational integration enhances the application's appeal, offering users an interactive and informative journey through geographical data.


![data](https://github.com/Augmaster/Augmaster.github.io/assets/90472022/9f5778fe-c62d-4e63-b5d2-d536e03bc5ae)


#### The technologies I used: 

* OpenCV: Used for processing webcam input and detecting hand gestures.
* cvzone: Integrated for hand tracking capabilities.
* NumPy: Employed for numerical operations and data manipulation.
* MetaAI: Utilized for obtaining information about selected countries.
* Python Pickle: Employed for serializing Python objects.
* Matplotlib: Potential use for data visualization.
* cv2: OpenCV library for various computer vision tasks.

### [Project - Wordpress Deployment -  KUBERNETES](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/MiniProject-Docker)
#### Overview
In my recent DevOps training project, I successfully deployed a WordPress website on Kubernetes following a structured approach. The process involved creating a reliable MySQL deployment with a single replica and setting up a ClusterIP service to expose the MySQL pods internally. For the WordPress deployment, I configured the necessary environment variables to establish a connection with the MySQL database. To ensure data persistence, I implemented volume mounting. Additionally, I created a NodePort service to expose the WordPress frontend externally, enabling seamless user access.

#### The technologies I used: 
* Kubernetes (K8s): Orchestrated the deployment, scaling, and management of containers.
* MySQL: Utilized for the database backend of the WordPress website.
* Persistent Volumes (PV): Implemented to ensure data persistence across pod restarts.
* Deployment YAML: Defined configurations for MySQL and WordPress deployments.
* Service YAML: Configured ClusterIP service for MySQL and NodePort service for WordPress frontend access.

![Kubernetes](image-1.png)

### [Project - Student List App Deployment -  DOCKER](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/MiniProject-Docker)
#### Overview
The student-list project involves building a proof of concept (POC) for POZOS, a French IT company, to demonstrate the use of Docker for creating a decoupled infrastructure. The application, student_list, comprises a REST API and a web app written in HTML + PHP, both housed in separate containers. The objective is to improve deployment processes, implement versioning, follow best practices in Docker infrastructure, and employ Infrastructure as Code (IAC) principles.

#### The technologies I used: 
* PHP: Powering the web app for end-user interaction.
* Flask (Python): Creating the REST API with basic authentication.
* Docker: Utilized for containerization of both modules.
* Centos 7.6 OS: Recommended operating system for deployment.
* Docker Compose: Orchestrating the deployment of API and web app containers.
* Docker Registry: Setting up a private registry to store built Docker images.
* Python:2.7-stretch: Base image for building the API container.
* Flask Packages: Various packages including Flask, Flask HTTPAuth, Flask SimpleLDAP, and others, necessary for the API.
* Portus/Web Interface: Options for managing and viewing pushed images in the private registry.

![Student list app](image.png)

### [Project - Wireless Volume Control - COMPUTER VISION](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/WirelessVolumeChange)
#### Overview
The project uses a camera to track hand movements and gestures in real-time.It allows users to control their computer's volume by performing specific hand gestures.For example, getting your fingers closer can increase the volume while bringing spacing them can decrease it. The wireless nature of the project means that users can adjust their volume from a distance without having to touch their computer.
This technology could be applied to various other applications, such as smart home devices or gaming interfaces, making it a potentially useful addition to everyday life.

<img width="806" alt="image" src="https://user-images.githubusercontent.com/90472022/231293177-07680993-6ef4-4b86-a26d-ec3c218e174a.png">

[MediaPipe - Hand Tracking](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)

#### The technologies I used: 
* OpenCV to process the camera input, detecting and tracking the hand movements.
* Mediapipe  to estimate the hand landmarks, providing accurate data for gesture recognition.
* Numpy for data processing and manipulation, allowing for efficient calculation of gesture characteristics.
* Osascript to control the volume of the computer (MAC).

![image](https://user-images.githubusercontent.com/90472022/231293425-01346230-5a9e-474b-a7dc-37b338fa3a1e.png)

### [Project - Emotion detection Wine reviews - NATURAL LANGUAGE PROCESSING](https://www.kaggle.com/augustinrenard/emotion-detection-wine-review/edit)
#### Overview
The goal of this project was to develop an emotion detection model to categorize wine reviews as positive, neutral, or negative. The dataset used was a wine review database containing thousands of reviews, and two models were utilized for the analysis: Vadors and Roberta. Both models are pre-trained on large datasets and have been shown to perform well in NLP tasks such as sentiment analysis.
This project demonstrates the effectiveness of NLP techniques for emotion detection in wine reviews. The combination of lexicon-based and transformer-based models allowed for a comprehensive analysis of the emotional tone of the text. The high accuracy of the models suggests that they could be applied to other datasets with similar characteristics. Future work could involve exploring the use of additional models and fine-tuning the existing models to improve their performance.

<img width="342" alt="image" src="https://user-images.githubusercontent.com/90472022/231913962-7cea7ff3-da50-43f4-bc4b-59966beeaf62.png">

[Hugging face Roberta model](https://huggingface.co/docs/transformers/model_doc/roberta)

#### The technologies I used: 
* Pandas for data manipulation and analysis, especially for tabular data.
* NumPy for numerical computing, especially for scientific and mathematical calculations.
* Vadors model for lexicon-based sentiment analysis tool used to categorize text as positive, neutral, or negative based on a dictionary of words and their associated sentiment scores.
* Roberta model for transformer-based language model used for natural language processing tasks such as text classification and sentiment analysis.
* Kaggle  for the datasets, and collaborating with other data scientists.
* Seaborn for creating attractive and informative statistical graphics.

<img width="1307" alt="image" src="https://user-images.githubusercontent.com/90472022/231914495-bde2666e-de7e-4fb1-be7b-b51a66622325.png">

### [Project - Sleep forcasting - Rob Mulla Competition(Youtuber/Streamer) - MACHINE LEARNING](https://www.kaggle.com/competitions/kaggle-pog-series-s01e04)
#### Overview
The goal of this project was to develop a sleep forcasting model to predict futur sleep hours of the famous streamer/youtuber Rob Mulla. The dataset used was a number of hours of sleep for the past 4-5 years as well as some raw data from the application he used, such as steps of the day etc. 
<img width="1081" alt="image" src="https://user-images.githubusercontent.com/90472022/232236997-5b2c7061-20a7-43be-8925-526923ca5419.png">


For the first try I used an XGBRegressor model without much parameter tunning or cross validation and ended up having a score of 0.95113 which led me to 134/142 people participating: https://www.kaggle.com/code/augustinrenard/predict-rob-sleep-time

For the second attempt I reused XBGRegressor model but this time with a little more parameter tunning, a cross validation and a bit more exploratory data analysis and features development. I ended up finishing 63/142 with a score of 0.67656: https://www.kaggle.com/code/augustinrenard/predict-time-sleep-simple-method

Finaly I used the Facebook famous model Prophet but the results were not as good as XGBRegressor model. 

#### The technologies I used: 
* Pandas for data manipulation and analysis, especially for tabular data.
* NumPy for numerical computing, especially for scientific and mathematical calculations.
* XGBRegressor model for predicting continuous numerical values in various fields, such as finance, healthcare, and marketing.
* FB Prophet model for predicting future values of a given time series based on historical trends and patterns.
* Kaggle  for the datasets, and collaborating with other data scientists.
* Seaborn for creating attractive and informative statistical graphics.


### [Project - Bitcoin Trend Sentiment Predicter - MACHINE LEARNING](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/BitcoinSentimentPredicter)
#### Overview
The project is a bitcoin price predictor that utilizes the sentiment analysis of comments made on Wikipedia edits related to bitcoin. The project predicts the trend and popularity of bitcoin for the next day, indicating whether the price will increase or decrease. It uses natural language processing techniques to analyze the sentiment of comments and assess the mood of the community surrounding bitcoin. This information is then used to train a machine learning model that can accurately predict future trends in the bitcoin market. The end result is a tool that can help investors make informed decisions about their investments in bitcoin.

![image](https://user-images.githubusercontent.com/90472022/232858325-8eec2680-2452-45d7-a5e6-bcdf21a87d62.png)

I managed to improve the accuracy of the model up to 53% but there is a lot of improvment that can be done such as adding more features from tweets, articles and news that we can scrap online, but also by adding some other financial indicators such as inflation rate, GDP growth rate, etc.

![image](https://user-images.githubusercontent.com/90472022/232859034-e331fbb6-2269-4920-a7f6-82e5a7b8d5b9.png)


#### The technologies I used: 
* Pandas for data manipulation and analysis, especially for tabular data.
* NumPy for numerical computing, especially for scientific and mathematical calculations.
* XGBRegressor model for predicting continuous numerical values in various fields, such as finance, healthcare, and marketing.
* Hugging Face Sentiment Pipeline to analyze and understand the sentiment of large volumes of text data, such as social media posts, customer feedback, and product reviews.
* Mwclient for the datasets from wikipedia
* Yfinance to get the Bitcoin closing prices


### [Project - Speech Recognition to transcript in multi-languages - NATURAL LANGUAGE PROCESSING](https://github.com/Augmaster/Augmaster.github.io/tree/main/Projects/SpeechRecognitionEmotionAnalyser)
#### Overview
This project is based on Natural Language Processing and translation. This tool can efficiently generate transcripts from various sources such as live speeches, YouTube videos, and downloaded video files. With its multi-language support, it can provide accurate translations of different languages, making it an essential tool for translating live events, YouTube videos, classes, and other content that requires fast and detailed transcription. This project has potential to provide an efficient and reliable transcription service and makes it a valuable resource for individuals and organizations looking to reach a global audience.

This project is still on going and here is a road-map for the development:
- Add live speech recogntion
- Integrate a GUI from customtkinter
- Integrate in the GUI a way of chaning modes (youtube, live speach, downloaded video)
- In the GUI add features to change languages, modes, interfaces and themes
- Good feature could be to analyse the sentences sentiment and do an estimation of the total speech emotion score

#### The technologies I used: 
* Nltk to tokenize the transcript
* Pandas for data manipulation and analysis, especially for tabular data.
* NumPy for numerical computing, especially for scientific and mathematical calculations.
* Assenbly AI for the online transcription through the API
* GoogleTranslator library for the fast translation using google's API
* Pytube for downloading youtube videos


## Certifications
### [The Ultimate DevOps Bootcamp - 2023](https://www.udemy.com/certificate/UC-fe226cb8-800f-4725-86ef-e6efd245dc07/?utm_source=sendgrid.com&utm_medium=email&utm_campaign=email)
### [Masterclass Python | Algorithms and data processing](https://www.udemy.com/certificate/UC-da4b6a0e-b31c-419c-8bc1-bb625fdf6845/?utm_medium=email&utm_campaign=email&utm_source=sendgrid.com)
### [AWS Certified Developer - Associate](https://www.credly.com/badges/696e7ce0-e0e6-4c26-bb31-90e268741af8/public_url)
### [The web developer bootcamp 2022](https://www.udemy.com/certificate/UC-d3981853-f340-44a6-a414-342c181b024b/)
### [AWS Certifided Cloud Practionner](https://www.credly.com/badges/5e654fb4-f342-4ebc-a9f5-b0cd9b05eb95/public_url)

