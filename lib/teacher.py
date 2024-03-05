#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    '''Class "Teacher" in teacher.py'''
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge or []

    def teach(self):
        '''returns a random element from self.knowledge.'''
        if not self.knowledge:
            return None 
        return random.choice(self.knowledge)