import check50
import check50.c


@check50.check()
def exists():
    """cash exists"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash compiles"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def test1800():
    """input of 1800 yields output of 4"""
    check50.run("./cash").stdin("1800").stdout(coins(4), "4\n").exit(0)


@check50.check(compiles)
def test100():
    """input of 100 yields output of 1"""
    check50.run("./cash").stdin("100").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test700():
    """input of 700 yields output of 2"""
    check50.run("./cash").stdin("700").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test6500():
    """input of 6500 yields output of 7"""
    check50.run("./cash").stdin("6500").stdout(coins(7), "7\n").exit(0)


@check50.check(compiles)
def test92000():
    """input of 92000 yields output of 92"""
    check50.run("./cash").stdin("92000").stdout(coins(92), "92\n").exit(0)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -100"""
    check50.run("./cash").stdin("-100").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./cash").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./cash").stdin("").reject()


def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"