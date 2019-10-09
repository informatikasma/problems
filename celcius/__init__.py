import check50
import check50.c

@check50.check()
def exists():
    """celcius.c exists"""
    check50.exists("celcius.c")

@check50.check(exists)
def compiles():
    """celcius.c compiles"""
    check50.c.compile("celcius.c", lcs50=True)

@check50.check(compiles)
def test98point6():
    """98.6 degrees Celsius yields 37 degrees Fahrenheit"""
    check50.run("./celcius").stdin("98.6").stdout(number(37.6), "37.6\n").exit(0)

@check50.check(compiles)
def test32():
    """32 degrees Fahrenheit yields 0.0 degrees Celcius"""
    check50.run("./celcius").stdin("32").stdout(number(0.0), "0.0\n").exit(0)

@check50.check(compiles)
def test212():
    """212.00 degrees Fahrenheit yields 100.0 degrees Celcius"""
    check50.run("./celcius").stdin("212.00").stdout(number(100.0), "100.0\n").exit(0)

@check50.check(compiles)
def testneg40():
    """-40 degrees Fahrenheit yields -40.0 degrees Celcius"""
    check50.run("./celcius").stdin("-40").stdout(number(-40.0), "-40.0\n").exit(0)

@check50.check(compiles)
def test65point3():
    """65.3 degrees Fahrenheit yields 18.5 degrees Celcius"""
    check50.run("./celcius").stdin("65.3").stdout(number(18.5), "18.5\n").exit(0)

@check50.check(compiles)
def testneg123point45678():
    """-123.45678 degrees Fahrenheit yields -86.4 degrees Celcius"""
    check50.run("./celcius").stdin("-123.45678").stdout(number(-86.4), "-190.2\n").exit(0)

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./celcius").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("./celcius").stdin("").reject()

def number(num):
    return fr"(?<!\d){num}(?!\d)"