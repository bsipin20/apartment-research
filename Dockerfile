FROM python:3.9

WORKDIR app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN apt-get update && apt-get upgrade
RUN apt-get install -y cron
RUN chmod +x wait-for-it.sh

#ENTRYPOINT ["bin/sh", "bin/update.sh"]
