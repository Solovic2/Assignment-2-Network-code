my_file = open("tcp-example.tr", "r")
content = my_file.readlines()
node0={}
delay={}
queue_size=0
count = 0
for line in content:
    record = line.split(" ",3)
    packet = record[3]
    if((record[0] == "+" or record[0] == "-") and record[2][10] == "0"):
      if(record[0] == "+" ):
       node0[packet] += 1
      elif(record[0] == "-"):
       delay[count] = node0[packet]
       count+=1
output = open("output.txt", "w")
for op in delay:
 output.writelines(op)
 output.writelines(" " + str(delay[op]))
 output.writelines("\n")
print("************************")
