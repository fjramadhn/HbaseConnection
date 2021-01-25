import certifi
import phoenixdb

cafile = certifi.where()
with open(pathjks, 'rb') as infile:
    customca = infile.read()
with open(cafile, 'ab') as outfile:
    outfile.write(customca)
    
conn = phoenixdb.connect("http://localhosts:8765", authentication="SPNEGO", autocommit=True)
