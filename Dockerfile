FROM python:3.10

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

#* BTW, when you do "WORKDIR /app"   you also "cd" into "/app" That is why you can do "COPY . ." 
COPY . . 


# CMD ["flask", "run", "--host", "0.0.0.0"]