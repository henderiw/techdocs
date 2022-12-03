# packer

## introduction

builds machine images cross platform

- golden image
- machine image

platform: aws, gcp, etc
confgiration mgmt: ansible
os/distribution: linux

by providing templates

## why use packer

create images via packer
automate
identical images cross platform

## packer breakdown

- builder: what tells packer the platform, api key info and desired 
- provisioner: chef, puppel or salt or files or ansible
- post-precssor: related to the builder
- communicator: by default this is SSH, WINRM for windows

terminology:

build -> create a machine image; a template
artifact -> machine image or meta data files
command -> packer build

## installation

## environment configuration

## packer plugins

- binary
- clone a repo and build the binary
- location of binary
  - /usr/bin            -> for all users globally
  - ~/.packer.d/plugins -> local directory
- name of binary:
  - packer-<type>-name
  - type can be: 
    - builder
    - provisioner
    - post-processor

## builders

different builders for different cloud environments

-> see packer file

## provisioners



## cli

### validate

packer validate packer.json
packer fix packer.json

