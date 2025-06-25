from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()

    guest1 = Guest(name="Tom Hanks", occupation="Actor")
    guest2 = Guest(name="Taylor Swift", occupation="Singer")

    episode1 = Episode(date="2023-01-01", number=1)
    episode2 = Episode(date="2023-01-02", number=2)

    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)

    db.session.add_all([guest1, guest2, episode1, episode2, appearance1, appearance2])
    db.session.commit()

    print("Database seeded!")
