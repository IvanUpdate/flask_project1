from flask import Flask, render_template
import data
import random

app = Flask(__name__)
tours = data.tours
departures = data.departures


@app.route('/')
def render_main():
    num_of_tours = 6
    for key, value in tours.items():
        tours[key]["id"] = key
    tours_for_view = random.sample(list(tours.values()), num_of_tours)
    print(tours_for_view)
    return render_template('index.html', tours=tours_for_view, title=data.title, subtitle=data.subtitle, description=data.description, num_of_tours=num_of_tours)


@app.route('/departures/<departure>/')
def render_departure(departure):
    for key, value in tours.items():
        tours[key]["id"] = key
    upgrade_tours = []
    for key, value in tours.items():
        if value["departure"] == departure:
            upgrade_tours.append(value)
    return render_template('departure.html', departure=departure, tours=upgrade_tours, departures=departures)


@app.route('/tours/<id>/')
def render_tour(id):
    tour = tours[int(id)]
    tour_stars = "★"*int(tour["stars"])
    return render_template('tour.html', tour=tour, tour_stars=tour_stars, departure=departures[tour["departure"]])


if __name__ == '__main__':
    app.run()
