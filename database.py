from mongoengine import connect
from models import Department, Employee, Role

# connect('graphene-mongo-example',
#       host='mongodb://localhost', alias='default')
connect('graphene-mongo-example',
        host='mongomock://localhost', alias='default')


def init_db():

    engineering = Department(name='Engineering')
    engineering.save()

    hr = Department(name='Human Resources')
    hr.save()

    manager = Role(name='manager')
    manager.save()

    engineer = Role(name='engineer')
    engineer.save()

    peter = Employee(name='Peter', department=engineering, role=engineer)
    peter.save()

    roy = Employee(name='Roy', department=engineering, role=engineer)
    roy.save()

    tracy = Employee(name='Tracy', department=engineering, role=engineer)
    tracy.save()
