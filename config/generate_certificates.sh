#!/bin/bash

FQDN=$1

# Create the root cert
if [ ! -e surcCA.pem ]
then
    openssl genrsa -des3 -out surcCA.key 2048
    openssl req -x509 -new -nodes -key surcCA.key -subj "/C=US/ST=CA/O=SU Researach Computing/CN=${FQDN}" -sha256 -days 1825 -out surcCA.pem
fi

# Create a server key
openssl genrsa -out ${FQDN}.key 2048

# and a signing request
openssl req -new -key ${FQDN}.key -subj "/C=US/ST=CA/O=SU Research Computing/CN=${FQDN}" -out ${FQDN}.csr

cat > ${FQDN}.ext <<EOT
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = ${FQDN}
EOT

# Sign and get the cert
openssl x509 -req -in ${FQDN}.csr -CA surcCA.pem -CAkey surcCA.key -CAcreateserial -out ${FQDN}.crt -days 825 -sha256 -extfile ${FQDN}.ext

rm ${FQDN}.csr ${FQDN}.ext dccCA.srl

