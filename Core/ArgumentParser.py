import argparse

def createArgumentParser():
    parser = argparse.ArgumentParser(description="Analyzing workout trends in order to optimize peak athletic performance",
        prog="Rowlog Analyzer")
    parser.add_argument('teamCode', metavar='Team Code', help='Your code to access your team\'s workouts')
    parser.add_argument('service', metavar='Service', help='The analytic service you wish to call')
    parser.add_argument('--query', '-q', help='Search term you want to find')
    return parser;
