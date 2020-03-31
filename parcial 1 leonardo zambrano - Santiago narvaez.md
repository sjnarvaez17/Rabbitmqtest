### Leonardo Zambrano Cifuentes - A00027552
### Santiago José Narváez Prado - A0027544

## Primer parcial Sistemas Distribuidos

### Procedimiento:
#### Primero se realizó la configuración del vagrantFile, donde se indicaba las direcciones ip de las máquinas que se usarán, los puertos de comunicación y los nombres de las maquinas virtuales. Se puede evidenciar la configuración en la imagen VagrantFile-1 y VagrantFile-2

#### VagrantFile-1
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/VagrantFile-1.PNG">

#### VagrantFile-2
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/VagrantFile-2.PNG
">

#### Luego, se realizó la configuración de Ansible, el cual servirá para provisionar el servicio a las máquinas. Para eso se usó RabbitMQ el cual nos va a permitir tener la funcionalidad de 'productor de mensajes' (imagen serverYml-1, serverYml-2, serverYml-3) y de 'consumidor de mensajes' (serverYml-5).

<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/serverYml-1.PNG
">
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/serverYml-2.PNG
">
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/serverYml-3.PNG
">
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/serverYml-4.PNG
">
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/serverYml-5.PNG
">

### Problemas
#### - El principal problema fué que Ansible no es soportado por Windows 10 y nos lanzaba el error que se evidencia en la imagen 'ansible not supported', el cual ocurría despues de ejecutar el comando 'vagrant up'.
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/vagrant%20up.PNG
">

<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/ansible%20not%20supported.PNG
">

#### Para esto, se intentó instalar por medio del comando 'conda install ansible', el cual tampoco cumplió con el objetivo. Así mismo, se usó el comando 'pip install git+git://github.com/ansible/ansible.git@devel', sin embargo, salió el error que se evidencia en la imagen 'install github ansible error'

<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/conda%20install%20ansible.PNG
">
<img srchttps://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/install%20github%20ansible.PNG
">
<img src="https://github.com/sjnarvaez17/Rabbitmqtest/blob/master/parcialuno/Im%C3%A1genes%20del%20c%C3%B3digo/install%20github%20ansible%20error.PNG
">

