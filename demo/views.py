from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from elasticsearch import Elasticsearch
from .serializers import (
    MovieSerializer, ArtistSerializer
)
from .models import (
    Movie
)


es = Elasticsearch()


class SearchMovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'artist__name', 'artist__email']


class SearchMovieElasticView(generics.ListAPIView):

    def get(self, *args, **kwargs):
        query = self.request.GET.get('search', None)
        print("query", query)
        if query:
            q = {
                "from": 0,
                "size": 500,
                "query": {
                    "bool": {
                        "must": {
                            "multi_match": {
                                "query": query,
                                "fields": ["name^3", "description",  "artist.name^2", "artist.email^2"],
                                "fuzziness": "2",
                            }
                        },

                    }
                }
            }

        res = es.search(index="movie", body=q)
        final = []
        for hit in res['hits']['hits']:
            final.append(hit['_source'])
        return Response(final)
