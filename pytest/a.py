def display():
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]
    
    for l in people:
        for d in l:
            print(d , l[d])

    r = []
    for l in people:
        r.append(l["given_name"] + " " + l["family_name"] + " : " + l["title"])
    # print(r)
    return r
    
if __name__ == "__main__":
    r = display()
    print(r)
