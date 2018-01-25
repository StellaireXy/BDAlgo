from __future__ import unicode_literals
from hdfs3 import HDFileSystem

test_host = 'localhost'
test_port = 9000

class Station:
    
    def __init__(self, USAF, NAME, FIPS, ELEV):
        self.USAF = USAF
        self.NAME = NAME
        self.FIPS = FIPS
        self.ELEV = ELEV
    
    def display(self):
        print("USAF:", self.USAF, " NAME:", self.NAME, " FIPS:", self.FIPS, " ELEV:", self.ELEV)

if __name__ == '__main__':
    
    file = '/test/isd-history.txt'
    station = []
    n = 0
    
    # connect to HDFS and read the file
    hdfs_client = HDFileSystem(host=test_host, port=test_port)

    with hdfs_client.open(file, 'rb') as f:
        line = f.readline()
        while line:
            n += 1
            if n > 22 :
                USAF = line[0:6]
                NAME = line[13:42]
                FIPS = line[43:45]
                ELEV = line[74:81]
                print("I'm converting the number " + str(n) + " station ...")
                station.append(Station(USAF, NAME, FIPS, ELEV))
            line = f.readline()
    
    hdfs_client.disconnect()
    
    # display the station info
    n -= 22
    print("There are", n, "stations :")
    for i in range(n):
        print(i, end=' ')
        station[i].display()
    
    print("-" * 20 + "END" + "-" * 20)
