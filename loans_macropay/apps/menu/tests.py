from loans_macropay.config.tests import ConfigAPITest
from rest_framework import status
import json


class MenuTestCase(ConfigAPITest):
    def setUp(self):
        self.user = self.create_user()
        self.path = "/menu/create/"
        self.authenticate(self.user)

    def test_create_menu(self):
        data_menu = [
            {
                "external_id": 11,
                "icon": "heroicons_solid:book-open",
                "key_menu": "administration",
                "link": "",
                "order_menu": 1,
                "parent_id": 10,
                "title": "Administración",
                "type_menu": "collapsable"
            },
            {
                "external_id": 12,
                "icon": "heroicons_outline:users",
                "key_menu": "users1",
                "link": "/ruta1",
                "order_menu": None,
                "parent_id": 11,
                "title": "Usuarios1",
                "type_menu": "basic"
            },
            {
                "external_id": 13,
                "icon": "heroicons_outline:key",
                "key_menu": "claves",
                "link": "/ruta2/",
                "order_menu": None,
                "parent_id": 11,
                "title": "claves",
                "type_menu": "basic"
            },
            {
                "external_id": 14,
                "icon": "heroicons_outline:banknotes",
                "key_menu": "accounts",
                "link": "/ruta3",
                "order_menu": None,
                "parent_id": 11,
                "title": "Cuentas",
                "type_menu": "basic"
            },
            {
                "external_id": 15,
                "icon": "heroicons_outline:lock-closed",
                "key_menu": "collapse",
                "link": "",
                "order_menu": 2,
                "parent_id": 10,
                "title": "Permisos",
                "type_menu": "collapsable"
            },
            {
                "external_id": 10,
                "icon": "",
                "key_menu": "configuration",
                "link": "",
                "order_menu": None,
                "parent_id": None,
                "title": "Configuración",
                "type_menu": "group"
            },
            {
                "external_id": 16,
                "icon": "heroicons_outline:user-circle",
                "key_menu": "users",
                "link": "/ruta4",
                "order_menu": None,
                "parent_id": 15,
                "title": "Usuarios",
                "type_menu": "basic"
            },
            {
                "external_id": 17,
                "icon": "heroicons_outline:lock-closed",
                "key_menu": "permissions",
                "link": "/ruta5",
                "order_menu": None,
                "parent_id": 15,
                "title": "Permisos",
                "type_menu": "basic"
            },
            {
                "external_id": 31,
                "icon": "heroicons_outline:globe-alt",
                "key_menu": "permissionsMenu",
                "link": "/ruta6",
                "order_menu": None,
                "parent_id": 15,
                "title": "Meny por Permisos",
                "type_menu": "basic"
            }
        ]
        response = self.client.post(f"{self.path}", data=json.dumps(data_menu), content_type='application/json')
        data_response = [
            {
                "title": "Configuración",
                "type": "group",
                "children": [
                    {
                        "title": "Administración",
                        "type": "collapsable",
                        "icon": "heroicons_solid:book-open",
                        "children": [
                            {
                                "id": 12,
                                "title": "Usuarios1",
                                "type": "basic",
                                "icon": "heroicons_outline:users",
                                "link": "/ruta1"
                            },
                            {
                                "id": 13,
                                "title": "claves",
                                "type": "basic",
                                "icon": "heroicons_outline:key",
                                "link": "/ruta2/"
                            },
                            {
                                "id": 14,
                                "title": "Cuentas",
                                "type": "basic",
                                "icon": "heroicons_outline:banknotes",
                                "link": "/ruta3"
                            }
                        ]
                    },
                    {
                        "title": "Permisos",
                        "type": "collapsable",
                        "icon": "heroicons_outline:lock-closed",
                        "children": [
                            {
                                "id": 16,
                                "title": "Usuarios",
                                "type": "basic",
                                "icon": "heroicons_outline:user-circle",
                                "link": "/ruta4"
                            },
                            {
                                "id": 17,
                                "title": "Permisos",
                                "type": "basic",
                                "icon": "heroicons_outline:lock-closed",
                                "link": "/ruta5"
                            },
                            {
                                "id": 31,
                                "title": "Meny por Permisos",
                                "type": "basic",
                                "icon": "heroicons_outline:globe-alt",
                                "link": "/ruta6"
                            }
                        ]
                    }
                ]
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data_response)

    def test_list_menu(self):
        self.test_create_menu()
        response = self.client.get(f"{self.path}")
        data_response = [
            {
                "title": "Configuración",
                "type": "group",
                "children": [
                    {
                        "title": "Administración",
                        "type": "collapsable",
                        "icon": "heroicons_solid:book-open",
                        "children": [
                            {
                                "id": 12,
                                "title": "Usuarios1",
                                "type": "basic",
                                "icon": "heroicons_outline:users",
                                "link": "/ruta1"
                            },
                            {
                                "id": 13,
                                "title": "claves",
                                "type": "basic",
                                "icon": "heroicons_outline:key",
                                "link": "/ruta2/"
                            },
                            {
                                "id": 14,
                                "title": "Cuentas",
                                "type": "basic",
                                "icon": "heroicons_outline:banknotes",
                                "link": "/ruta3"
                            }
                        ]
                    },
                    {
                        "title": "Permisos",
                        "type": "collapsable",
                        "icon": "heroicons_outline:lock-closed",
                        "children": [
                            {
                                "id": 16,
                                "title": "Usuarios",
                                "type": "basic",
                                "icon": "heroicons_outline:user-circle",
                                "link": "/ruta4"
                            },
                            {
                                "id": 17,
                                "title": "Permisos",
                                "type": "basic",
                                "icon": "heroicons_outline:lock-closed",
                                "link": "/ruta5"
                            },
                            {
                                "id": 31,
                                "title": "Meny por Permisos",
                                "type": "basic",
                                "icon": "heroicons_outline:globe-alt",
                                "link": "/ruta6"
                            }
                        ]
                    }
                ]
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data_response)
