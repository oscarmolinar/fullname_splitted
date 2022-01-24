if "fullname" in input:
    fullname = input["fullname"]
    firstname = ""
    lastname = ""
    fullname_splitted = fullname.split(" ")

    if len(fullname_splitted) > 1:
        firstname = fullname_splitted[0]
        del fullname_splitted[0]
        lastname = " ".join(fullname_splitted)
    else:
        lastname = fullname_splitted[0]
else:
    firstname = ""
    lastname = ""

output = [{ "firstname": firstname, "lastname": lastname }]