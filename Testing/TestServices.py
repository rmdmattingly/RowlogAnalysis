import os
import pytest
from ... import main

def testService(service, arg):
    print(os.system('python ../main.py service'))

for service in main.switcher:
    testService(service)
