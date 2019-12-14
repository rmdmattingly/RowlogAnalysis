import pytest

@pytest.fixture
def serviceCalls():
    import json, os
    from jsonschema import validate

    python = "python ~/RowlogAnalysis/main.py"

    def serviceCalls(service, args):
        print(service)
        output = os.system(python + " " + service + " " + args)
        if service in "Invalid Service":
            assert isinstance(json, str)
        else:
            testCalls(output)

    def testCalls(output):
        assert validate(instance=json.loads(str(output)), schema=output)

    yield serviceCalls

def testServices(serviceCalls):
    from RowlogAnalysis import main
    from .MultipleArgScripts import MultipleArgScripts

    hasOneArg = True

    for service in main.switcher:
        for script in MultipleArgScripts:
            if service in script.name:
                serviceCalls(service, script.value)
                hasOneArg = False
        if hasOneArg:
            serviceCalls(service, "")
        hasOneArg = True
