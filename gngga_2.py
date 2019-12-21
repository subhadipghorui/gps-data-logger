# Input TXT file path as string
print("............................................................................................")
print("Convert the GPS log file to .txt formate and Copy it to the same directory where the python programme present.")
print("............................................................................................")
print("Enter the file name in the input box like---- 2.txt")
print("............................................................................................")
path = input("Enter File Path (log.txt) :")

# Enter the file path
myfile = open(path, "r")
# print(myfile.read())

# Creating a new file and closed it
newFile = open("lat_lon_alt.csv", "w")
newFile.writelines("lat, lon, alt" + "\n")
newFile.close()
# Set the cursor to the 0 position
myfile.seek(0)
alt: int = 0
for db_set in myfile.readlines():
    # fine the GNGGA data only
    # Check the string position and store in a variable
    val1 = db_set.find("$GNGGA")
    if val1 > -1:
        # print(db_set)
        # print(val1)

        data = db_set
        lat = data[(val1+18): (val1+28)]
        lon = data[(val1+31): (val1+42)]
        
        alt1 = float(data[(val1+55): (val1+59)])
        alt2 = float(data[(val1+62): (val1+67)])
        alt = alt1 + alt2

        print(lat, lon, alt)

        # Write to a new file
        newFile = open("lat_lon_alt.csv", "a")
        newFile.writelines(str(lat) + ", " + str(lon) + ", " + str(alt) + "\n")
        newFile.close()


print("New file created name lat_lon_alt.csv file Successfully.")
