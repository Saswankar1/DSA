import re
while True:
    try:
        s = input().rstrip()    
        sc, mcv, op = s.split(";")
        if sc == "S":
            if mcv == "M":
                cap = op[:-2]                                   
                
            if mcv == "C" or mcv == "V":
                cap = op
            
            s = re.sub ("(\w)([A-Z])", r"\1 \2", cap)
            print (s.lower())
                
        if sc == "C":
            cap = op.title ()
            s = re.sub (r" ", r"", cap)
            q = s[:1].lower() + s[1:]                
            
            if mcv == "M":                                
                print (q+"()")
                
            if mcv == "C":
                print (s)
              
            if mcv == "V":
                print (q)
            
    except EOFError:
        break
