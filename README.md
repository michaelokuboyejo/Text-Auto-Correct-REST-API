An AutoCorrect Spelling Checker REST API
====================================================

NB: This is based on Edward Pie's tutorial on [Building An AutoCorrect Spelling Checker.](https://youtu.be/4yOKlWZk52M)


This is a simple auto correct project with a rest api. It uses the texts/words The Project Gutenberg EBook of The Adventures of Sherlock Holmes
by Sir Arthur Conan Doyle gotten [here](https://norvig.com/big.txt) as corpus.


# How to run this project

1. Install the project's dependencies using the command : `pip install -r requirements.txt`
2. Download the corpus file and store in the project's folder, then reference in the index.py file.


Demonstration
--------------

On successful startup of the service, hit the `/predict/{word_to_predict}` endpoint of the service and the response will be of the pattern:

```json5
[
  {
    "probability": 0, // float value representing probability
    "word": "string" // word_to_predict, the value of the word in your request
  }
]
```



![Screenshot](img.png?raw=true)
 
Dependencies:
---

- Flask

# Next Steps

1. User specific predictions
2. Allow Clients add new words to the vocabulary 
3. Multi-Language Support
4. Implement Continuous learning