# Primer Examen Parcial.

Implemente una arquitectura que contenga:
 
 * un productor de mensajes (puede ser en la máquina física o en una máquina virtual)
 * Un broker de RabbitMQ (puede ser en la máquina física o en una máquina virtual)
 * Dos consumidores de mensajes (pueden ser en una máquina virtual o contenedores)
    * El primer consumidor recibirá los mensajes de la cola "Grupo 01"
    * El segundo consumidor recibirá los mensajes de la cola "Grupo 02"
    * Ambos consumidores recibirán los mensajes enviados al grupo "General"

### Actividades
1. Documento README.md en formato markdown:  
  * Formato markdown (5%).
  * Nombre y código del estudiante (5%).
  * Ortografía y redacción (5%).
2. Documentación del procedimiento para el aprovisionamiento del productor (10%). Evidencias del funcionamiento (5%).
3. Documentación del procedimiento para el aprovisionamiento de los consumidores (10%). Evidencias del funcionamiento (5%).
4. Documentación del procedimiento para el aprovisionamiento del broker (10%). Evidencias del funcionamiento (5%).
5. Documentación de las tareas de integración (10%). Evidencias de la integración (10%).
6. El informe debe publicarse en un repositorio de github el cual debe ser un fork de https://github.com/ICESI-Training/Rabbitmqtest y para la entrega deberá hacer un Pull Request (PR) al upstream (10%). Tenga en cuenta que el repositorio debe contener todos los archivos necesarios para el aprovisionamiento.
7. Documente algunos de los problemas encontrados y las acciones efectuadas para su solución al aprovisionar la infraestructura y aplicaciones (10%).
