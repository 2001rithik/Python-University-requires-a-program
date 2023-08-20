#student id-20210166/w1870601
#name-Rithik Subasinghe
#PART 4

print("Staff Version with Histogram")

file = open("file.txt","w+")

print("")

pr  = 0 # Progress
pmt = 0 # Progress (module trailer)
dnp = 0 # Do not Progress – module retriever
ex  = 0 # Exclude

x="y"

#Progression outcomes as defined by the University regulations
table  =  [
         [120,0,0,"Progress"],[100,20,0,"Progress (module trailer)"],[100,0,20,"Progress (module trailer)"],[80,40,0,"Do not Progress – module retriever"],
         [80,20,20,"Do not Progress – module retriever"],[80,0,40,"Do not Progress – module retriever"],[60,60,0,"Do not Progress – module retriever"],
         [60,40,20,"Do not Progress – module retriever"],[60,20,40,"Do not Progress – module retriever"],[60,0,60,"Do not Progress – module retriever"],
         [40,80,0,"Do not Progress – module retriever"],[40,60,20,"Do not Progress – module retriever"],[40,40,40,"Do not Progress – module retriever"],
         [40,20,60,"Do not Progress – module retriever"],[40,0,80,"Exclude"],[20,100,0,"Do not Progress – module retriever"],
         [20,80,20,"Do not Progress – module retriever"],[20,60,40,"Do not Progress – module retriever"],[20,40,60,"Do not Progress – module retriever"],
         [20,20,80,"Exclude"],[20,0,100,"Exclude"],[0,120,0,"Do not Progress – module retriever"],[0,100,20,"Do not Progress – module retriever"],
         [0,100,20,"Do not Progress – module retriever"],[0,80,40,"Do not Progress – module retriever"],[0,60,60,"Do not Progress – module retriever"],
         [0,40,80,"Exclude"],[0,20,100,"Exclude"],[0,0,120,"Exclude"]
          ]

while x!="q": #program should exit on ‘q’ to quit
    
    while True: #q is not equal to x

        p = input("Enter your total PASS credits:")

        try:
            p = int(p) #p only int value

        except:
            print('Integer required')
            print("")
            continue #Skip the iteration
        
        if not(p==0 or p==20 or p==40 or p==60 or p==80 or p==100 or p==120):
            print('Out of range')
            print("")
            continue #Skip the iteration

        break #End the loop

    while True: #q is not equal to x

        d = input("Please enter your credit at defer: ")

        try:
            d = int(d) #d only int value

        except:
            print('Integer required')
            print("")
            continue #Skip the iteration
        
        if not(d==0 or d==20 or d==40 or d==60 or d==80 or d==100 or d==120):
            print('Out of range')
            print("")
            continue #Skip the iteration

        break #End the loop

    while True: #q is not equal to x

        f = input("Please enter your credit at fail: ")

        try:
            f = int(f) #f only int value

        except:
            print('Integer required')
            print("")
            continue #Skip the iteration
        
        if not(f==0 or f==20 or f==40 or f==60 or f==80 or f==100 or f==120):
            print('Out of range')
            print("")
            continue #Skip the iteration

        break #End the loop

    if (p+f+d)!=120: #only total value 120
        print('Total incorrect')
        print("")
        continue
    query = [p,d,f]
    text = str(p)+","+str(d)+","+str(f)+","

    for i in range(len(table)):
        if [table[i][0], table[i][1], table[i][2]] == query:
            result = table[i][3]
            print(result)
            if result =="Progress":
                pr = pr + 1
                text="Progress"+"," + text
            elif result =="Progress (module trailer)":
                pmt = pmt + 1
                text = "Progress (module trailer)" + ","+ text
            elif result =="Do not Progress – module retriever":
                dnp = dnp + 1
                text = "Do not Progress – module retriever" + ","+ text
            elif result =="Exclude":
                ex = ex + 1
                text = "Exclude" + ","+ text

    print("")#space
    x=input("Would you like to enter another set of data? \n"
            "Enter 'y' for yes or 'q' to quit and view results: ")# input the (y = yes   , q =  quit)
    print("")#space
    
    file.write(text)
file.close()
print("--------------------------------------------------------------- ")
# Horizontal Histogram
print("Horizontal Histogram ")
print("Progress ",pr," : ","*"*pr)
print("Trailer ",pmt," : ","*"*pmt)
print("Retriever ",dnp," : ","*"*dnp)
print("Excluded ", ex," : ","*"*ex)

print("--------------------------------------------------------------- ")

print("")
# Vertical Histogram
print("Vertical Histogram ")
star = "*"
final=[pr,pmt,dnp,ex]
final =sorted(final)
pr_final,pmt_final,dnp_final,ex_final =(star*pr)+(" "*(final[3]-pr)),(star*pmt)+(" "*(final[3]-pmt)),(star*dnp)+(" "*(final[3]-dnp)),(star*ex)+(" "*(final[3]-ex))
print(" Progress "," Trailing "," Retriever "" Excluded ")
for j in range(final[3]):
    print("   ",pr_final[j],"        ",pmt_final[j],"         ",dnp_final[j],"        ",ex_final[j])

print("\n")
print(pr+pmt+dnp+ex," outcomes in total")
print("--------------------------------------------------------------- ")

with open("file.txt", "r") as file:
    for data in file:
        new_data = data.split(",")

r=int((len(new_data)-1)/4)
for f in range(r):
    g=3*f+f
    print(new_data[g]," - ",new_data[g+1],", ",new_data[g+2],", ",new_data[g+3])
file.close()
    


