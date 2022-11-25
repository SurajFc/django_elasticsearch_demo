# Instructions

## Download and Install Elasticsearch
- https://www.elastic.co/downloads/elasticsearch
(version should not be greater than 7)
- Start Elasticsearch service 
``` sudo systemctl start elasticsearch  ```

## For django
- ```  pip install -r requirements.py ```
- ``` python manage.py makemigrations ```
- ``` python manage.py migrate ```
- You can also add fake data to the db with the following management command.
``` python manage.py createdata ```
- Create elasticsearch index
``` python manage.py search_index --create ```
- Populate data in elasticsearch
```python manage.py search_index --populate ```
- Finally run the server
- ``` python manage.py runserver ```

## Api
- Simple django search
``` http://localhost:8000/api/movie?search=test ```
- Elastic search django
``` http://localhost:8000/api/movieElastic?search=test ```

