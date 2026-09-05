# CÉSAR RUEDA — CAMPUS CDE (`cesar-rueda-web`)
> **Consultorio Digital de Desprogramación Evolutiva & Sanación del Árbol Genealógico**  
> *Profesional Titular:* César Rueda Murillo  
> *Gestión Comercial & Enlace:* Julio  
> *Estrategia & Dirección:* Esteban Alfaro — [Marketing Strategy AI Solutions](file:///c:/Proyectos/Marketing%20Strategy%20AI%20Solutions)  
> *Despliegue Activo (Borrador Oficial):* [cesar-rueda-draft.netlify.app](https://cesar-rueda-draft.netlify.app/)  
> *Repositorio Git Oficial:* [github.com/thetebis-wq/cesar-rueda-web](https://github.com/thetebis-wq/cesar-rueda-web)  

---

## 📚 DOCUMENTACIÓN INTEGRAL DEL PROYECTO

Toda la inteligencia de negocio, técnica y de conversión se encuentra centralizada en la carpeta [`docs/`](docs/):

* 📄 **[Dossier General del Proyecto (`docs/PROJECT_OVERVIEW.md`)](docs/PROJECT_OVERVIEW.md):**  
  Identidad de César Rueda, metodología Campus CDE, dolores que atiende (dinero, relaciones, ansiedad), mercados internacionales (México, España, EE.UU.), modelo de costos $0 para el cliente y opciones de monetización para la agencia.
* 🛠️ **[Especificaciones Técnicas (`docs/TECHNICAL_SPECS.md`)](docs/TECHNICAL_SPECS.md):**  
  Arquitectura PWA, algoritmo del Escáner de 3 pasos, blindaje de privacidad Zero-PII (LFPDPPP/RGPD), optimización GEO Answer-First para motores de IA, accesibilidad WCAG 2.1 AA y suite de pruebas automatizadas.
* 📈 **[Estrategia de Marketing y Ventas (`docs/MARKETING_AND_SALES_STRATEGY.md`)](docs/MARKETING_AND_SALES_STRATEGY.md):**  
  Embudo de conversión completo, pack de guiones para videos virales de TikTok/Reels, protocolo de respuestas rápidas para WhatsApp Business, detección UTM dinámica y estructura de campaña piloto en Meta Ads.
* 🗺️ **[Hoja de Ruta y Backlog (`docs/ROADMAP.md`)](docs/ROADMAP.md):**  
  Hitos cumplidos al 100% en Fase 1 y tareas atómicas para las Fases 2 (Lanzamiento piloto), 3 (Automatización de agenda y cobros) y 4 (Agentes conversacionales de IA).
* 🏛️ **[Bitácora de Decisiones Arquitectónicas (`docs/DECISIONS_LOG.md`)](docs/DECISIONS_LOG.md):**  
  Compendio de decisiones heredadas del Framework Madre (`ADR-001` a `ADR-007`) y decisiones locales del consultorio digital.

---

## 📁 ESTRUCTURA DE ARCHIVOS DE LA RAÍZ

* [`index.html`](index.html): Aplicación web completa de una sola página (PWA). Incluye optimización móvil con barra de acción fija para el pulgar, metadatos OpenGraph con foto real, Schema.org estructurado (`ProfessionalService` y `FAQPage`), y el **Escáner de Lealtades Inconscientes de 3 pasos**.
* [`cesar-rueda.jpg`](cesar-rueda.jpg): Fotografía oficial de César Rueda, utilizada para generar confianza profesional y previsualización en redes sociales (WhatsApp, Instagram, Facebook).
* [`verify_draft.py`](verify_draft.py): Suite automatizada de verificación de sanidad y cumplimiento de calidad (Schema.org, OpenGraph, Zero-PII, HTTP 200).
* [`firebase.json`](firebase.json): Archivo de configuración de Firebase Hosting para el despliegue serverless rápido del consultorio.
* [`AGENTS.md`](AGENTS.md): Estándares de ingeniería de agentes (Addy Osmani) y Quality Gates obligatorios específicos para este repositorio.
* [`assets/`](assets/): Activos gráficos y capturas de referencia de la interfaz.

---

## 🧪 VERIFICACIÓN DE CALIDAD PRE-ENTREGA

Antes de realizar cualquier commit o entrega a cliente, ejecutar obligatoriamente:
```bash
python verify_draft.py
```
El script verifica la integridad de las 8 reglas de calidad y asegura que el despliegue público en Netlify responda `HTTP 200 OK`.

---

## 🚀 CÓMO ACTUALIZAR EL DESPLIEGUE EN NETLIFY

1. Ingresar a [app.netlify.com](https://app.netlify.com/) en el sitio **cesar-rueda-draft**.
2. Ir a la pestaña **Deploys**.
3. Arrastrar el archivo [`index.html`](index.html) al recuadro inferior de *Need to update your site? Drag and drop your site output folder here*.
4. En 5 segundos, la URL pública [cesar-rueda-draft.netlify.app](https://cesar-rueda-draft.netlify.app/) se actualizará de forma instantánea.
