import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.20.110.72', port=22, username='root', password='1212')
stdin1, stdout1, stderr1 = ssh.exec_command('python3 /home/sch/cpu_record/cpu_avg_count.py')
stdin2, stdout2, stderr2 = ssh.exec_command('python3 /home/sch/cpu_record/mem_avg_count.py')
result_cpu = stdout1.read().decode('utf-8')
result_mem = stdout2.read().decode('utf-8')

if result_cpu > 60 and result_mem > 75:
    ssh.exec_command('docker update --cpus 2 -m 3.5g 946f')
    ssh.exec_command('docker update --cpus 6 -m 3.5g 5ec4')
    ssh.close()
else:
    ssh.exec_command('docker update --cpus 1 -m 2.5g 946f')
    ssh.exec_command('docker update --cpus 5 -m 2.5g 5ec4')
    ssh.close()
