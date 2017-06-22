# Which image I am using
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code to /src
COPY . .

# What to run
CMD [ "python", "./CracklePop.py.py" ]
