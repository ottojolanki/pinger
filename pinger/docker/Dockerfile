FROM ubuntu

RUN apt-get update && apt-get install -y curl

ADD ping.sh /ping.sh

CMD [ "/bin/bash", "/ping.sh" ]
