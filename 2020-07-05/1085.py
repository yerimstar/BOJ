x,y,w,h = map(int,input().split())
diff = [x,y,w-x,h-y]
print(min(diff))