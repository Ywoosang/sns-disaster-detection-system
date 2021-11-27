FROM mysql:8.0
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y locales 
RUN export LANGUAGE=ko_KR.UTF-8 
RUN export LANG=ko_KR.UTF-8 
RUN locale-gen ko_KR ko_KR.UTF-8 
RUN update-locale LANG=ko_KR.UTF-8 
RUN dpkg-reconfigure locales
# COPY my.cnf /etc/mysql/my.cnf