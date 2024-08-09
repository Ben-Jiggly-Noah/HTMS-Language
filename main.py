with open("main.htmc", "r") as f:
    buffer = "";
    stops = [" ", "\t", "\n"];
    for ch in f.read():
        if ch in stops: print("'"+buffer+"'"); buffer="";
        else: buffer+=ch;
