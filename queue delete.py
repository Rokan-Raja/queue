queue = []
n=int(input("Enter the Total No of Queue:"))
for i in range(1,n):
    a=int(input("\nEnter the Element:"))
    queue.append(a)
print("\n Before Deleting Queue:")
print(queue)
print("\n After Deleting Queue:")
queue.pop(0)
queue.pop(0)
print(queue)
