# Hbase Connection with HTTPS URL

## Connection String
Steps:

1. Make sure to kinit your credentials
```kinit USERNAME -kt USERNAME.keytab```

2.Hold your jks/pem file for handle certificate
```usually : "cm-auto-global_truststore.jks"/"cm-auto-global_truststore.pem"```

3.Build your certificate
```This thing to make sure our connection is known by the server by hold the certificate```
```import certifi
cafile = certifi.where()
with open(pathjks, 'rb') as infile:
    customca = infile.read()
with open(cafile, 'ab') as outfile:
    outfile.write(customca)
 ```

4.Open connection
### example
```conn=phoenixdb.connect("https://yourhostname:8765, authentication="SPNEGO", autocommit=True)```

Well Done, you already connect to Hbase using python :)

## Requirements
Tested on phoenixdb = 1.0.0 & python = 3.8
