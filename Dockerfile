# what os is gonna be used.
FROM python:3.9

# working directory 
WORKDIR app/

# steps to copy the source code
COPY app.py app.py
COPY requirement.txt requirement.txt

# any other utilities
RUN pip install -r requirement.txt

EXPOSE 5000

# how to run the application
CMD ["python", "app.py"]