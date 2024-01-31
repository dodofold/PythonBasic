def fold(*args):
    arg1, arg2, arg3 = args
    print(f"I'm gonna fold it {arg1}, {arg2}, {arg3} papers.")
    
fold("up", "down", "close it over the")

def no_changes(manpap, mandone):
    print(f"I'm not changing anything. I just fold the papers from {manpap} to {mandone}.\nNow I'm done.")

no_changes("A4", "A6")
    