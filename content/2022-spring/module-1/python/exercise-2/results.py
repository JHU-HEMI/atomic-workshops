#!/usr/bin/env python

class Results:

  def __init__(
    self,
    date=None,
    name='',
    path='',
  ):
    self.date = date
    self.name = name
    self.path = path

  def __str__(self):
    return 'Result %s on %s' % (self.name, self.date)


class Experiment(Results):

  def __str__(self):
    return 'Experiment %s on %s' % (self.name, self.date)


class Simulation(Results):

  def __str__(self):
    return 'Simulation %s on %s' % (self.name, selfdate)
