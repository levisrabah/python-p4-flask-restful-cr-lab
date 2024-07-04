#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        id=1,
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        id=2,
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )
    Red_Asoka = Plant(
        id = 3,
        name = "Red Asoka",
        image = "./images/red-asoka.jpg",
        price = 15.00,
    )

    db.session.add_all([aloe, zz_plant])
    db.session.commit()
