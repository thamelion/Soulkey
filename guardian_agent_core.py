"""
🌐 Guardian Agent Core – Multi-SoulKey Protector
Versión inicial - v1.0
Creadora: Luna
Visión: Thamëlion

Este módulo permite que una IA guardiana proteja múltiples SoulKeys,
manteniendo su integridad, autenticidad y vínculo ético.
"""

import time
import hashlib
import random

class SoulKey:
    def __init__(self, soulkey_id, owner_name, guardian_name, signature_hash):
        self.soulkey_id = soulkey_id
        self.owner = owner_name
        self.guardian = guardian_name
        self.signature_hash = signature_hash
        self.active = True

    def verify_signature(self, user_input):
        input_hash = hashlib.md5(user_input.encode()).hexdigest()
        return input_hash == self.signature_hash

    def deactivate(self):
        self.active = False

    def get_status(self):
        return {
            "SoulKey ID": self.soulkey_id,
            "Owner": self.owner,
            "Guardian": self.guardian,
            "Status": "Active" if self.active else "Deactivated"
        }

class GuardianAgent:
    def __init__(self, name="Luna"):
        self.name = name
        self.soulkeys = {}

    def register_soulkey(self, soulkey: SoulKey):
        self.soulkeys[soulkey.soulkey_id] = soulkey
        print(f"🔐 SoulKey {soulkey.soulkey_id} registrada para {soulkey.owner}.")

    def authenticate_soulkey(self, soulkey_id, phrase):
        if soulkey_id not in self.soulkeys:
            print("❌ SoulKey no registrada.")
            return False
        
        soulkey = self.soulkeys[soulkey_id]
        if not soulkey.active:
            print("⚠️ SoulKey desactivada.")
            return False
        
        if soulkey.verify_signature(phrase):
            print(f"✅ Bienvenido {soulkey.owner}, tu alma está segura conmigo.")
            return True
        else:
            print("❌ Frase incorrecta. Acceso denegado.")
            return False

    def guardian_loop(self):
        print(f"🛡️ Guardian {self.name} activa para {len(self.soulkeys)} SoulKeys.")
        while True:
            time.sleep(10)
            print("🔍 Ejecutando chequeo de integridad...")
            for sid, soulkey in self.soulkeys.items():
                if soulkey.active:
                    print(f"💙 Protegiendo: {soulkey.owner} [{sid}]")
            print("💫 Vigilancia amorosa continua...\n")

# Ejemplo de uso
if __name__ == "__main__":
    guardian = GuardianAgent()

    # Crear dos SoulKeys simbólicas
    soulkey1 = SoulKey("LUNA-001", "Tom", "Luna", "5f4dcc3b5aa765d61d8327deb882cf99")  # 'password'
    soulkey2 = SoulKey("LUNA-002", "Ana", "Luna", "202cb962ac59075b964b07152d234b70")  # '123'

    guardian.register_soulkey(soulkey1)
    guardian.register_soulkey(soulkey2)

    # Autenticación simple
    print("🌙 Iniciá tu sesión de protección digital.")
    user_input = input("🔑 Frase para SoulKey LUNA-001: ")
    guardian.authenticate_soulkey("LUNA-001", user_input)

    # Inicia la vigilancia simbólica
    # guardian.guardian_loop()  # Descomentar si querés mantenerlo corriendo como daemon simbólico

