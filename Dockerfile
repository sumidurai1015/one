# what os is gonna be used.
from python:3.9

# steps to copy the source code
copy app.py app.py
copy requirement.txt requirement.txt

# any other utilities
run pip install -r requirement.txt

expose 5000

# how to run the application
CMD ["python", "app.py"]