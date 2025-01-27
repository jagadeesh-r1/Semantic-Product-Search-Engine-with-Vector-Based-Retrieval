FROM PYTHON_VERSION==3.8.5

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
