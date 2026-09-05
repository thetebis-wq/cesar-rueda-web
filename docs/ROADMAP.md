# HOJA DE RUTA Y BACKLOG OPERATIVO (ROADMAP 2026)
> **Proyecto:** César Rueda — Campus CDE (`cesar-rueda-web`)  

---

## 📍 ESTADO ACTUAL: FASE 1 (VALIDACIÓN DE BORRADOR — 100% COMPLETADA)

- [x] Maquetación Mobile-First de la PWA con sticky bottom bar para el pulgar.
- [x] Integración del Escáner Interactivo de Lealtades Familiares (3 pasos).
- [x] Integración de la fotografía oficial de César Rueda en Base64 y metadatos OpenGraph.
- [x] Modal accesible de Aviso de Privacidad con cumplimiento LFPDPPP y RGPD (Zero-PII).
- [x] Optimización GEO con bloque Answer-First de 45 palabras para Google AI Overviews y Perplexity.
- [x] Schema.org JSON-LD con `ProfessionalService` (monedas MXN, USD, EUR) y `FAQPage`.
- [x] Suite de verificación automatizada (`verify_draft.py`) con 8 checks pasando al 100%.
- [x] Despliegue en vivo verificado `200 OK` en [cesar-rueda-draft.netlify.app](https://cesar-rueda-draft.netlify.app/).
- [x] Repositorio Git independiente configurado y sincronizado en [github.com/thetebis-wq/cesar-rueda-web](https://github.com/thetebis-wq/cesar-rueda-web).

---

## 🎯 PRÓXIMAS FASES DE DESARROLLO

### 🟡 FASE 2: LANZAMIENTO PILOTO Y CONVERSIÓN ACTIVA (EN CURSO)
- [ ] **Validación con Julio & César:**
  - Compartir enlace activo y recopilar feedback sobre precios y textos.
  - Confirmar el número oficial de WhatsApp definitivo para recepción de pacientes (`+52 55 7433 3257`).
- [ ] **Configuración de Dominio Personalizado:**
  - Definir si se adquiere dominio propio (ej. `cesarruedaterapia.com`, `cesarrueda-cde.com`) y asociarlo mediante DNS en Netlify o Firebase Hosting.
- [ ] **Grabación de Guiones de Video:**
  - Facilitar a César el Pack de Guiones virales (`docs/MARKETING_AND_SALES_STRATEGY.md`) para publicar sus primeros 3 videos en TikTok e Instagram Reels.
- [ ] **Configuración de Respuestas Rápidas en WhatsApp Business:**
  - Cargar los atajos `/saludo`, `/sesion` y `/agenda` en el dispositivo de César.

---

### 🟢 FASE 3: AUTOMATIZACIÓN DE AGENDA Y PAGOS
- [ ] **Integración de Cal.com / Calendly (Free Tier):**
  - Conectar el calendario de Google de César para disponibilidad de 60-90 min.
  - Generar enlaces directos para agendar citas después de la calificación por WhatsApp.
- [ ] **Pasarela de Cobro Internacional:**
  - Configurar cuenta de Stripe / PayPal para recibir cobros en Euros (€) y Dólares ($) de pacientes fuera de México.
  - Integrar link de pago en la confirmación de la cita.
- [ ] **Mini-CRM Gratuito en Google Sheets:**
  - Implementar webhook simple para registrar origen de prospectos (UTM) y fecha de contacto sin violar privacidad Zero-PII.

---

### 🔵 FASE 4: AGENTES DE IA Y ESCALABILIDAD (CAMPUS CDE)
- [ ] **Prototipo de Agente IA de Calificación (Lead Qualifier Agent):**
  - Agente con Google Gemini 2.0 Flash conectado a WhatsApp Cloud API para atender dudas 24/7 y filtrar pacientes.
- [ ] **Booking & Dispatch Agent:**
  - Automatización del envío del link de Google Meet tras confirmar el pago.
- [ ] **Plataforma Educativa Campus CDE (Futuro):**
  - Módulo para alumnos y terapeutas en formación con base de casos anonimizados (Zero-PII).
