# encoding=utf8

"""An exercise in encoding custom objects to JSON and decoding them back."""

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json


class Subject(object):
    def __init__(self, name="", comment=""):
        self.name = name
        self.comment = comment
        self.courses = []

    def __repr__(self):
        return "Subject: %s (%s):%s" % (self.name,
                                        self.comment,
                                        '\n - '.join([str(x) for x in [""]+self.courses]))

    def add_course(self, c):
        self.courses.append(c)


class Course(object):
    def __init__(self, name="", URL="", finished=False, comment=""):
        self.name = name
        self.URL = URL
        self.comment = comment
        self.finished = finished
        self.lessons = []

    def __repr__(self):
        justdoit = ""
        if (self.finished):
            justdoit = u'\u2713 '
        return "Course: %s%s (%s) - %s :%s" % (justdoit,
                                              self.name,
                                              self.comment,
                                              self.URL,
                                              '\n\t '.join([str(x) for x in [""]+self.lessons]))

    def add_lesson(self, l):
        self.lessons.append(l)

    def add_dummy_lesson_range(self, n):
        """ Create n dummy lessons and add them to the course """
        for i in range(1, n+1):
            l = Lesson(i)
            self.addLesson(l)


class Lesson(object):
    def __init__(self, number=0, name="", URL="", date_started="", date_finished="", finished=False, comment=""):
        self.number = number
        self.name = name
        self.URL = URL
        self.comment = comment
        self.date_started = date_started
        self.date_finished = date_finished
        self.finished = finished

    def __repr__(self):
        justdoit = ""
        if (self.finished):
            justdoit = u'\u2713 '
        return "Lesson: %s%d. %s (%s) - %s" % (justdoit,
                                               self.number,
                                               self.name,
                                               self.comment,
                                               self.URL)


def to_json(python_object):
    """ encoding Lesson/Course/Subject objects to JSON
    __class__ - class name used to decode the object later
    __value__ - a dictionary of all the object's attributes
    """
    if isinstance(python_object, (Lesson, Subject, Course)):
        return {'__class__': type(python_object).__name__,
                '__value__': python_object.__dict__}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    """ converting Lesson/Course/Subject from JSON back to objects
    (if we do this with unknown objects, something's bound to explode)
    (plus playing with globals() which I don't like, but let's try it anyway)
    """
    if '__class__' in json_object:
        cls = json_object['__class__']
        # Create an object which is an instance of the class named in variable 'cls'
        obj = globals()[cls]()
        # Take a walk through the dict containing all attributes and assign them to the new object
        for key, value in json_object['__value__'].items():
            # We can process individual attributes here, like converting
            # the value of "number" from string back into integer
            if (key == "number"):
                # it's stupid to have an exception to the rule, but oh well
                # I'll see if it's really necessary later
                value = int(value)
            setattr(obj, key, value)
        return obj
    else:
        return json_object
