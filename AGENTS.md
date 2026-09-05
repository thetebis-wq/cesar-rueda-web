# AGENTS.md — Client Engineering Discipline & Standards
# Proyecto: César Rueda — Campus CDE (cesar-rueda-web)
# Framework Madre: Marketing Strategy AI Solutions

> **Alcance:** Este archivo gobierna el comportamiento técnico de los agentes de IA (Google Antigravity, Gemini CLI, Claude Code) en este repositorio de cliente.
> **Herencia:** Hereda los estándares del Framework Central de la Agencia (`Marketing Strategy AI Solutions`) basados en *Production-Grade Engineering Skills for AI Coding Agents* (Addy Osmani).

---

## 🧭 CICLO DE VIDA OBLIGATORIO (6 ETAPAS)

Todo cambio o nueva funcionalidad en este proyecto debe ejecutarse siguiendo las 6 etapas:
1. **DEFINE (`/spec`):** Especificar el requerimiento (ej. nueva sección, nuevo test, cambio de copys o nuevo servicio).
2. **PLAN (`/plan`):** Desglosar en tareas atómicas con orden de dependencias.
3. **BUILD (`/build`):** Desarrollo incremental en rebanadas delgadas (Mobile-first, semántica HTML5 pura).
4. **VERIFY (`/test`):** Ejecutar obligatoriamente `python verify_draft.py` para validar que los 8 checks pasen al 100%.
5. **REVIEW (`/review`):** Revisión de calidad (accesibilidad, performance, seguridad, zero-PII).
6. **SHIP (`/ship`):** Despliegue verificado en Netlify/Firebase y prueba de URL pública 200 OK.

---

## 🎯 QUALITY GATES ESPECÍFICOS DEL CLIENTE

* **Privacidad Zero-PII (LFPDPPP / RGPD):** Ningún dato personal sensible (respuestas de lealtades inconscientes, nombres o correos) se almacena en base de datos sin consentimiento expreso. El escáner redirige a WhatsApp con mensaje prearmado vía parámetros URL.
* **Accesibilidad (WCAG 2.1 AA):** Tap targets mínimos de 48px, contraste de color verificado, atributos ARIA (`aria-expanded`, `aria-label`, `role="region"`).
* **Core Web Vitals:** LCP < 2.5s en conexiones 4G móvil, sin saltos de diseño (CLS = 0).
* **SEO & GEO Semántico:** Schema.org JSON-LD con `ProfessionalService` (moneda EUR) y `FAQPage`, bloque Answer-First optimizado para motores de búsqueda con IA.
* **Suite de Verificación:** Ningún cambio puede ser commiteado si `python verify_draft.py` arroja algún fallo.

---

## 🔄 RETROALIMENTACIÓN HACIA EL CORE (UPSTREAM)

Cuando se implemente una mejora o se descubra un insight de alta conversión en este proyecto (ej. nuevo hook de copy, componente interactivo o mejora de velocidad), debe documentarse y comunicarse al framework central en `Marketing Strategy AI Solutions` para enriquecer los playbooks y ADRs de la agencia.
