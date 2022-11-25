# documents.py
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields
from .models import Movie, Artist


@registry.register_document
class MovieDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'movie'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 2,
                    'number_of_replicas': 0}

    artist = fields.ObjectField(properties={
        'name': fields.TextField(),
        'email': fields.TextField(),
    })

    class Django:
        model = Movie  # The model associated with this Document
        related_models = [Artist]

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'description',
            'rating'
        ]
