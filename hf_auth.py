"""
Módulo de Autenticación Hugging Face

Proporciona funciones para autenticarse con Hugging Face Hub.
Necesario para publicar modelos.

USO:
====
from hf_auth import login_hf, get_hf_token

# Obtener token
token = get_hf_token()
print(f"✅ Token encontrado")

# Realizar login
if login_hf():
    print("✅ Listo para publicar modelos")
"""

import os


def get_hf_token():
    """
    Obtiene el token de Hugging Face desde .env
    
    Returns:
        str: Token HF
        
    Raises:
        ValueError: Si HF_TOKEN no está en .env
        
    Ejemplo:
        >>> token = get_hf_token()
        >>> print(f"Token: {token[:10]}...")
    """
    token = os.getenv('HF_TOKEN')
    
    if not token:
        raise ValueError(
            "❌ No se encontró HF_TOKEN en .env\n"
            "   Solución:\n"
            "   1. Obtén token: https://huggingface.co/settings/tokens\n"
            "   2. Edita .env: HF_TOKEN=hf_xxxxx\n"
            "   3. Intenta de nuevo"
        )
    
    return token


def login_hf():
    """
    Realiza login en Hugging Face Hub.
    
    Returns:
        bool: True si login exitoso
        
    Ejemplo:
        >>> if login_hf():
        ...     print("Listo para publicar")
    """
    try:
        from huggingface_hub import login
    except ImportError:
        print("❌ Instala huggingface-hub: pip install huggingface-hub")
        return False
    
    try:
        # Obtener token
        token = get_hf_token()
        
        # Realizar login
        login(token=token)
        print("✅ Login exitoso en Hub")
        return True
        
    except ValueError as e:
        # Error de get_hf_token
        print(f"❌ {e}")
        return False
        
    except Exception as e:
        print(f"❌ Error en login: {e}")
        return False


def verify_hf_token():
    """
    Verifica que el token de HF es válido.
    
    Returns:
        bool: True si token funciona, False en otro caso
        
    Ejemplo:
        >>> if verify_hf_token():
        ...     print("Token válido")
    """
    try:
        from huggingface_hub import HfApi
        
        token = get_hf_token()
        
        # Crear conexión a Hub
        api = HfApi(token=token)
        
        # Verificar obtener info del usuario (intenta conexión real)
        user = api.whoami()
        
        print(f"✅ Token válido - Usuario: {user['name']}")
        return True
        
    except ValueError as e:
        # Token no configurado
        print(f"❌ {e}")
        return False
        
    except Exception as e:
        print(f"❌ Token inválido o sin conexión: {e}")
        return False
