# Edulibre

## Descripción General

**Edulibre** es una plataforma web educativa inspirada en la experiencia de aprendizaje de Duolingo, dirigida a adultos mayores colombianos. Su objetivo es facilitar el acceso a la educación digital, con una experiencia motivadora, gamificada y adaptada a las necesidades de este público. El proyecto busca reducir la brecha digital y promover el aprendizaje continuo, usando tecnología accesible y moderna.

---

## Visión Futura

En el futuro, Edulibre funcionará como una aplicación web progresiva (PWA) que permitirá a los usuarios:
- Registrarse y comenzar su camino de aprendizaje en minutos.
- Seguir rutas de aprendizaje temáticas, con retos y recompensas.
- Acceder a contenido extra y recursos de ayuda desde cualquier dispositivo.
- Recibir motivación constante a través de mensajes y animaciones.
- Contar con una experiencia personalizada, inclusiva y fácil de usar.

---

## Arquitectura Propuesta y Herramientas por Épica

### 1. Experiencia Inicial tipo Duolingo
**Objetivo:** Crear una primera impresión atractiva y motivadora.

**Herramientas/Arquitectura:**
- **Frontend:** React.js + Vite, usando componentes modulares y Styled Components para UI.
- **Animaciones:** Framer Motion o Lottie para animaciones ligeras y atractivas.
- **Diseño:** Figma para wireframes y prototipos interactivos.
- **Internacionalización:** react-i18next para textos adaptables.

### 2. Flujo de Registro y Login Simplificado
**Objetivo:** Facilitar el acceso y la creación de cuenta.

**Herramientas/Arquitectura:**
- **Autenticación:** Firebase Auth o Auth0 para gestión segura y simple de usuarios.
- **UX:** Formularios con validaciones en vivo y feedback claro.
- **Backend:** Node.js + Express para API custom si es necesario.

### 3. Onboarding Interactivo y Tutorial Motivacional
**Objetivo:** Guiar y motivar al usuario en los primeros pasos.

**Herramientas/Arquitectura:**
- **Flujo:** React-router para navegación entre pantallas.
- **Tutorial:** Contenido interactivo en React, con pasos gamificados y barra de progreso.
- **Gamificación:** Sistema de puntos/recompensas en frontend, persistido en backend.

### 4. Visualización del Camino de Aprendizaje
**Objetivo:** Motivar mostrando progreso y objetivos.

**Herramientas/Arquitectura:**
- **Visualización:** D3.js o recharts para gráficos simples de progreso.
- **Backend:** MongoDB para almacenar rutas y progreso personalizado.
- **Sincronización:** Websockets para actualizaciones en tiempo real.

### 5. Primer Desafío Gamificado
**Objetivo:** Iniciar el aprendizaje con una experiencia divertida.

**Herramientas/Arquitectura:**
- **Motor de retos:** Microservicio en Node.js para gestión de ejercicios y retos.
- **Frontend:** Componentes de ejercicios interactivos en React.
- **Persistencia:** MongoDB para registrar intentos y resultados.

### 6. Mensajes Motivacionales y Animaciones
**Objetivo:** Mantener motivado al usuario.

**Herramientas/Arquitectura:**
- **Animaciones:** Lottie/Framer Motion para microinteracciones.
- **Mensajes:** Sistema de notificaciones push (OneSignal o Firebase Cloud Messaging).

### 7. Acceso a Contenido Extra desde Landing
**Objetivo:** Ofrecer valor incluso antes de registrarse.

**Herramientas/Arquitectura:**
- **Contenido Extra:** Repositorio CMS headless (Strapi, Contentful) para gestionar recursos.
- **Frontend:** Sección pública en la landing con acceso directo a recursos.

### 8. Footer y Enlaces de Ayuda
**Objetivo:** Proveer soporte y navegación adicional.

**Herramientas/Arquitectura:**
- **Footer:** Componente universal en React, con enlaces a soporte, ayuda y políticas.
- **Documentación:** Help Center básico integrado, posible integración futura con Zendesk.

---

## Diseño de Arquitectura General

```
┌───────────────────────────────┐
│        Usuario final          │
└─────────────┬─────────────────┘
              │
      ┌───────▼─────────┐
      │    Frontend     │
      │  (React + Vite) │
      └───────┬─────────┘
              │
      ┌───────▼──────────┐
      │    Backend API   │
      │ (Node.js/Express)│
      └───────┬──────────┘
              │
      ┌───────▼──────────┐
      │   Base de datos  │
      │    (MongoDB)     │
      └────────┬─────────┘
               │
      ┌────────▼─────────┐
      │   Servicios 3ros │
      │ (Firebase, CMS,  │
      │  Auth0, Helpdesk)│
      └──────────────────┘
```

---

## Documentación y Flujo de Trabajo

- **Wireframes y prototipos**: Se documentarán en Figma y se enlazarán en este repositorio.
- **Epics y issues**: Cada funcionalidad principal está desglosada en issues y sub-issues, siguiendo el flujo de usuario.
- **Commits y PRs**: Todo cambio significativo debe estar ligado a una issue y documentado en el mensaje de commit.
- **Manual de usuario**: Se incluirá una sección de ayuda para usuarios finales dentro del frontend y en la wiki del proyecto.
- **Arquitectura y decisiones técnicas**: Se documentarán en la carpeta `/docs/` con diagramas y justificaciones.

---

## Cómo contribuir

1. Clona el repositorio y revisa las issues activas.
2. Propón cambios mediante PRs asociados a una issue.
3. Sigue las guías de estilo y documentación del proyecto.

---

## Estado actual

El proyecto está en fase inicial de diseño y prototipado. Se invita a colaboradores, diseñadores y desarrolladores interesados en la educación inclusiva.

---

## Contacto y soporte

Para dudas, sugerencias o soporte, utiliza el footer en la aplicación o abre una issue en GitHub.

---

**¡Con Edulibre, aprender es libre, motivador y accesible para todos!**
