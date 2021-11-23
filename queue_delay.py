my_file = open("tcp-example.tr", "r")
content = my_file.readlines()
node0={}
delay={}
queue_size=0
count = 0
for line in content:
    record = line.split(" ",4)
    packet = record[4]
    if((record[0] == "+" or record[0] == "-") and record[2][10] == "0"):
      if(record[0] == "+" ):
       node0[packet] = record[1]
      elif(record[0] == "-"):
       delay[count] = [record[1],str( float(record[1]) -float(node0[packet]))]
       count+=1
output = open("delay/output_delay.cwnd", "w")
for op in delay:
 output.writelines(delay[op][0])
 output.writelines("\t" + delay[op][1])
 output.writelines("\n")
output.close()
print("************************")
