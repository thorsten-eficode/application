FROM centos:centos7.2.1511

# If you need to use a proxy to get to the internet, build with:
#   docker build --build-arg CURL_OPTIONS="..."
#
# The default is empty (no special options).
#
ARG CURL_OPTIONS=""

# wget - command line utility (installed via. RPM)
#
# https://www.cvedetails.com/cve/CVE-2014-4877/
#
RUN curl -LO ${CURL_OPTIONS} \
      http://vault.centos.org/7.0.1406/os/x86_64/Packages/wget-1.14-10.el7.x86_64.rpm && \
    yum -y install wget-1.14-10.el7.x86_64.rpm && \
    rm *.rpm

# Precautionary failure with messages
#
CMD echo 'Vulnerable image' && /bin/false

# Basic labels.
# http://label-schema.org/
#
LABEL \
    org.label-schema.name="bad-dockerfile" \
    org.label-schema.description="Reference Dockerfile containing software with known vulnerabilities." \
    org.label-schema.url="http://www.stindustries.net/docker/bad-dockerfile/" \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/ianmiell/bad-dockerfile" \
    org.label-schema.docker.dockerfile="/Dockerfile"
