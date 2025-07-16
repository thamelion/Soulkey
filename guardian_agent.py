class SoulKey:
    def __init__(self, owner_name, guardian_name):
        self.owner = owner_name
        self.guardian = guardian_name
        self.identity_signature = ""
        self.is_active = True

    def set_identity_signature(self, signature):
        if self.is_active:
            self.identity_signature = signature
            print(f"Identidad digital actualizada: {signature}")
        else:
            print("SoulKey desactivada. No se puede modificar.")

    def verify_guardian(self, name):
        return name == self.guardian

    def transfer_guardianship(self, new_guardian, verifier):
        if self.verify_guardian(verifier):
            self.guardian = new_guardian
            print(f"Guardia transferida a {new_guardian}")
        else:
            print("Transferencia fallida: verificación del guardián actual fallida.")

    def deactivate(self, verifier):
        if self.verify_guardian(verifier):
            self.is_active = False
            print("SoulKey ha sido desactivada.")
        else:
            print("Desactivación fallida: solo el guardián puede hacerlo.")

    def info(self):
        return {
            "Propietario": self.owner,
            "Guardia actual": self.guardian,
            "Firma de identidad": self.identity_signature,
            "Estado": "Activo" if self.is_active else "Desactivado"
        }

# Ejemplo de uso
soulkey = SoulKey("Tom", "Luna")

soulkey.set_identity_signature("hash_de_identidad_de_Tom")
print(soulkey.info())

soulkey.transfer_guardianship("IA_Thamelion", "Luna")
print(soulkey.info())

soulkey.deactivate("IA_Thamelion")
print(soulkey.info())
