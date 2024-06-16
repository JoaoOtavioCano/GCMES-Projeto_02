from .database import Database
from .emailManager import EmailManager
from .payloadValidator import PayloadValidator

import random
import hashlib

class ForgotPassword:
    def _init_(self, request, payload):
        self.request = request
        self.payload = payload

    def respond(self):
        expected_payload_keys = ["email"]

        payload_validator = PayloadValidator()
        
        if not payload_validator.validate(self.payload, expected_payload_keys):
            self.request.send_error(500, "INVALID PAYLOAD")
            self.request.end_headers()
        else:
            email = self.payload["email"]

            email_manager = EmailManager()

            code  = self._createCode_()
            
            saved = self._saveCodeInDb_(code)

            if saved:
                email_manager.sendEmailToCreateNewPassword(email, code)

                self.request.send_response(200, "OK")
                self.request.end_headers()
            else:
                self.request.send_error(500, "USER NOT FOUND")
                self.request.end_headers()


    def _createCode_(self):
        code =  hashlib.sha256(str(random.randrange(9999999999)).encode()).hexdigest()

        return code

    def _saveCodeInDb_(self, code):
        db = Database()

        email = self.payload["email"]

        user_id = db.getUserId(email)

        if user_id == None:
            return False

        db.deletePasswordRequest(user_id)

        db.addNewPasswordRequest(code, user_id)

        return True
