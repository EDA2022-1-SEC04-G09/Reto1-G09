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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo



def catalogo():
    catalogo = model.newCatalog()
    return catalogo


def cargarDatos(spotify):
    cargarArtistas(spotify)
    cargarAlbumes(spotify)



# Funciones para la carga de datos
def cargarArtistas(spotify):
    """
    """
    file = cf.data_dir + 'spotify-artists-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for artista in input_file:
        model.addArtista(spotify, artista)


def cargarAlbumes(spotify):
    """
    """
    file = cf.data_dir + 'spotify-albums-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(spotify, album)

def cargarTracks(spotify):
    """
    """
    file = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for track in input_file:
        model.addTrack(spotify, track)