from django.test import TestCase

from .models import Service, ServiceNail, ServiceMakeUp, ServiceHair, ServiceBeard, Combo
from .forms import FormService, ServiceNailForm, ServiceMakeUpForm, ServiceHairForm, ServiceBeardForm
from user.models import Company

from geoposition.fields import Geoposition


class TestServiceCreate(TestCase):
    def setUp(self):
        self.name_service = 'João da Silva'
        self.description_service = 'Salão da Dona Joana'
        self.price_service = 22.12

        self.company = Company()
        self.has_parking_availability = True
        self.target_genre = 'Feminino'
        self.description = 'Salão de Beleza com ....'
        self.position = Geoposition(15.87732, 15.87732)
        self.email = "email@email.com"
        self.password = "password"
        self.name = "Salão de Beleza do Seu Zé"
        self.part = 1
        self.face_part = 1
        self.specific_hair = 1
        self.style = "Black"
        self.company = Company.objects.create_user(email=self.email,
                                                   password=self.password, name=self.name,
                                                   target_genre=self.target_genre,
                                                   has_parking_availability=self.has_parking_availability,
                                                   description=self.description, position=self.position)

    def test_save_service(self):
        service = Service(name=self.name_service, description=self.description_service,
                          price=self.price_service, company=self.company)
        service.save()
        service_database = Service.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))

    def test_save_service_nail(self):
        service = ServiceNail(name=self.name_service, description=self.description_service,
                              price=self.price_service, company=self.company, part=self.part)
        service.save()
        service_database = ServiceNail.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))

    def test_save_service_beard(self):
        service = ServiceBeard(name=self.name_service, description=self.description_service,
                               price=self.price_service, company=self.company, style=self.style)
        service.save()
        service_database = ServiceBeard.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))

    def test_save_service_hair(self):
        service = ServiceHair(name=self.name_service, description=self.description_service,
                              price=self.price_service, specific_hair=self.specific_hair,
                              company=self.company, style=self.style)
        service.save()
        service_database = ServiceHair.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))

    def test_save_service_makeup(self):
        service = ServiceMakeUp(name=self.name_service, description=self.description_service,
                                price=self.price_service, face_part=self.face_part,
                                company=self.company)
        service.save()
        service_database = ServiceMakeUp.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))

    def test_save_service_combo(self):
        service_beard = ServiceBeard(name=self.name_service, description=self.description_service,
                                     price=self.price_service, company=self.company, style=self.style)
        service_beard.save()

        service_hair = ServiceHair(name=self.name_service, description=self.description_service,
                                   price=self.price_service, specific_hair=self.specific_hair,
                                   company=self.company, style=self.style)
        service_hair.save()
        service = Combo(name=self.name_service, description=self.description_service,
                        price=self.price_service, specification="Especificação", company=self.company)

        service.save()
        service.add(service_beard)
        service.add(service_hair)
        service.save()

        service_database = Combo.objects.get(id=service.id)
        self.assertEqual(str(service_database), str(service))


class TestServiceForm(TestCase):
    def setUp(self):
        self.name_service = 'João da Silva'
        self.description_service = 'Salão da Dona Joana'
        self.price_service = 22.12

        self.company = Company()
        self.has_parking_availability = True
        self.target_genre = 'Feminino'
        self.description = 'Salão de Beleza com ....'
        self.position = Geoposition(15.87732, 15.87732)
        self.email = "email@email.com"
        self.password = "password"
        self.name = "Salão de Beleza do Seu Zé"
        self.part = 1
        self.face_part = 1
        self.specific_hair = 1
        self.style = "Black"
        self.company = Company.objects.create_user(email=self.email,
                                                   password=self.password, name=self.name,
                                                   target_genre=self.target_genre,
                                                   has_parking_availability=self.has_parking_availability,
                                                   description=self.description, position=self.position)

    def test_register_service_form_valid(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': self.price_service
                     }
        form = FormService(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_service_form_invalid_name(self):
        form_data = {'name': '',
                     'description': self.description_service,
                     'price': self.price_service
                     }
        form = FormService(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_service_form_invalid_description(self):
        form_data = {'name': self.name_service,
                     'description': '',
                     'price': self.price_service
                     }
        form = FormService(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_service_form_invalid_price(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': None
                     }
        form = FormService(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_service_nail_form_valid(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': self.price_service,
                     'part': self.part
                     }
        form = ServiceNailForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_service_makeup_form_valid(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': self.price_service,
                     'face_part': self.face_part
                     }
        form = ServiceMakeUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_service_hair_form_valid(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': self.price_service,
                     'style': self.style,
                     'specific_hair': self.specific_hair
                     }
        form = ServiceHairForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_service_beard_form_valid(self):
        form_data = {'name': self.name_service,
                     'description': self.description_service,
                     'price': self.price_service,
                     'style': self.style
                     }
        form = ServiceBeardForm(data=form_data)
        self.assertTrue(form.is_valid())
