import paramiko
import os
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='ip', username='username', password='password')
sftp_client=client.open_sftp()
#sftp_client.chdir("/home")
#print(sftp_client.getcwd())

#below command to coppy logs to server
#sftp_client.put('sid.txt', '/home/theatro/siddarth/sid.txt')
#below command to get log from server
sftp_client.get('/home/theatro/siddarth/sid.txt', 'sid.txt')
sftp_client.close()
client.close()
