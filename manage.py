from app import create_app
from flask_script import Manager, Server

# create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

#unittest in manager instance
@manager.command
def test():
    '''
    Runs the unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


#manager.add_command('server', Server)
if __name__ == '__main__':
    manager.run()