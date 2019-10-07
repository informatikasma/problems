import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Dimas"""
    check50.run("./hello").stdin("Dimas").stdout("Dimas").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Deni"""
    check50.run("./hello").stdin("Deni").stdout("Deni").exit()
