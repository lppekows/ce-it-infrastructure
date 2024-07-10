#!/bin/bash

domain=surctest.org

# Create the root cert
if [ ! -e dccCA.pem ]
then
    openssl genrsa -des3 -out dccCA.key 2048
    openssl req -x509 -new -nodes -key dccCA.key -subj "/C=US/ST=CA/O=LIGO@caltech/CN=${FQDN}" -sha256 -days 1825 -out dccCA.pem
fi

# Create a server key
openssl genrsa -out ${FQDN}.key 2048

# and a signing request
openssl req -new -key ${FQDN}.key -subj "/C=US/ST=CA/O=LIGO@caltech/CN=${FQDN}" -out ${FQDN}.csr

cat > ${FQDN}.ext <<EOT
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = ${FQDN}
EOT

# Sign and get the cert
openssl x509 -req -in ${FQDN}.csr -CA dccCA.pem -CAkey dccCA.key -CAcreateserial -out ${FQDN}.crt -days 825 -sha256 -extfile ${FQDN}.ext

rm dcc.popstar.party.csr dcc.popstar.party.ext dccCA.srl

