# Which image I am using
FROM python 
# Copy code to /src
COPY . /src 
# What to run
CMD ["python", "/src/CracklePop.py"] 
