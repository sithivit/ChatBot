CS50 ChatBot website created by Ken Bunlungsak

In the frontend i use html and css from bootstrap template to create a beautiful scenery in index.html, login.html and register.html
You can find the source code of the template from here https://colorlib.com/wp/template/login-form-v1/. The Template could be find in template folder.

In the frontend I ueses javascript to automate function and pass information without reloading the page this is called AJAX https://www.w3schools.com/xml/ajax_intro.asp

For backend the code is written in python with module flask and socketIO to pass information and render template that the user want
the link to the document is here flask: https://flask.palletsprojects.com/en/1.1.x/ socketIO: https://socket.io/docs/. The code could be find in app.py. Furthermore, I use sqlite database to store essential information that the website need. sqlite document: https://www.sqlite.org/docs.html

For ChatBot using in the website, I use many module to create this simple ChatBot but the main one is Chatterbot and Chatterbot_corpus.
 chatterbot: https://chatterbot.readthedocs.io/en/stable/ chatterbot_corpus: https://chatterbot.readthedocs.io/en/stable/corpus.html. I trained the ChatBot with stack dataset, the dataset could be found in categoreis directory under ChatBot folder(ChatBot.py). I also created extract.py under resource directory to extract subtitle from netflix movie  https://languagelearningwithnetflix.com/. when the subtitle is extracted you can convert the file into .yml and put in format that the chatbot can train on.

The chatterbot document also provide many dataset to train the ChatBot dataset: https://www.kaggle.com/kausr25/chatterbotenglish

the ChatBot can be improveby importing logic adpater from the document document: https://chatterbot.readthedocs.io/en/stable/logic/
