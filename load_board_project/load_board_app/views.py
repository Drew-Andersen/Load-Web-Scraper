from django.shortcuts import render
from .scraper import scrape_load_board

def load_board_view(request):
    load_listings = scrape_load_board()
    return render(request, 'load_board_app/load_list.html', { 'load_listings': load_listings }) 