import random
import csv
from datetime import datetime

#Problem 1
raw_data=([[random.random() for sensor in range(16)] for cluster in range(32)])     #created 2d array, 32 cluster by 16 sensor
#print(raw_data)

#Problem 2
#Created function to read data
def sensor_read(data,cluster_no):
    cluster_data=[]
    date = str(datetime.date(datetime.today()))
    time = str(datetime.time(datetime.today()))
    cluster_data.append('cluster_{}'.format(cluster_no+1))                             #
    cluster_data.append(date)                                       #Placing date of reading reading
    cluster_data.append(time)                                       #Placing time of reading
    cluster_data.extend(data[cluster_no][:])
    return cluster_data

data=[]                                                             #Storing read data
for cluster_no in range(32):
    data.append(sensor_read(raw_data,cluster_no))                   #place read data to storage
    print(data)

file = "Data_File.csv"                                              #from data stored create file
with open(file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(data)):
        test=sensor_read(data,i)
        #print(test)
        writer.writerow(test)



#Problem 3
#create corrupt data
for error in range(random.randint(1,10)):
    err_cluster_pos=random.randint(0,32)
    err_sensor_pos=random.randint(0,16)
    raw_data[err_cluster_pos-1][err_sensor_pos-1]='err'

#print error+1


def Faulty_check(data):
    Error_log=[['date','time','Cluster No.','sensor No.']]
    for cluster_pos in range(32):
        for sensor_pos,error_str in enumerate(data[cluster_pos]):
            if error_str=='err':
                err_cluster=cluster_pos+1
                err_sensor=sensor_pos+1
                date = str(datetime.date(datetime.today()))
                time = str(datetime.time(datetime.today()))
                Error_log.append([date,time,err_cluster,err_sensor])
                data[cluster_pos][sensor_pos]=1000                          #converted 'err' string to number for identification

    error_file = "Faulty_sensor.csv"
    with open(error_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(Error_log[0])
        for i in range(1,len(Error_log)):
            writer.writerow(Error_log[i])

Faulty_check(raw_data)

file = "Corrupt_Data_File.csv"
with open(file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(raw_data)):
        test=raw_data[i]
        #print(test)
        writer.writerow(test)
