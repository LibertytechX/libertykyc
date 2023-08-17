from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import urlencode
import requests, json

User = get_user_model()

class DojahVerifications:
    baseUrl = settings.DOJAH_BASE_URL
    secret_key = settings.DOJAH_PUBLIC_SECRET_KEY
    app_id = settings.DOJAH_APP_ID

    headers = {
        "AppId": f"{app_id}",
        "Authorization": f"{secret_key}"
    }

    @classmethod
    def verify_bvn_with_dojah(cls, bvn, user: User = None):
        """
        Lookup a provided bvn against government Database
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "bvn": "22171234567",
                        "first_name": user.first_name if user else "JOHN",
                        "last_name": user.last_name if user else "DOE",
                        "middle_name": "AHMED",
                        "gender": "Male",
                        "date_of_birth": "1997-05-16",
                        "phone_number1": user.phone_number if user else "09087231333",
                        "image": "BASE 64 IMAGE",
                        "email": user.email if user else "johndoe@gmail.com",
                        "enrollment_bank": "GTB",
                        "enrollment_branch": "IKEJA",
                        "level_of_account": "LEVEL 2",
                        "lga_of_origin": "OSOGBO",
                        "lga_of_residence": "IKEJA",
                        "marital_status": "SINGLE",
                        "name_on_card": "",
                        "nationality": "NIGERIAN",
                        "nin": "70123456789",
                        "phone_number2": "08012345678",
                        "registration_date": "",
                        "residential_address": "",
                        "state_of_origin": "OSUN",
                        "state_of_residence": "LAGOS",
                        "title": "MISS",
                        "watch_listed": "NO"
                    }
                }
        else:
            query_params = {
                            "bvn": {bvn}
                            }

            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/bvn/advance"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp

    @classmethod
    def match_bvn_and_user_details_with_dojah(cls, bvn, user: User=None, first_name="", last_name="", dob=""):
        """
        Returns boolean values to show that bvn matches any of account_number, 
        firstname, lastname or middle_name.
        dob format = "yyyy-mm-dd. The bvn is required.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "bvn": {
                            "value": "23456789012",
                            "status": "true"
                        },
                        "first_name": {
                            "confidence_value": 100,
                            "status": "true"
                        }
                    }
                }
        else:
            query_params = {
                "bvn": {bvn},
                "first name": {user.first_name} if user else first_name,
                "last name": {user.last_name} if user else last_name,
                "dob": {user.dob} if user else dob
            }

            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/bvn"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp

    @classmethod
    def verify_nin_with_dojah(cls, nin, user: User=None):
        """
        Lookup a provided NIN against government Database
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "nin": "70123456789",
                        "firstname": user.first_name if user else "John",
                        "middlename": "Doe",
                        "surname": user.last_name if user else "Alamutu",
                        "telephoneno": "08012345678",
                        "birthdate": "01-01-1982",
                        "photo": "/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgc...",
                        "gender": "m",
                    }
                }
        else:
            query_params = {
                "nin": {nin}
                }
            
            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/nin"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp    

    @classmethod
    def verify_virtual_nin_with_dojah(cls, vnin, user: User=None):
        """
        Users will generate the virtual NIN from
        the NIMC mobile app. This 12-digit code is vald
        for 72 hours.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "vnin": "AB012345678910YZ",
                        "firstname": user.first_name if user else "John",
                        "middlename": "Doe",
                        "surname": user.last_name if user else "Alamutu",
                        "user_id": "WXABCD-1234",
                        "gender": "M",
                        "mobile": user.phone_number if user else "08012345678",
                        "dateOfBirth": "YYYY-MM-DD",
                        "photo": "/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgc..."
                    }
                }
        else:
            query_params = {
                "vnin": {vnin}
                }
            
            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/vnin"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp
    
    @classmethod
    def verify_drivers_licence_with_dojah(cls, license_number, user: User=None):
        """
        Users will generate the virtual NIN from
        the NIMC mobile app. This 12-digit code is vald
        for 72 hours.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "uuid": "1625583696",
                        "licenseNo": "FKJ494A2133",
                        "firstName": user.first_name if user else "JOHN",
                        "lastName": user.last_name if user else "DOE",
                        "middleName": "",
                        "gender": "Male",
                        "issuedDate": "2019-01-25",
                        "expiryDate": "2024-08-17",
                        "stateOfIssue": "LAGOS",
                        "birthDate": "28-09-1998",
                        "photo": "BASE 64 IMAGE"
                    }
                }
        else:
            query_params = {
                "license_number": {license_number}
                }
            
            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/dl"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp

    @classmethod
    def verify_voters_id_with_dojah(cls, vin, user: User=None):
        """
        returns user details for a provided VIN
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                                "full_name": user.get_full_name() if user else "ADEMOLA WASIU KOLAWOLE",
                                "voter_identification_number": "91F6B1F5BE295355586",
                                "gender": "Male",
                                "occupation": "STUDENT",
                                "time_of_registration": "2011-02-18 13:59:46",
                                "state": "ONDO",
                                "local_government": "IDANRE",
                                "registration_area_ward": "ISALU JIGBOKIN",
                                "polling_unit": "OJAJIGBOKIN, O/S IN FRONT OF ABANA I & II",
                                "polling_unit_code": "18/07/07/005",
                                "address": "NO 16 OWODE QTS KABBA",
                                "phone": "0812345678",
                                "date_of_birth": "1960-10-16"
                            }
                        }
        else:
            query_params = {
                "vin": {vin}
                }
            
            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/vin"
            url = init_url + "?" + encoded_params
            headers = cls.headers

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp
    
    @classmethod
    def verify_international_passport_with_dojah(cls, passport_number, surname, user: User=None):
        """
        Users will generate the virtual NIN from
        the NIMC mobile app. This 12-digit code is vald
        for 72 hours.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "passport_number": "A00123456",
                        "date_of_issue": "01/02/2000",
                        "expiry_date": "01/02/2000",
                        "document_type": "Standard Passport",
                        "issue_place": "LAGOS",
                        "surname": user.last_name if user else "JOHN",
                        "first_name": user.first_name if user else "DOE",
                        "other_names": "MOSES",
                        "date_of_birth": "10/06/1993",
                        "gender": "Undecided",
                        "photo": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBA..."
                    }
                }
        else:
            query_params = {
                "passport_number": {passport_number},
                "surname": {surname}
                }
            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/passport"
            url = init_url + "?" + encoded_params
            headers = cls.baseUrl

            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp

    @classmethod
    def verify_age_identity_with_dojah(cls, account_number, bank_code, dob, first_name, last_name, user: User=None):
        """
        Confirms that the user details submitted are correct. With the account_number, 
        phone_number or bvn selected as mode the age, surname or last name of the user 
        may be confirmed as true or false. It in effect returns a boolean value 
        for the verification.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "first_name": user.first_name if user else "ADEOLA",
                        "last_name": user.last_name if user else "SEMIU",
                        "date_of_birth": "1993-06-10",
                        "verification": "true"
                    }
                }
        else:
            query_params = {
                "mode": {account_number},
                "account_number": {account_number},
                "bank_code": {bank_code},
                "dob": {dob},
                "first_name": {first_name},
                "last_name": {last_name}
            }

            encoded_params = urlencode(query_params)
            init_url = f"{cls.baseUrl}/api/v1/kyc/age_verification"
            url = init_url + "?" + encoded_params
            
            headers = cls.headers
            response = requests.request("GET", url, headers=headers)
            resp = json.loads(response.text)
        return resp
    
    @classmethod
    def verify_bvn_selfie_image_with_dojah(cls, selfie_image, bvn, user: User=None):
        """
        Returns a confidence value from 90% and above represents a successful match else a mismatch.
        The selfie image should be converted to a base64 string.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "bvn": "22156341123",
                        "first_name": user.first_name if user else "ADEYEMO",
                        "middle_name": "ADELEKE",
                        "last_name": user.last_name if user else "AKIN",
                        "date_of_birth": "15-Apr-1985",
                        "phone_number1": "08134720263",
                        "phone_number2": "",
                        "gender": "Male",
                        "enrollment_bank": "044",
                        "enrollment_branch": "BBA LAGOS,BANK PLAZA",
                        "email": "adelek@yahoo.com",
                        "lga_of_origin": "Obafemi Owode",
                        "lga_of_residence": "Ojo",
                        "marital_status": "Single",
                        "nin": "76221462632",
                        "name_on_card": "ADEYEMO ADELEKE AKIN",
                        "residential_address": "1, OMOLOLA CLOSE CASSIDY BUS STOP OKOKOMAIKO.",
                        "state_of_origin": "Ogun State",
                        "state_of_residence": "Lagos State",
                        "watch_listed": "NO",
                        "level_of_account": "Level 2 - Medium Level Accounts",
                        "registration_date": "",
                        "image": "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",
                        "selfie_verification": {
                        "confidence_value": 99.99803924560547,
                        "match": "true"
                        }
                    }
                }
        else:
            url = f"{cls.baseUrl}/api/v1/kyc/bvn/verify"
            headers = cls.headers
            
            data = {
                    "selfieimage": f"{selfie_image}",
                    "bvn": f"{bvn}"
                    }

            response = requests.request("POST", url, headers=headers, data=data)
            resp = json.loads(response.text)
        return resp
    
    @classmethod
    def verify_virtual_vin_selfie_image_with_dojah(cls, vnin, selfie_image, user: User=None):
        """
        Returns a confidence value from 90% and above represents a successful match else a mismatch.
        The selfie image should be converted to a base64 string.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity": {
                        "firstname": user.first_name if user else "John",
                        "middlename": "Asake",
                        "surname": "Doe",
                        "userid": "WXLLUK-1011",
                        "gender": "M",
                        "photo": "/9j/4AA....",
                        "vnin": "EE848965768582SO",
                        "telephoneno": "2348012345678",
                        "birthdate": "18-05-1992",
                        "selfie_verification": {
                            "confidence_value": 0,
                            "match": "false"
                        }
                    }
                }
        else:
            url = f"{cls.baseUrl}/api/v1/kyc/vnin/verify"            
            headers = cls.headers
            
            data = {
                    "selfieimage": f"{selfie_image}",
                    "bvn": f"{vnin}"
                    }

            response = requests.request("POST", url, headers=headers, data=data)
            resp = json.loads(response.text)
        return resp
    
    @classmethod
    def liveness_check_with_dojah(cls, sprite):
        """
        Returns a confidence value from 90% and above represents a successful match else a mismatch.
        The image should be converted to a base64 string.
        """
        if settings.ENVIRONMENT == "development":
            resp = {
                    "entity":{
                    "liveness": {
                            "liveness_check": "false",
                            "liveness_probability": 0.014614949759561568
                        },
                        "face": {
                            "face_detected": "true",
                            "message": "face detected",
                            "multiface_detected": "false",
                            "details": {
                                "age_range": {
                                    "low": 25,
                                    "high": 35
                                },
                                "smile": {
                                    "value": "false",
                                    "confidence": 92.67727661132812
                                },
                                "gender": {
                                    "value": "Female",
                                    "confidence": 99.92608642578125
                                },
                                "eyeglasses": {
                                    "value": "false",
                                    "confidence": 96.146484375
                                },
                                "sunglasses": {
                                    "value": "false",
                                    "confidence": 99.99609375
                                },
                                "beard": {
                                    "value": "false",
                                    "confidence": 85.18626403808594
                                },
                                "mustache": {
                                    "value": "false",
                                    "confidence": 96.13561248779297
                                },
                                "eyes_open": {
                                    "value": "true",
                                    "confidence": 88.61351776123047
                                },
                                "mouth_open": {
                                    "value": "false",
                                    "confidence": 76.0062484741211
                                },
                                "emotions": [
                                    {
                                        "type": "CALM",
                                        "confidence": 81.77631378173828
                                    },
                                    {
                                        "type": "FEAR",
                                        "confidence": 6.811796188354492
                                    },
                                    {
                                        "type": "SURPRISED",
                                        "confidence": 6.772216320037842
                                    },
                                    {
                                        "type": "SAD",
                                        "confidence": 6.691151142120361
                                    },
                                    {
                                        "type": "ANGRY",
                                        "confidence": 2.304255723953247
                                    },
                                    {
                                        "type": "DISGUSTED",
                                        "confidence": 2.147843599319458
                                    },
                                    {
                                        "type": "HAPPY",
                                        "confidence": 1.2251189947128296
                                    },
                                    {
                                        "type": "CONFUSED",
                                        "confidence": 0.9095264673233032
                                    }
                                ]
                            },
                            "quality": {
                                "brightness": 65.93645477294922,
                                "sharpness": 97.45164489746094
                            },
                            "confidence": 99.99896240234375,
                            "bounding_box": {
                                "width": 0.4954420328140259,
                                "height": 0.39241859316825867,
                                "left": 0.27790528535842896,
                                "top": 0.3333175778388977
                            }
                        }
                    }
                }
        else:
            url = f"{cls.baseUrl}/api/v1/ml/liveness/"            
            headers = cls.headers
            
            data = {
                    "image": f"{sprite}"
                    }

            response = requests.request("POST", url, headers=headers, data=data)
            resp = json.loads(response.text)
        return resp    