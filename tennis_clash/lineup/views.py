from django.shortcuts import render
from django.requests import HttpRequest
from .models import Character

# Create your views here.
def calculate_player_attributes(HttpRequest):
    character_level = HttpRequest.get('character_level')
    character_name = HttpRequest.get('character_name')
    pass

def calculate_item_attributes(HttpRequest):
    item_type = HttpRequest.get('item_type')
    item_name = HttpRequest.get('item_name')
    item_level = HttpRequest.get('item_level')
    
    pass

def calculate_combined_attributes(HttpRequest):
    character_level = HttpRequest.get('character_level')
    character_name = HttpRequest.get('character_name')
    items = HttpRequest.get('items')
    combine_attrs =calculate_player_attributes()
    for item in items:
        item_type = HttpRequest.get('item').get('item_type')
        item_name = HttpRequest.get('item').get('item_name')
        item_level = HttpRequest.get('item').get('item_level')
        combine_attrs +=calculate_item_attributes()
    
    return combine_attrs

def rank_lineups(HttpRequest):
    pass