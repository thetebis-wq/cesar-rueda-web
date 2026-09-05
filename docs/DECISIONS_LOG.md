# BITÁCORA DE DECISIONES ARQUITECTÓNICAS (ADRS HEREDADOS Y LOCALES)
> **Proyecto:** César Rueda — Campus CDE (`cesar-rueda-web`)  
> **Framework Madre:** Marketing Strategy AI Solutions  

---

## 🏛️ REGISTRO DE DECISIONES CLAVE

### [ADR-007] Transición a Arquitectura Multi-Repo Desacoplada
* **Decisión:** Separar los proyectos de clientes del repositorio central de la agencia (`Marketing Strategy AI Solutions`) hacia repositorios Git independientes (ej. `thetebis-wq/cesar-rueda-web`).
* **Impacto en este proyecto:** Código, historial y despliegue completamente aislados. Máxima privacidad para los consultantes de César y cero riesgo de fuga de datos hacia otros clientes o proyectos.

### [ADR-002] Blindaje de Privacidad y Pipeline Zero-PII
* **Decisión:** Ningún dato personal sensible (motivos de consulta, dinámicas familiares, respuestas de lealtades) se recopila en bases de datos sin consentimiento expreso.
* **Impacto en este proyecto:** El Escáner de 3 pasos se ejecuta íntegramente en el navegador del usuario y transfiere las variables mediante codificación URL a WhatsApp. Cumplimiento estricto con LFPDPPP (México) y RGPD (Unión Europea).

### [ADR-004] Desacoplamiento de Ecosistemas Tecnológicos
* **Decisión:** La suite Google AI Pro (Esteban) se usa como motor de inteligencia, copy, estrategia y código. El cliente final opera con infraestructura inicial a costo $0 (Firebase Hosting, Netlify Free, WhatsApp Business, Cal.com).
* **Impacto en este proyecto:** Julio y César no pagan costes fijos recurrentes de tecnología para validar su propuesta de mercado.

### [ADR-006] Calidad de Ingeniería de Agentes (Addy Osmani Discipline)
* **Decisión:** Gobernanza del desarrollo bajo el ciclo de vida de 6 etapas (`DEFINE`, `PLAN`, `BUILD`, `VERIFY`, `REVIEW`, `SHIP`) y Quality Gates automatizados.
* **Impacto en este proyecto:** Establecimiento de `AGENTS.md` y de la suite de pruebas `python verify_draft.py` como barrera obligatoria de paso antes de cualquier commit o despliegue.

### [ADR-LOCAL-001] Autocontención y Embebido de Medios Críticos
* **Decisión:** Integrar la foto profesional oficial de César Rueda en formato Base64 dentro del código HTML para despliegues instantáneos sin fallos de CDN, y mantener el archivo binario `cesar-rueda.jpg` en raíz para previsualizaciones de tarjetas OpenGraph y Twitter.
* **Impacto en este proyecto:** 100% de fiabilidad visual en cualquier dispositivo, sin dependencias externas de hosting de imágenes.
