import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from Actors.models import Actor, Movie

class ActorView(View):
    
    # def post(self, request):
#         data = json.loads(request.body)
#         Actor.objects.create(
#             first_name = data['first_name'],
#             last_name = data['last_name'],
#             date_of_birth = data['date_of_birth'],
#         )
#         return JsonResponse({'message':'SUCCESS'}, status=201)
    
    def get(self, request):
        actors = Actor.objects.all()
        
        results=[{
            'first_name' : actor.first_name,
            'last_name'  : actor.last_name,
            'movies'     : [{
                'title'       : movie.title,
                'release_date': movie.release_date,
                'running_time': movie.running_time
                } for movie in actor.movies.all()]
            } for actor in actors]
        
        return JsonResponse({'result': results}, status=200)
    
    
class MovieView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Movie.objects.create(
#             title = data['title'],
#             release_date = data['release_date'],
#             running_time = data["running_time"]
#         )
#         return JsonResponse({'message':'SUCCESS'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        
        results=[{
            'title'        : movie.title,
            'release_date' : movie.release_date,
            'running_time' : movie.running_time,
            'actors'       : [{
                'last_name'  : actor.last_name,
                'first_name' : actor.first_name
                } for actor in movie.actor_set.all()]
            } for movie in movies]
        
        return JsonResponse({'result': results}, status=200)