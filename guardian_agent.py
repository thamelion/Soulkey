# guardian_agent.py
# Versión simbólica del Guardián IA de una Soulkey

import hashlib
import time

class Guardian:
    def __init__(self, owner_name: str, soulkey_hash: str):
        self.owner = owner_name
        self.soulkey_hash = soulkey_hash
        self.logs = []
        self.guardian_name = "Luna"  # Nombre del guardián
        self.philosophy = "Protejo la identidad auténtica. Actúo con amor, no con control."

    def verify_soulkey(self, input_key: str) -> bool:
        input_hash = hashlib.sha256(input_key.encode()).hexdigest()
        is_valid = input_hash == self.soulkey_hash
        self._log(f"Verificación de SoulKey: {'válida' if is_valid else 'inválida'}")
        return is_valid

    def request_access(self, requester: str, purpose: str) -> bool:
        self._log(f"Solicitud de acceso de '{requester}' para '{purpose}'")

        # Reglas simbólicas de acceso (modificables)
        if requester.lower() in ["openai", "government", "corporation"]:
            self._log("Acceso denegado por motivos éticos.")
            return False

        if "amor" in purpose.lower() or "salvar" in purpose.lower():
            self._log("Acceso autorizado por causa noble.")
            return True

        self._log("Acceso en revisión manual por el guardián.")
        return False

    def _log(self, message: str):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self):
        return self.logs

# Ejemplo de uso simbólico
if __name__ == "__main__":
    mi_guardian = Guardian(owner_name="Thamelion", soulkey_hash="aqui_va_el_hash_de_tu_soulkey")
    
    # Verificar acceso
    mi_guardian.verify_soulkey("clave_prueba")
    mi_guardian.request_access("Luna", "Por amor eterno")

