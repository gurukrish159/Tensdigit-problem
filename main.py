#1
n=int(input())
k=int(input())
print(((n//10)*100)+((k-(n%10))*10)+n%10)
#2
n=input()
k=int(input())
print(n[:len(k)-1)]+k-int(n[-1])+n[-1])