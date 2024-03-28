# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "bridge" do |bridge|
      bridge.vm.box = "ubuntu/jammy64"
      bridge.vm.network "public_network", ip: "172.16.0.2"
      bridge.vm.network "private_network", ip: "192.168.100.2"
      bridge.vm.hostname = "bridge"
      bridge.vm.provider "virtualbox" do |v|
        v.name = "bridge"
        v.memory = 2048
        v.cpus = 1
      end
       bridge.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "playbook_bridge.yaml"
        ansible.inventory_path = "./inventory/bridgeserver.yaml"
      end
    end 
  config.vm.define "dbserver" do |dbserver|
      dbserver.vm.box = "ubuntu/jammy64"
      dbserver.vm.network "private_network", ip: "192.168.100.3"
      dbserver.vm.network "private_network", ip: "192.168.101.3"
      dbserver.vm.hostname = "dbserver"
      dbserver.vm.provider "virtualbox" do |v|
        v.name = "dbserver"
        v.memory = 2048
        v.cpus = 1
      end
      dbserver.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "playbook_dbserver.yml"
        ansible.inventory_path = "./inventory/dbserver.yaml"
      end
    end
end     
#    config.vm.define "web" do |web|
#      web.vm.box = "ubuntu/jammy64"
#      web.vm.network "private_network", ip: "192.168.100.4"
#      web.vm.network "public_network", ip: "192.168.102.4"
#     web.vm.provision "ansible" do |ansible|
#       ansible.verbose = "v"
#       ansible.playbook = "playbook_web.yml"
#      web.vm.hostname = "web"
#      web.vm.provider "virtualbox" do |v|
#        v.name = "web"
#        v.memory = 2048
#        v.cpus = 1
#      end
#    end
#end