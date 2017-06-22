FROM python # Which image
COPY . /src # code to /src
CMD ["python", "/src/CracklePop.py"] # What to run
