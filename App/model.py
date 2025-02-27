﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
   
    """
    spotify= {'artistas': None,
            'albums': None,
            "tracks":None}

    

    spotify['artistas'] = lt.newList('ARRAY_LIST')
    spotify['albums'] = lt.newList('ARRAY_LIST')
    spotify['tracks'] = lt.newList('ARRAY_LIST')


    return (spotify)

    
                            

# Funciones para agregar informacion al catalogo

def Artistas(id, track_id, artist_popularity, genres, name, followers):

    artista= {'id': " ",
            'track_id': " ",
            'artist_popularity': 0,
            'genres': " ",
            'name': " ",
            'followers': 0}
    artista['id']=id
    artista['genres'] = lt.newList('ARRAY_LIST')
    artista['genres']= genres
    artista['track_id']= track_id
    artista['artist_popularity']= artist_popularity
    artista['name']= name
    artista['followers']= followers
    return artista

def Albumes (id,track_id,total_tracks,external_urls,album_type,available_markets,artist_id,images,release_date,name,release_date_precision):

    album = {"id":"",
             "track_id":"",
             "total_tracks":"",
             "external_urls":"",
             "album_type":"",
             "available_markets":"",
             "artist_id":"",
             "images":"",
             "release_date":0,
             "name":"",
             "release_date_precision":""

    }
    album["id"]=id
    album["track_id"]=track_id
    album["total_tracks"]=total_tracks
    album["external_urls"]=external_urls
    album["album_type"]=album_type
    album["available_markets"]= lt.newList('ARRAY_LIST')
    album["available_markets"]=available_markets
    album["artist_id"]=artist_id
    album["images"]= lt.newList('ARRAY_LIST')
    album["images"]=images
    album["release_date"]=release_date
    album["name"]=name
    album["release_date_precision"]=release_date_precision

    return album

def Tracks (id,href,album_id,key,track_number,artists_id,energy,loudness,valence,danceability,playlist,speechiness,popularity,liveness,tempo,duration_ms,acousticness,available_markets,lyrics,disc_number,instrumentalness,preview_url,name):
    tracks = {"id":"",
            "href":"",
            "album_id":"",
            "key":0,
            "track_number":0,
            "artists_id":"",
            "energy":0,
            "loudness":0,
            "valence":0,
            "danceability":0,
            "playlist":"",
            "speechiness":0,
            "popularity":0,
            "liveness":0,
            "tempo":0,
            "duration_ms":0,
            "acousticness":0,
            "available_markets":"",
            "lyrics":"",
            "disc_number":"",
            "instrumentalness":"",
            "preview_url":"",
            "name":""}
    tracks["id"]=id
    tracks["href"]=href
    tracks["album_id"]=album_id
    tracks["key"]=key
    tracks["track_number"]=track_number
    tracks["artists_id"]=artists_id
    tracks["energy"]=energy
    tracks["loudness"]=loudness
    tracks["valence"]=valence
    tracks["danceability"]=danceability
    tracks["playlist"]=playlist
    tracks["speechiness"]=speechiness
    tracks["popularity"]=popularity
    tracks["liveness"]=liveness
    tracks["tempo"]=tempo
    tracks["duration_ms"]=duration_ms
    tracks["acousticness"]=acousticness
    tracks["available_markets"]=available_markets
    tracks["lyrics"]=lyrics
    tracks["disc_number"]=disc_number
    tracks["instrumentalness"]=instrumentalness
    tracks["preview_url"]=preview_url
    tracks["name"]=name

    return Tracks

def addArtista(spotify, artista):
    lt.addLast(spotify['artistas'], artista)

def addAlbum(spotify, album):
    lt.addLast(spotify['albums'], album)

def AddTrack(spotify, track):
    lt.addLast(spotify["tracks"], track)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

