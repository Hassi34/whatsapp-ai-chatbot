FROM python:3.11-slim

LABEL maintainer="hasanain@aicaliber.com"

WORKDIR /hassi_bot

COPY ./ ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80 443 8080

CMD ["python", "src/app.py"]