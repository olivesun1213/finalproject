# Graduation Project - Accident Fatality Predictor

## Team 👨🏻‍💻👨🏻‍💻👨🏻‍💻👩🏻‍💻👩🏻‍💻

- [Jaehong Kwon](https://github.com/sssaso)
- [XiongFei (Frank) Shi](https://github.com/xshi64)
- [Feng Wang](https://github.com/FengWang1991)
- [Olive Sun](https://github.com/olivesun1213)
- [Neha Nayeem](https://github.com/neha-nayeem)

## Topic and Description 
#### Topic: Prediction of Accident Fatality using Machine Learning

Using historical KSI (Killed or Seriously Injured) data from Toronto Police Open Data, we aim to predict the fatality of an accident given a certain input (time/weather condition/etc.). 

This information could be used to possibly prevent accidents by encouraging drivers to drive more carefully in a particular area. 

## Datasets 🗃
* [Toronto Police Open Data](https://data.torontopolice.on.ca/pages/open-data)

## Project Infrastructure

Our app is deployed using Heroku and is available at: [Accident Fatality Predictor](http://accident-fatality-predictor.herokuapp.com/)

### Tools used

### Machine Learning Models

### Flask
Our Flask app hosts our API endpoints as follows:

* `/`: The root endpoint directs the user to the landing page (`index.html`) where they are able to provide user input.

* `/historicaldata`: This endpoint shows the data used in our machine learning models as an HTML table that can be filtered.

* `/dashboard`: Our Tableau story and dashboards are embedded in the HTML page hosted at this endpoint.

* `/models`: We link our Jupyter notebooks to all the machine learning models that were tested during the project.

* `/predict`: This endpoint gets user input from the HTML forms and encodes the values into binary value arrays using a predefined function. These arrays are then merged together to form a 2D array with 66 features as required by the ML model. `model.predict` gives us our prediction of "Fatal" or "Non-Fatal Injury" which is then passed to the `prediction.html` page using `render_template`.
