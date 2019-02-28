####### Main File for execution #######
Main File - /Project/src/SentimentAnalysisCode.py
Supporting File - /Project/src/SentimentGUI.py


####### Install the following libraries #######
1) Natural Language Tool Kit - nltk
  sudo pip3 install nltk

2) numpy
  sudo pip3 install numpy

3) pandas
  sudo pip3 install pandas

4) SciKit - sklearn
  sudo pip3 install scikit-learn

5) tkinter
  in-built with Python

6) GIF Animator
  pygif.py


####### Gathered Data and Cleaned Data #######
data.xlsx and new_data.sxlsx

####### Images (GIFs) #######
"anger.gif", "joy.gif", "sadness.gif", "fear.gif", "disgust.gif", "shame.gif", "guilt.gif"

####### Abstract #######
Natural language processing is an area of computer science concerned with the interaction between computers and human languages. Sentiment analysis and opinion mining is the field of study in natural language processing that analyzespeople’s opinions, sentiments, and emotions from text. It is one of the most actively researched areas in natural language processing due to its importance in computer science, management science, social media analytics to name a few. We present a software which classifies the input sentence with a sentiment such as joy, sadness, fear, anger, disgust, shame, and guilt. We modeled different classifiers such as Naïve Bayes classifier, Maximum Entropy, and SVM classifier to achieve this task. Our result is a sentiment analysis model trained using the ISEAR dataset which will return the sentiment of the input sentence. Among the models that we built, SVM had the most optimal performance with an accuracy of 54% for in-built libraries and Naive Bayes was 51% accurate for the classifiers we built on our own. It is evident from the results of our models that multi-class emotion classification remains a challenging task due to informal language in user responses, presence of non-textual information such as emoticons, use of slang words/abbreviations, and lack of pre-furnished labeled corpus for training and improving models to achieve near-perfect accuracy. Nevertheless, our model also works effectively for binary classification with an improved accuracy of 81%.
