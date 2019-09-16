# Gowleyes Version 0.0.01

Gowleyes (Gatsby's Owl Eyes) is a pipeline program to convert latex documents to Ereader friendly formats (epub and mobi). 

Rather than reinventing the wheel, it aims to connect stronger programs to each other to generate a nice end to end output with minimal user intervention. As such, it requires a lot of programs to be installed. 

In its current phase, it has only one pipeline path, and the path is ugly, slow, and not recommended. But it's existence should pave the way for improvements in the near future. Documentation is sparce but coming. 


## System Structure
In parellel with this program exists a Firefox and Chrome Extension, and a Flask server. The extensions grab the the url of the current tab, and send that string to a flask server. Upon recieving a url, the flask server calls a specific pipeline in gowleyes.



