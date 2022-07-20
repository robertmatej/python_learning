def htmlitalic (text):
    def wrapper():
        string = "<i>" + text() + "<i>"
        return string
    return wrapper

def htmlbold(text):
    def wrapper():
       return ("<b>"+ text () +"<b>")
    return wrapper

@htmlitalic
@htmlbold
def text():
    return "Hey, this is a test text."

print(text())