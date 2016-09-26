def calculateApacheIpHits(logfile_pathname):
    ipHitListing = {}
    contents = open(logfile_pathname,"r")

    for line in contents:
        ip = line.split(" ",1)[0]

        if 6 < len(ip) <= 15:
            ipHitListing[ip] = ipHitListing.get(ip,0) + 1
    return ipHitListing


HitsDictionary = calculateApacheIpHits("/var/log/apache2/www.access.log")

print sorted(HitsDictionary.iteritems(), key=lambda asd:asd[1], reverse=True)
