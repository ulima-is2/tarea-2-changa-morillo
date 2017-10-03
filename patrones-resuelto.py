# **********************
# * PATRONES APLICADOS *
# **********************
# - Factory
# - State
# - Fachada

import sys

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)



class CineStark:
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

# Patrón Factory:
# La razón por la que se aplicó este patron es porque se puede aprovechar la existencia de dos clases distintas
# y la necesidad de un condicional que permita escoger uno de los tipos. De esta manera esta lógica puede
# encapsularse en una clase factory para poder usarla en el método main.
class CineFactory:
    def obtenerCine(self, idCine):
        if idCine == '1'
            return CinePlaneta()
        elif idCine == '2'
            return CineStark()
        else
            return None

# Patrón State:
# La razón por la que se aplicó este patron es porque en el código se maneja un sistema de menus. Ante esta
# necesidad el uso del patrón state resulta útil para controlar el menú en el cual se encuentra el usuario,
# y limitar las opciones que se pueden realizar una vez en un menú en cuestión.

class EstadoMenu:
    def __init__(self, menu, cine, pelicula):
        self.cine = cine
        self.pelicula = pelicula
        self.funcion = funcion
        self.menu = menu

    def iniciarListarCines(self):
        pass

    def escogerCine(self, idCine):
        pass

    def iniciarListarCartelera(self):
        pass

    def listarCartelera(self)
        pass

    def listarPeliculas(self):
        pass

    def escogerPelicula(self, pelicula):
        pass

    def iniciarComprarEntrada(self):
        pass

    def escogerFuncion(self, funcion, entradas):
        pass

    def regresar(self):
        pass

class EstadoMenuPrincipal(EstadoMenu):
    def iniciarListarCines(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        self.menu.estado = EstadoCinesListados(self.menu, None, None)

    def iniciarListarCartelera(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        self.menu.estado = EstadoListarCarteleraIniciado(self.menu, None, None)

    def iniciarComprarEntrada(self):
        print('********************')
        print('COMPRAR ENTRADA')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')
        self.menu.estado = EstadoComprarEntradaIniciado(self.menu, None, None)

class EstadoCinesListados(EstadoMenu):
    def regresar(self):
        self.menu.estado = EstadoMenuPrincipal(self.menu, None, None)

class EstadoListarCarteleraIniciado(EstadoMenu):
    def escogerCine(self, idCine):
        cineFactory = CineFactory()
        cine = cineFactory.obtenerCine(idCine)
        self.menu.estado = EstadoCineEscogido1(self.menu, cine, None)

class EstadoCineEscogido1(EstadoMenu):
    def listarCartelera(self):
        peliculas = self.cine.listar_peliculas()
        print('********************')
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')
        self.menu.estado = EstadoCarteleraListada1(self.menu, None, None)

class EstadoCarteleraListada1(EstadoMenu):
    def regresar(self):
        self.menu.estado = EstadoMenuPrincipal(self.menu, None, None)

class EstadoComprarEntradaIniciado(EstadoMenu):
    def escogerCine(self, idCine):
        cineFactory = CineFactory()
        cine = cineFactory.obtenerCine(idCine)
        self.menu.estado = EstadoCineEscogido2(self.menu, cine, None)

class EstadoCineEscogido2(EstadoMenu):
    def listarCartelera(self):
        peliculas = self.cine.listar_peliculas()
        print('********************')
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')
        self.menu.estado = EstadoCarteleraListada2(self.menu, cine, None)

class EstadoCarteleraListada2(EstadoMenu):
    def escogerPelicula(self, pelicula):
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in cine.listar_funciones(pelicula_elegida):
            print('Función: {}'.format(funcion))
        self.menu.estado = EstadoPeliculaEscogida(self.menu, cine, pelicula)

class EstadoPeliculaEscogida(EstadoMenu):
    def escogerFuncion(self, funcion, entradas):
        codigo_entrada = cine.guardar_entrada(self.pelicula, funcion, entradas)
        print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        self.menu.estado = EstadoEntradaComprada(self.menu, None, None)

class EstadoEntradaComprada(EstadoMenu):
    def regresar(self):
        self.menu.estado = EstadoMenuPrincipal(self.menu, None, None)

class Menu:
    def __init__(self):
        self.estado = EstadoMenuPrincipal(self, None, None)

def main():
    terminado = False
    menu = Menu()
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            menu.estado.iniciarListarCines()
            menu.estado.regresar()

        elif opcion == '2':
            menu.estado.iniciarListarCartelera()
            idCine = input('Primero elija un cine:')
            menu.estado.escogerCine(idCine)
            menu.estado.listarCartelera()
            menu.estado.regresar()

        elif opcion == '3':
            menu.estado.iniciarComprarEntrada();
            idCine = input('Primero elija un cine:')
            menu.estado.escogerCine(idCine)
            menu.estado.listarCartelera()
            pelicula = input('Elija pelicula:')
            menu.estado.escogerPelicula(pelicula)
            funcion = input('Funcion:')
            entradas = input('Ingrese cantidad de entradas: ')
            menu.estado.escogerFuncion(funcion, entradas)
            menu.estado.regresar()

        elif opcion == '0':
            terminado = True
        else:
            print(opcion)

if __name__ == '__main__':
    main()
