import subprocess
import os
import sys

#before running this script, in command line:
#use the following command to set the password for PostgreSQL:
#set PGPASSWORD=""
#run with arguments
#python split_csv.py "D:/Thesis/libraries-1.6.0-2020-01-12/dependencies-1.6.0-2020-01-12.csv" "D:/Thesis/libraries-1.6.0-2020-01-12" "dependencies"

print("This is the name of the program:", sys.argv[0])

with open(sys.argv[1], mode="r", encoding="utf-8") as file_in:
    maxnum = 1000000
    count = 0
    filecount = 1
    lines = []
    for line in file_in:
        lines.append(line)

        count+= 1

        if(count > maxnum):
            count = 0
            filename = sys.argv[2] + "/temp-" + str(filecount) + ".csv"
            f = open(filename, "a", encoding="utf-8")
            f.write("".join(lines))
            f.close()

            lines = []
            filecount+= 1

            commandString = "COPY " + sys.argv[3] + " FROM '" + filename + "' DELIMITER ',' CSV HEADER ENCODING 'UTF8';"
            print(commandString)

            command = ['C:/Program Files/PostgreSQL/13/bin/psql.exe', '-U', 'postgres', ('--command='+commandString)]
            subprocess.call(command)

            #delete file
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("The file does not exist")

    filename = sys.argv[2] + "/temp-" + str(filecount) + ".csv"
    f = open(filename, "a", encoding="utf-8")
    f.write("".join(lines))
    f.close()

    commandString = "COPY " + sys.argv[3] + " FROM '" + filename + "' DELIMITER ',' CSV HEADER ENCODING 'UTF8';"
    print(commandString)
    command = ['C:/Program Files/PostgreSQL/13/bin/psql.exe', '-U', 'postgres', ('--command='+commandString)]
    subprocess.call(command)
    

        
