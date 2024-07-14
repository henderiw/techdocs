

sudo sysctl -w vm.nr_hugepages=102400

grep Huge /proc/meminfo



echo 512 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
echo 16 |sudo tee /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages
echo 16 |sudo tee /sys/kernel/mm/hugepages/hugepages-1048576kB/free_hugepages

```

sudo vi /etc/default/grub

->
GRUB_CMDLINE_LINUX_DEFAULT="default_hugepagesz=1G hugepagesz=1G hugepages=16"
GRUB_CMDLINE_LINUX="hugepagesz=1G hugepages=16 hugepagesz=2M hugepages=0"
->

sudo update-grub
```