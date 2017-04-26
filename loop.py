#"Code for while loop"

def while_loop():
    x = 0
    while (x < 4):
        print x
        x = x + 1

if __name__ == "__main__":
    while_loop()

#"Simple code for forloop"
def for_loop():
    z = 0
    for z in range(2, 7):
        print z
if __name__ == "__main__":
    for_loop()

#"Use of forloop in string"
def for_string():
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for y in (Months):
        print y


if __name__ == "__main__":
    for_string()

#"Use break-statement in forloop"
def for_break():
    for x in range(10, 20):
        if (x == 15): break
        print x


if __name__ == "__main__":
    for_break()

#"Use of Continue statement in forloop"
def for_continue():
    for x in range(10, 20):
        if (x % 5 == 0): continue
        print x


if __name__ == "__main__":
    for_continue()

#"Code for "enumerate function" with "forloop""
def for_enumerate():
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(Months):
        print i, m


if __name__ == "__main__":
    for_enumerate()
