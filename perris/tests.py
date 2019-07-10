from django.test import TestCase
from .models import Persona

# Create your tests here.
class PersonaTestCase(TestCase):
    def testGetDato(self):
        #Arrange
        expected = "prueba"
        result = ""
        #Act
        Persona.objects.create(rut="123456789", nombre ="prueba", apellidos ="aprueba", edad =22, telefono =1235412, email ="prueba@prueba.com", direccion ="pruebadirec")
        persona = Persona.objects.get(nombre='prueba')
        result = persona.nombre
        #Assert
        self.assertEqual(expected,result)

    def testCreacionPersona(self):
        #Arrange
        expected = 2
        result = 0
        #Act
        Persona.objects.create(rut="123456789", nombre ="prueba1", apellidos ="aprueba1", edad =22, telefono =1235412, email ="prueb1a@prueba.com", direccion ="pruebadirec3")
        Persona.objects.create(rut="214512345", nombre ="prueba2", apellidos ="aprueba2", edad =22, telefono =1235412, email ="prueb2a@prueba.com", direccion ="pruebadirec2")
        result = len(Persona.objects.all())
        #Assert
        self.assertEqual(expected,result)

    def testEliminacionMultiple(self):
        #Arrange
        expected = 0
        result = 0
        #Act
        Persona.objects.create(rut="123456789", nombre ="prueba1", apellidos ="aprueba1", edad =22, telefono =1235412, email ="prueb1a@prueba.com", direccion ="pruebadirec3")
        Persona.objects.create(rut="214512345", nombre ="prueba2", apellidos ="aprueba2", edad =22, telefono =1235412, email ="prueb2a@prueba.com", direccion ="pruebadirec2")
        Persona.objects.all().delete()
        result = len(Persona.objects.all())
        #Assert
        self.assertEqual(expected,result)