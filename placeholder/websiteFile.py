import os
from website import create_app, db
from website.models import event_user,User,Event,EventCategories,EventOrganizer
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Event=Event,EventCategories=EventCategories,EventOrganizer=EventOrganizer, event_user=event_user)
@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)