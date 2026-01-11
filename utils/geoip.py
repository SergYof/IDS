# utils/geoip.py
try:
    import geoip2.database
    reader = geoip2.database.Reader("GeoLite2-City.mmdb")
except Exception:
    reader = None

def lookup(ip):
    if not reader:
        return "Unknown"

    try:
        r = reader.city(ip)
        return f"{r.country.name}, {r.city.name}"
    except Exception:
        return "Unknown"
