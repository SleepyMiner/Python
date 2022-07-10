n=int(input("What Long Should the series be:"))
n1,n2=0,1
count=0
if n<=0:
    print("Please Enter a positive integer")
elif n==1:
    print("Fibbonacci sequence upto",n,":")
    print(n1)
else:
    print("Fibonaci Sequence:")
    while count<n:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      count +=1
