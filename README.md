# hours-of-operation-parser
This code is my solution for the following challenge:

Build an API with an endpoint which takes a single parameter, a date time string, and returns a list of restaurant names which are open on that date and time. You are provided a data set in the form of a CSV file of restaurant names and a human-readable, string-formatted list of open hours. Store this data in whatever way you think is best. Optimized solutions are great, but correct solutions are more important. Make sure whatever solution you come up with can account for restaurants with hours not included in the examples given in the CSV. Please include all tests you think are needed.

The CSV mentioned in the section above is in the 'data' directory at the root of this project and is named 'restaurants.csv'.

## Install Dependencies
If you ate running this via docker you shouldn't need to run this step. If you are running it manually, run the following command in your terminal from the root of this project to install the dependencies.

`pip install -r requirements.txt`

## Running Tests
Run the following command from the root of this directory

`python3 -m unit test discover tests`

## Running Server Manually
You can run the following command from the root of this repo to start the HTTP server:

`python3 main.py`

## Running With Docker
You can run the following command from the root of this repo to build and run the docker container for this code:

`docker build -t hours_of_op.`

Once that finishes building you can start it using the following command:

`sudo docker run -p 8000:8000 -t hours_of_op`

## Endpoint
You can interact with the service by sending a GET request to the following URL with a similar date time string.

`http://127.0.0.1:8000/?date=May%2010%201988%201am`

You may also hit the service using curl with the command below:

`curl http://127.0.0.1:8000/?date=May%2010%201988%201am`

With both of the requests above you should see a response similar to the one below:

`{"status": 200, "data": ["Seoul 116"], "message": "success"}`

## Parameters
The endpoint only accepts one parameter and it is mandatory that it be passed. The parameter name is date and it must be passed as a url GET parameter as seen in the examples above. The value for this parameter should be in the format "<Month> <Day> <Year> <Time><am or pm>". Note there is no space between the digit to the time and the am or pm. Some example values are 'May 21 2010 1am', 'December 15 2012 12am', 'March 22 2021 6pm' and 'December 9 2011 5pm'.

## Response Format
The response from the server will always contain a status, message and data key. The status will indicate a 200 if all went well, a 500 for a server error and a 400 for a bad request. When the request is successful it will return a list of restaurant names that are open during the time you provided.

## Basic Flow
- When the server starts it reads the CSV and creates a list of objects holding the restaurant's name and it's hours in the human format they come from in the csv.
- The hours strings are then split into a list on a forward slash and normalized, removing all multi spaces, trimming the left and right, swapping tues for tue to make all days 3 characters and lower casing each string.
- The normalized strings are then classified as either a single day, group of days, group of days with a day in front of it or a group of days with a single day after it.
- Based on the type of each string found in the previous step the hours of operation are split into a dictionary with each key being a day of the week and the value being a list of the hours the store is open on that day.
- These lists are then looped through and all the timestamps are converted to 24 hour timestamps to make comparing them easier.
- Once everything is in military time I loop back through them and look for any times that cross midnight, those need to be handles separately as the time past midnight is technically the next day. Any timestamp that rolled past midnight is split and the value in our offending day is updated to end at midnight. A new hours object is then pushed to the next day with the open time of midnight and the close time of the offending close time.
- Now that everything is sorted by day, the system parses the users date string passed into our GET request and extracts the day of the week and converts the timestamp passed to military time.
- With the above data parsed from our request we can loop through the list of all restaurants and check of they are open at all on the day in question and if they are, if the time the user is asking about falls within any of the open times.

## Notes
- Ideally I think this could use some more unit tests. I tried to cover a reasonable amount without sinking too much time into it but I think there are more to be added.
- The verification of the data and its format needs to be be expanded on. The function normalizing the hours strings could be expanded to work in a lot more corner cases with different ways the user passes the data in.
- If this were for a production service I would not use the HTTP code I used and would wrap that in a more suitable framework.
- Right now the verification of the format of the data input by the user could use a lot of expanding on before this would be ready for production.
- I think the organization of the code could use a second set of eyes and a good look over. I worked on some of this a little tired. I'm sure there is a lot of room for improvement on the organization end.
- There is a ton of room for improvement on the iteration of the hours data. I broke all the logic up to make it easy to develop the first time but when going back in, after getting all the data verification nailed down, it would be very high on my list to go back through the logic turning a string of hours into military time stamps and breaking out the overflowing past midnight. I could cut back on the amount of looping needed to fetch the data.
- In a production environment I would not store the restaurant objects in memory. I would use something like redis to persist the objects. This would also prob work very well with something like MySQL. You could use relational tables with one to many on a day to hours open / close to easily query the places open on a specific date / time.