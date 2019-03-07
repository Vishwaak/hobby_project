import socket

class LanScanner():
    def __init__(self):
        self.hostname = socket.gethostname()
        self.networkIP = socket.gethostbyname(self.hostname)
        self.networkPrefix = self .networkIP.split(".")
        del(self.networkPrefix[-1])
        self.networkPrefix = ".".join(self.networkPrefix)

    def checkIp(self, currentIP):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(0.01)
        if not s.connect_ex((currentIP,135)):
            s.close()
            return 1
        else:
            s.close()

    def startScan(self):
        print('Your IP is : %s' % (self.networkIP))
        print('scanning Lan network')
        for ip  in range(1,255):
            currentIP = self.networkPrefix + '.'+str(ip)
            if self.checkIp(currentIP):
                print('%s \t- %s' % (currentIP , socket.getfqdn(currentIP)))
                print("Scanning completed")

if __name__ == '__main__':
    sLan = LanScanner()
    sLan.startScan()
