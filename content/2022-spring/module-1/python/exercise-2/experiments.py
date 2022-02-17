#!/usr/bin/env python

from datetime import datetime
import results

exp1 = results.Experiment(date=datetime.now(), name='a')
exp2 = results.Experiment(date=datetime.now(), name='b')

print(exp1)
