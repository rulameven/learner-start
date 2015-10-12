============
LearnerStart - objects and JSON
============

I wanted to have a way to track my self-directed learning efforts, like various
tutorials or online courses. I wanted the data to be easily accessible in a 
plain file, not in a database somewhere. So I built a model (Subject\Course\
Lesson) and methods to store these objects in JSON. 

Here's the basic code for the project. I intend to build upon it, but want to
leave this here as an example of object-JSON encoding and decoding.



Sources
--------
* http://chimera.labs.oreilly.com/books/1230000000393/ch06.html#_discussion_95
* http://www.diveintopython3.net/serializing.html#json
* https://docs.python.org/2/library/json.html


Example usage:
--------------

.. code-block:: python

    import json
    from start import Subject, Course, Lesson, to_json, from_json
    
    s = Subject("Javascript", "Let's see what's new")
    c = Course("JavaScript Road Trip Part 1", "https://www.codeschool.com/courses/javascript-road-trip-part-1", "next step")
    l1 = Lesson(1, "The Cliffs of Value")
    l2 = Lesson(2, "Variable Valley")
    l3 = Lesson(2, "Files Falls")
    c.add_lesson(l1)
    c.add_lesson(l2)
    c.add_lesson(l3)
    s.add_course(c)
    print s

    c2 = Course("something", "http://example.com", "comment? what?")
    c2.add_dummy_lesson_range(4)
    s.add_course(c2)
    print s

    jo = json.dumps(c, default=to_json)
    m = json.loads(jo, object_hook=from_json)

    with open('data.txt', 'w') as outfile:
        json.dump(s, outfile, default=start.to_json)
    
    with open('data.txt') as d:
        m = json.load(d, object_hook=start.from_json)
   
