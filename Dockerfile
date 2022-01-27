FROM python:3.6
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD ["streamlit","run","main.py"]