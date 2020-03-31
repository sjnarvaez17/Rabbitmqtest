### Leonardo Zambrano Cifuentes - A00027552
### Santiago José Narváez Prado - A0027544

## Primer parcial Sistemas Distribuidos

### Procedimiento:
#### Primero se realizó la configuración del vagrantFile, donde se indicaba las direcciones ip de las máquinas que se usarán, los puertos de comunicación y los nombres de las maquinas virtuales. Se puede evidenciar la configuración en la imagen VagrantFile-1 y VagrantFile-2

<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/VagrantFile-1.PNG">

#### Luego, se realizó la configuración de Ansible, el cual servirá para provisionar el servicio a las máquinas. Para eso se usó RabbitMQ el cual nos va a permitir tener la funcionalidad de 'productor de mensajes' (imagen serverYml-1, serverYml-2, serverYml-3) y de 'consumidor de mensajes' (serverYml-5).

### Problemas
#### - El principal problema fué que Ansible no es soportado por Windows 10 y nos lanzaba el error que se evidencia en la imagen 'ansible not supported'. Para esto, se intentó instalar por medio del comando 'conda install ansible', el cual tampoco cumplió con el objetivo. Así mismo, se usó el comando 'pip install git+git://github.com/ansible/ansible.git@devel', sin embargo, salió el error que se evidencia en la imagen 'install github ansible error'

#### - Despues de ejecutar el comando 'vagrant up' salió el error que se puede evidenciar en la imagen 'ansible not supported'
