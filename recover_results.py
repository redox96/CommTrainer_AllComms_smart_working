import csv

def recover_results(buffer, type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-42
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    with open ("data/output_%s.csv"%(type), "r", newline="") as output:
        readerOUT = csv.reader(output)
        outputList = list(readerOUT)

        with open ("data/average_%s.csv"%(type), "r", newline="") as buffers:
            reader = csv.reader(buffers)
            bufferavrgs = list(reader)

        with open ("data/results_%s.csv"%(type), "r", newline="") as prev_results:
            reader = csv.reader(prev_results)
            results = list(reader)
            for i in range(0,len(results)):
                randlet = results[i][0]
                d_time = float(results[i][1])
                for k in range(total):
                    if outputList[k][0]== randlet:
                        count = int(outputList[k][2])
                        average = float(bufferavrgs[k][5])
                        times_prev = float(outputList[k][1])
                        times_new = (count*times_prev+d_time)/(count+1)
                        outputList[k][2] = count+1
                        outputList[k][1] = times_new
                        outputList[k][5] = average
                        if d_time > 15:
                            outputList[k][4]= int(outputList[k][4])+1
                        else:
                            pass
                    else:
                        pass
                    if outputList[k][0]== randlet:
                        ind = len(results)-i
                        outputList[k][3] = ind
                    else:
                        pass

        with open("data/output_%s.csv"%(type), "w", newline="") as output:
            writer = csv.writer(output)
            for val in outputList:
                writer.writerow(val)

#recover_results(["I","C"], "Edge")
