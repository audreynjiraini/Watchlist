from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Role, Review
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)


@manager.command
def test():
    '''
    Run the unit tests
    '''
    
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
    
@manager.shell # create a shell context
def make_shell_context(): #allows us to pass in properties into the shell
    return dict(app=app, db=db, User=User, Role=Role, Review=Review) # return application and database instances and User and Role classes


    
if __name__ == '__main__':
    manager.run()