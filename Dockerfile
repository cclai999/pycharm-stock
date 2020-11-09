FROM python:3.8

WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /app
EXPOSE 5000
CMD ["gunicorn", "-w 1", "-b 0.0.0.0:5000", "web:app"]