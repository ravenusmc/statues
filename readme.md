# Statues
## Intro

This is a project that I wanted to build about 3-4 years ago but never got around to it. The project is 
focused on confederate statues and when they went up around the U.S. As a history major and a big 
Civil war guy, I'm really interested in this project. I'm not sure why I kept putting it off but 
a few months ago I finally got a good dataset. I downloaded it and put it on my desktop telling myself 
that I'll soon get to the project and start working on it. Well, I'm going to start doing that. 

Features of this project: 
1. Six graphs that show different aspects of the data.
2. Graphs have a drill down that all the user to get more data. 
3. Users can comment on individual graphs.
4. Sentiment is tracked and graphed for what every single person says. 
5. A user may drill down on the sentiment graph to see who wrote what was posted, date, sentiment 
and what was actually written. 
6. On the sentiment graph, a user may change between a line or a bar graph. 

Final issue to note: I don't believe that the data set has all civil war statues in the country.
Not 100% sure why they included what they did. 

# Getting started
### Installing

Please note that these instructions are not 100% complete. 

1. Clone the repo
2. Run [sudo] pip3 install or pip3 install flask
3. Run python3 app.py to run the application
4. Visit localhost:5000 to see the application
5. Please note that these instructions only follow the Python side of this application.

### Technology Stack

1. Flask-0.12
2. Python-3.4
3. Pandas-0.18.1
4. Numpy-1.11.0
5. Vue.JS-2.5
6. MySQL

### Operation

Once the program is downloaded, simply run the program as you would any other python program.
Then follow the address, which your console/terminal tells you to go to see the
website. Again, please do not forget to ensure that you have vue CLI installed
as well as npm.

# Issues / Other

1. Need to fix date/time graph issue for first graph drill downs. 
2. A note on the forms. I debated making one master form 'control' at the top of the page 
however I did not want each graph to be controlled by one form. I wanted each graph to 
have it's seperate control. I also thought about breaking my forms up into smaller components 
but also did not like how that turned out as well. Thus, that's why I have each graph has it's 
own form component. This may be fixed in the future...
3. Look at build_graph_six_drill_down method in data.py - may have minor issues. 

# Preview

To see a video that talks about this project please go here: COMING SOON