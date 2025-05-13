from fastapi import FastAPI,APIRouter
from pokemontcgsdk import Card,Set

router=APIRouter()

@router.get("")
def get_pokemon_set():
  sets=Set.all()
  return sets

@router.get("/{set_id}")
def get_pokemon_set_by_id(set_id : str):
  set = Set.find("set_id")
  return set
