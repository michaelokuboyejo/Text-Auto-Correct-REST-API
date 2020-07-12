An AutoCorrect Spelling Checker REST API
====================================================

NB: This is based on Edward Pie's tutorial on [Building An AutoCorrect Spelling Checker.](https://youtu.be/4yOKlWZk52M)


This is a simple auto correct project with a rest api. It uses the texts/words The Project Gutenberg EBook of The Adventures of Sherlock Holmes
by Sir Arthur Conan Doyle gotten [here](https://norvig.com/big.txt) as corpus.

How to run
------------



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



![Screenshot](img.png?raw=true "Screenshot")
 
Dependencies:
---

- Flask