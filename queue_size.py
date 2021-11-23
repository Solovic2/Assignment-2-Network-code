my_file = open("tcp-example.tr", "r")
content = my_file.readlines()
node0={}
queue_size=0
for line in content:
    record = line.split(" ",2)
    time = record[1]
    if((record[0] == "+" or record[0] == "-") and record[2][10] == "0"):
      if(time not in node0):
          node0[time] = 0
      if(record[0] == "+" ):
       node0[time] += 1
       queue_size += 1
      elif(record[0] == "-"):
       if(node0[time] != 0):
        node0[time] -= 1
       else: node0[time] = queue_size - 1
       queue_size -= 1    
output = open("queue_size/output.cwnd", "w")
for op in node0:
 output.writelines(op)
 output.writelines("\t" + str(node0[op]))
 output.writelines("\n")
output.close()
print("************************")

