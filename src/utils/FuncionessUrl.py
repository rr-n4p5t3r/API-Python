from urllib.parse import urlparse


def obtener_puerto_peticion(url):
    parts_url = urlparse(url)
    return parts_url.port

def obtener_subdominio(url, dominio):
    parts_url = urlparse(url)
    host = parts_url.hostname    
    # Verificar si el dominio actual es igual al dominio válido
    if host == dominio:
        return None  # No hay subdominio
    else:
        # Obtener la parte final del dominio
        dominio_actual = '.'.join(host.split('.')[-2:])
        # Obtener el subdominio
        subdominio = host[:-(len(dominio_actual) + 1)]
        return subdominio

