import requests
import json
from django.shortcuts import render, get_object_or_404
from .models import Season, Destination
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Home page: show all seasons
def home(request):
    seasons = Season.objects.all()
    return render(request, 'TripMate_app/home.html')

# Season page: list of destinations for selected season
def season_detail(request, slug):
    season = get_object_or_404(Season, slug=slug)
    destinations = season.destinations.all()
    return render(request, 'TripMate_app/season_detail.html', {
        'season': season,
        'destinations': destinations
    })

# Destination detail page
def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'TripMate_app/destination_detail.html', {
        'destination': destination
    })




@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '')

        # Pull destinations
        destinations = Destination.objects.all()
        dest_list = "\n".join([
            f"- {d.name}: {d.description}. Best months: {d.best_months}"
            for d in destinations
        ])

        prompt = f"""
          You are Seasonista's travel assistant bot.
          You know these destinations:
          greece,manali,japan

         {dest_list}

        Always answer in a friendly, helpful way about travel plans, best months to visit, 
        and seasonal recommendations.

        User: {user_message}
        """

        ollama_payload = {
            "model": "phi3:mini",
            "prompt": prompt
        }

        try:
            res = requests.post(
                'http://localhost:11434/api/generate',
                json=ollama_payload,
                stream=True,
                timeout=120
            )
            answer = ""
            for line in res.iter_lines():
                if line:
                    data = json.loads(line)
                    answer += data.get("response", "")
            return JsonResponse({"reply": answer})

        except Exception as e:
            return JsonResponse({"reply": "Sorry, I couldn't answer your question right now."})

    return JsonResponse({"error": "Invalid request"}, status=400)
