def isLandscape(width,height):
    if width>height:
        return 'Landscape'
    else:
        return 'Portrait'
    
w=int(input())
h=int(input())
Result=isLandscape(w,h)
print(Result)