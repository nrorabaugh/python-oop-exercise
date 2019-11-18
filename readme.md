[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Codebar

## Prerequisites

* Programming fundamentals in Python
* Object Oriented Programming in Python

## Instructions

1. Fork and clone this repository.
1. Change into the new directory.
1. Fulfill the listed requirements.

Starter code is available in [`lib/app.py`](lib/app.py). You are required to
turn in your submission by making a pull request on the original repository.

Unless otherwise specified on the calendar or by an instructor, homework is due
the next morning by 9:00am.

## Requirements

### Part I: Members, Students and Instructors

You're starting your own web development school called Codebar! Everybody at
Codebar - whether they are attending workshops or teaching them - is
a `Member`:

* Each member has a `full_name`.
* Each member should be able to `introduce` themselves (e.g., "Hi, my name is Kevin!").

Each `Member` is also either a `Student` or an `Instructor`:

* Each Student has a `reason` for attending Codebar (e.g., "I've always wanted to make websites!").
* Each Instructor a `bio` (e.g., "I've been coding in Python for 5 years and want to share the love!").
* Each Instructor also has a set of `skills` (e.g., `["Python", "Javascript", "C++"]`).
* An Instructor can gain a new skill using `add_skill`.

### Part II: Workshops

Codebar also has Workshops. Each Workshop has:

* A `date`.
* A `subject`.
* A group of instructors.
* A roster of students.
* An `add_participant` method that accepts a member as an argument. If the Member is an Instructor, add them to the instructors list. If a Member is a Student, add them to the students list.

Create another method `print_details` that outputs the details of the workshop.

### Test Your Code

Make your code work for the following calls and print out the response you can
see in the comments below:

```py
workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details
# =>
# Workshop - 12/03/2014 - Shutl
#
# Students
# 1. Jane Doe - I am trying to learn programming and need some help
# 2. Lena Smith - I am really excited about learning to program!
#
# Instructors
# 1. Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.
# 2. Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love
#
```

## Bonus

The `print_details` method currently does a number of different things, like
printing out workshop details, the list of Students and the list of Coaches.

Create separate methods to print the workshop details (date and classroom),
a method to print out the students and one to print out the coaches. Call these
from `print_details` instead of having all the code there.

> Hint: look into defining private class methods.

## Plagiarism

Take a moment to refamiliarize yourself with the [Plagiarism policy](https://git.generalassemb.ly/DC-WDI/Administrative/blob/master/plagiarism.md). Plagiarized work will not be accepted.

## Contributors

Original content from [DC at f01e95](https://git.generalassemb.ly/dc-wdi-python-django/codebar/commit/f01e954473086b7d16df2bb3991465e2c67dd83a). Original contributors can be found in that repository's history. Recent contributors can be found in this repository's history.

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
