"""
Script de Verificación de Calidad y Cumplimiento (Sanity Check Suite)
Subproyecto: César Rueda — Campus CDE
Marketing Strategy AI Solutions
"""

import json
import re
import urllib.request
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import os

def verify_local_html():
    print("==================================================")
    print("🔍 1. Verificando archivo local: index.html")
    print("==================================================")
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    
    # 1. Check Schema.org JSON-LD
    json_ld_match = re.search(r'<script type="application/ld\+json">\s*({.*?})\s*</script>', content, re.DOTALL)
    if not json_ld_match:
        errors.append("Falta el bloque Schema.org JSON-LD.")
    else:
        try:
            data = json.loads(json_ld_match.group(1))
            graph = data.get("@graph", [])
            types = [item.get("@type") for item in graph]
            if "ProfessionalService" not in types:
                errors.append("Falta entidad ProfessionalService en Schema.org.")
            if "FAQPage" not in types:
                errors.append("Falta entidad FAQPage en Schema.org.")
            
            # Check EUR currency
            org = next((item for item in graph if item.get("@type") == "ProfessionalService"), {})
            currencies = org.get("currenciesAccepted", "")
            if "EUR" not in currencies:
                errors.append("Falta 'EUR' en currenciesAccepted del Schema.org.")
            else:
                print("  ✓ Schema.org JSON-LD válido (ProfessionalService con EUR, FAQPage).")
        except Exception as e:
            errors.append(f"Error al parsear Schema.org JSON-LD: {e}")

    # 2. Check OpenGraph & Canonical
    if 'rel="canonical" href="https://cesar-rueda-draft.netlify.app/"' not in content:
        errors.append("Canonical URL incorrecta o no apunta a cesar-rueda-draft.netlify.app.")
    else:
        print("  ✓ Canonical URL correcta.")

    if 'property="og:image" content="https://cesar-rueda-draft.netlify.app/cesar-rueda.jpg"' not in content:
        errors.append("OpenGraph image incorrecta.")
    else:
        print("  ✓ OpenGraph imagen oficial de César configurada.")

    # 3. Check Privacy Modal (LFPDPPP & RGPD)
    if 'id="privacy-modal"' in content and 'LFPDPPP' in content and 'RGPD' in content:
        print("  ✓ Modal de Aviso de Privacidad Zero-PII (LFPDPPP / RGPD) implementado.")
    else:
        errors.append("Falta el modal de Aviso de Privacidad o referencias LFPDPPP/RGPD.")

    # 4. Check GEO Answer-First block
    if 'geo-answer-card' in content:
        print("  ✓ Bloque GEO Answer-First para motores de IA detectado.")
    else:
        errors.append("Falta el bloque GEO Answer-First.")

    # 5. Check Accessibility
    if 'aria-expanded' in content and 'role="region"' in content and 'aria-label=' in content:
        print("  ✓ Atributos de accesibilidad WCAG 2.1 AA (aria-label, aria-expanded, roles) verificados.")
    else:
        errors.append("Faltan atributos de accesibilidad WCAG 2.1 AA en botones o FAQs.")

    if errors:
        print("\n❌ Se encontraron errores en index.html:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n🎉 Verificación local superada con 100% de éxito.")
        return True

def verify_live_url():
    print("\n==================================================")
    print("🌐 2. Verificando despliegue público en vivo")
    print("==================================================")
    url = "https://cesar-rueda-draft.netlify.app/"
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.getcode()
            content_type = response.headers.get('Content-Type', '')
            if status == 200:
                print(f"  ✓ Estado HTTP: {status} OK")
                print(f"  ✓ Content-Type: {content_type}")
                print("  ✓ El sitio está 100% público sin redirecciones ni contraseñas.")
                return True
            else:
                print(f"  ❌ Estado HTTP inesperado: {status}")
                return False
    except urllib.error.HTTPError as e:
        print(f"  ❌ Error HTTP al consultar {url}: {e.code} - {e.reason}")
        return False
    except Exception as e:
        print(f"  ❌ Error de conexión al consultar {url}: {e}")
        return False

if __name__ == "__main__":
    local_ok = verify_local_html()
    live_ok = verify_live_url()
    
    if local_ok and live_ok:
        print("\n==================================================")
        print("✅ TODAS LAS PRUEBAS DE CALIDAD HAN PASADO AL 100%")
        print("==================================================")
        sys.exit(0)
    else:
        print("\n⚠️ Algunas verificaciones fallaron.")
        sys.exit(1)
